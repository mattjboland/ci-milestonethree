import os
import math
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Pagination and sorting
PAGE_SIZE = 8
KEY_PAGE_SIZE = 'page_size'
KEY_PAGE_NUMBER = 'page_number'
KEY_TOTAL = 'total'
KEY_PAGE_COUNT = 'page_count'
KEY_ENTITIES = 'items'
KEY_NEXT = 'next_uri'
KEY_PREV = 'prev_uri'
KEY_WORD_FIND = 'word_find'
KEY_ORDER_BY = 'order_by'
KEY_ORDER = 'order'


def get_paginated_list(entity, query={}, **params):
    page_size = int(params.get(KEY_PAGE_SIZE, PAGE_SIZE))
    page_number = int(params.get(KEY_PAGE_NUMBER, 1))
    order_by = params.get(KEY_ORDER_BY, '_id')
    order = params.get(KEY_ORDER, 'asc')
    order = pymongo.ASCENDING if order == 'asc' else pymongo.DESCENDING
    if page_number < 1:
        page_number = 1
    offset = (page_number - 1) * page_size
    items = []
    word_find = ''
    if KEY_WORD_FIND in params:
        word_find = params.get(KEY_WORD_FIND)
        if len(word_find.split()) > 0:
            entity.create_index([("$**", 'text')])
            result = entity.find({'$text': {'$search': word_find}})
            items = result.sort(order_by, order).skip(offset).limit(page_size)
        else:
            items = entity.find().sort(
                order_by, order
            ).skip(offset).limit(page_size)
    else:
        items = entity.find(query).sort(order_by, order).skip(
            offset).limit(page_size)
    total_items = items.count()
    if page_size > total_items:
        page_size = total_items
    if page_number < 1:
        page_number = 1
    if page_size:
        page_count = math.ceil(total_items / page_size)
    else:
        page_count = 0
    if page_number > page_count:
        page_number = page_count
    next_uri = {
        KEY_PAGE_SIZE: page_size,
        KEY_PAGE_NUMBER: page_number + 1
    } if page_number < page_count else None
    prev_uri = {
        KEY_PAGE_SIZE: page_size,
        KEY_PAGE_NUMBER: page_number - 1
    } if page_number > 1 else None

    return {
        KEY_TOTAL: total_items,
        KEY_PAGE_SIZE: page_size,
        KEY_PAGE_COUNT: page_count,
        KEY_PAGE_NUMBER: page_number,
        KEY_NEXT: next_uri,
        KEY_PREV: prev_uri,
        KEY_WORD_FIND: word_find,
        KEY_ORDER_BY: order_by,
        KEY_ORDER: order,
        KEY_ENTITIES: items
        }


@app.route('/')
@app.route('/get_recipes', methods=['GET'])
def get_recipes():
    paginated_recipes = get_paginated_list(
        mongo.db.recipe, **request.args.to_dict())
    return render_template(
        "recipes.html", recipes=paginated_recipes)


@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form.get("query")
    return render_template(
        "recipes.html", recipes=list(
            mongo.db.recipe.find({"$text": {"$search": query}})))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # check if username exists in mongodb
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put new user into a session cookie
        session['user'] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check username exists in mongodb
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
               existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from mongodb
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies or log out
    flash("You have been Logged Out!")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "category_name": request.form.get("category_name"),
            "allergen_name": request.form.get("allergen_name"),
            "recipe_title": request.form.get("recipe_title"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_method": request.form.getlist("method[]"),
            "recipe_ingredients": request.form.getlist("ingredients[]"),
            "recipe_serves": request.form.get("recipe_serves"),
            "recipe_cookingtime": request.form.get("recipe_cookingtime"),
            "recipe_preptime": request.form.get("recipe_preptime"),
            "recipe_cuisine": request.form.getlist("cuisine_name"),
            "created_by": session["user"]
        }
        mongo.db.recipe.insert_one(recipe)
        flash("Recipe Sucessfully Added!")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)

    cuisines = mongo.db.cuisines.find().sort("cuisine_name", 1)

    allergens = mongo.db.allergens.find().sort("allergen_name", 1)
    return render_template("add_recipe.html", categories=categories,
                           cuisines=cuisines, allergens=allergens)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "allergen_name": request.form.get("allergen_name"),
            "recipe_title": request.form.get("recipe_title"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_method": request.form.getlist("method[]"),
            "recipe_ingredients": request.form.getlist("ingredients[]"),
            "recipe_serves": request.form.get("recipe_serves"),
            "recipe_cookingtime": request.form.get("recipe_cookingtime"),
            "recipe_preptime": request.form.get("recipe_preptime"),
            "recipe_cuisine": request.form.getlist("recipe_cuisine"),
            "created_by": session["user"]
        }
        mongo.db.recipe.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Sucessfully Updated!")

    recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})

    categories = mongo.db.categories.find().sort("category_name", 1)

    cuisines = mongo.db.cuisines.find().sort("cuisine_name", 1)

    allergens = mongo.db.allergens.find().sort("allergen_name", 1)
    return render_template("edit_recipe.html", recipe=recipe,
                           categories=categories, cuisines=cuisines,
                           allergens=allergens)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipe.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted!!")
    return redirect(url_for("get_recipes"))


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added!")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated!")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted!")
    return redirect(url_for("get_categories"))


@app.route("/request_category", methods=["GET", "POST"])
def request_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(request)
        flash("New Category Added!")
        return redirect(url_for("get_categories"))

    return render_template("request_category.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
