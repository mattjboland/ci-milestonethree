## Online CookBook - An online cookbook App

    This is an Online Cookbook App, for Data Centric Milestone Three Project with Code Institute.

    Online Cookbook, is an App built using the Flask Framework with Python and MongoDB as the database. The purpose of
    this app is to allow users store and manage their recipes in an app using CRUD operation, Create, Read, Update and
    Delete.

    The deployed site can be found here.

## Table of Contents

1. **[UX]**

    * **[UserStories]**
    * **[Design]**
        * **[Framework]**
        * **[Database]**
        * **[Wireframes]**

2. **[Features]**

3. **[TechnologiesUsed]**

    * **[Languages]**
    * **[Libraries]**
    * **[Hosting]**

4. **[Testing]**

5. **[Deployment]**

6. **[Credits]**

    * **[Content]**
    * **[Acknowledgements]**

## UX

This is Milestone Three Project in Data Centric Development Module of the Full Stack Web Development by Code Institute.

As a qualified Pastry Chef, I found this project had a great meaning and purpose for me. I decided that I wanted to create
an app that could store recipes for me. Not only me that anyone interested could register and upload recipes, view and
try others. 

### User Stories

As a User to this app, I want to be able to do the following.

    * Gain access to an app to store my recipes
    * Upload recipes that I have used and would like to save/share
    * Be able to edit the recipes if a better method was found or similar
    * Be able to delete the recipe if it wasnt good
    * Have a database of recipes that could be searched for new ideas etc
    * Be able to view/search different categories of recipes
    * Have the ability to Login as a user and safely Logout

### Design

#### Framework

* **[Materialize 1.0.0](https://materializecss.com/)**

I used Materialize Framework for the layout and components, I prefer this Framework to the Bootstrap Framework althought
very similar in layout

* **[Flask 1.0.2](https://palletsprojects.com/p/flask/)**

I used Flask the micro web application Framework that actually runs the application

* **[jQuery 3.4.0](https://code.jquery.com/jquery/)**

jQuery is a JavaScript library which I used to simplify HTML DOM tree traversal and manipulation in my collapsible
popout, modal, icon rotate and buttons etc

#### Database

I used MongoDB for the database, This was used throughout the course material. MongoDB is a NoSQL database and was
perfect for my project. I found it very difficult to understand sometimes but with a little help from Slack and Guido
I  was able to improve my understanding. I still feel I could use some more learning and I have every intention to do 
so at a later stage.

I built up my collections in MongoDB and have listed them below.

## Categories

    _id: ObjectId("")                   _id: ObjectId("")
    category_name: "Starter"            category_name: "Main Course"

    _id: ObjectId("")                   _id: ObjectId("")
    category_name: "Dessert"            category_name: "Snack"

## Cuisines

    _id: ObjectId("")                   _id: ObjectId("")                   _id: ObjectId("")
    cuisine_name: "American"            cuisine_name: "British"             cuisine_name: "Caribbean"

    _id: ObjectId("")                   _id: ObjectId("")                   _id: ObjectId("")
    cuisine_name: "Chinese"             cuisine_name: "French"              cuisine_name: "Greek"

    _id: ObjectId("")                   _id: ObjectId("")                   _id: ObjectId("")
    cuisine_name: "Indian"              cuisine_name: "Italian"             cuisine_name: "Japanese"

    _id: ObjectId("")                   _id: ObjectId("")                   _id: ObjectId("")
    cuisine_name: "Mediterranean"       cuisine_name: "Mexican"             cuisine_name: "Moroccan"

    _id: ObjectId("")                   _id: ObjectId("")                   _id: ObjectId("")
    cuisine_name: "Spanish"             cuisine_name: "Thai"                cuisine_name: "Turkish"

    _id: ObjectId("")                   _id: ObjectId("")                   _id: ObjectId("")
    cuisine_name: "Vietnamese"          cuisine_name: "Fusion"              cuisine_name: "Vegan"

    _id: ObjectId("")
    cuisine_name: "Vegetarian"

## Recipes

    _id: ObjectId("")
    recipe_title: "title" <string>
    recipe_description: "description" <string>
    recipe_method: "method" <array>
    recipe_ingredients: "ingredients" <array>
    recipe_serves: "serves" <string>
    recipe_cookingtime: "cookingtime" <string>
    recipe_preptime: "preptime" <string>
    recipe_cuisine: "cuisine" <array>

## Users

    _id: ObjectId("")
    username: ""
    password: ""

## Allergens

    _id: ObjectId("")                   _id: ObjectId("")                   _id: ObjectId("")
    allergen_name: "Cereals.. Gluten"   allergen_name: "Crustaceans"        allergen_name: "Eggs"

    _id: ObjectId("")                   _id: ObjectId("")                   _id: ObjectId("")
    allergen_name: "Fish"               allergen_name: "Peanuts"            allergen_name: "Soya"

    _id: ObjectId("")                   _id: ObjectId("")                   _id: ObjectId("")
    allergen_name: "Milk"               allergen_name: "Nuts"               allergen_name: "Celery"

    _id: ObjectId("")                   _id: ObjectId("")                   _id: ObjectId("")
    allergen_name: "Mustard"            allergen_name: "Sesame Seeds"       allergen_name: "Sulphur Dioxide and Sulphites"

    _id: ObjectId("")                   _id: ObjectId("")                   _id: ObjectId("")
    allergen_name: "Lupin"              allergen_name: "Molluscs            allergen_name: "None"

    
