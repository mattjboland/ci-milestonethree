## Online CookBook - An online cookbook App

    This is an Online Cookbook App, for Data Centric Milestone Three Project with Code Institute.

    Online Cookbook, is an App built using the Flask Framework with Python and MongoDB as the database.
    The purpose of this app is to allow users store and manage their recipes in an app using CRUD 
    operation, Create, Read, Update and Delete.

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

   #### Wireframes

   I used [Balsamiq Wireframes](https://balsamiq.com/) for the Mockup Wireframes during the scope plan planning for this
   website / App. I have never used Balsamiq before but it is a great tool for planning stages and really help you with
   design aspects of the website. It give you a real feel and look at a plan and make it easier to visualise.

   All the wireframes for this project can be found here in [wireframes].(https://github.com/mattjboland/ci-milestonethree/tree/master/static/wireframes)

## Features

* Navigation Bar

    The NavBar used is this project is a Materialize NavBar. It provide the links between the various different pages on
    site. On the left is the name Online CookBook and this also acts as the Home button bringing the user bacl to the Home
    Page.

    When a user is not logged in or registered they have the following options on the NavBar.

    * Home
    * Log In
    * Register

    When a user is logged in they have the following options.

    * Home
    * Profile
    * New Recipe
    * Request Category
    * Log Out

    When the user is and Admin they have and extra option. 

    * Manage Categories

    These collapse into a Burger Bar when smaller screens are used and the Side NavBar is activated. This will display
    the options and links as a NavBar would but it will pop out from the side.

* Description 

    This is a brief description of the app and how it works and what the app does.

* Search

    This allows the users to search for recipes or keywords and have the results displayed. They can the view the 
    recipes and read through the steps etc. 

* Register

    Allows any user or visitor to register or sign up to the app. There is a link to the log in if the user has
    already registered.

* Log In

    When Registered users can log in using the username and password that they created on registering. There is also
    a link to the register page if a user has not registered.

* Log Out 

    Users can easily log out at any time.

* Add Recipe (CREATE)

    Users can add a recipe when logged in by using the form and selecting from the various dropdowns. The form field
    is well structured and layout for ease od adding recipes. It is clear the steps the user needs to take to add a recipe
    and when the form is filled out correctly they can add the recipe using the add recipe button at the bottom of the 
    form. This is the CREATE part for the CRUD functionality

* View Recipe (READ)

    Users can search and read all recipes including their own easily either on the home page or by searching. All recipes
    will be displayed whether the user has searched for a specific recipe. The logged in user will have the extra ability
    to edit or delete their recipes as the buttone will be displayed easily identifying which recipe belongs to the user.
    This is the READ part for the CRUD functionality.

* Edit Recipe (UPDATE)

    Similarly to the view above when a logged in user searches a recipe and decides to edit, a simple click of the edit
    button and this will bring the user to a page displaying the original recipe preloaded on the form available for 
    editing. All fields may be edited and some may need reconfirming. The edit allows you to add more ingredients but
    also delete unneccesary ones as well as the same for methods. This is the UPDATE part for the CRUD functionality.

* Delete Recipe (DELETE)

    The user can also delete the recipe if he/she wishes. Only the author/creator of the recipe may delete just like the 
    edit. When deleting a recipe and popup confirmation modal will display as a final warning to make sure that the user
    really wants to delete. This is the DELETE part for the CRUD functionality.

* Recipe Display

    This displays the recipes for all viewers to see. A logged in user will be able to edit and delete their owns recipes
    as the display will show the edit and delete buttons. Only the creator or the author of any recipe will only be able
    to edit and delete their own recipe, so any user will not be able to edit or delete anyone elses recipe.

* Footer

    A simple footer with the name of the app again like above amd some Copyright info. There is social links there to 
    allow the user to visit the social media sites of the App or App Author, but for now they just bring the user to 
    the home page of each social media outlet. The final link is to the Authors GitHub, where users can view others
    projects created by the Author.

* Flashed Messages

    Flashed messages are used throughout this app, this is a feature of Flask. It is used to help the user have a better
    overall experence and to provide some feedback to the user. For example if a new user registers and picks a user name
    that has already been used they will see a flashed message saying "Username already exists". Similarly if the user
    logs in with an incorrect username or password, they will see "Incorrect Username and/or Password". There are various
    examples of this across the app to prompt the user.

* Features for future development of the app, I would have like to include a bit more to this app but unfortunately I was
    out of time. I struggled with this project and that really hindered my timing as everything too quite a bit longer to
    to get right and fully understand. I would have like to include a feature where the user would like or dislike a 
    recipe or give it a rating of some sort, maybe 3 out of 5 stars or something similar. I would have also like to 
    a picture that could be uploaded with the recipe and stored in the database too. Maybe even a forum or chat feature
    various users could chat and talk about experiences with their recipes or to be able to look for help with other 
    recipes. I would also like to include the proper connection of an email to the app creator about suggestions for new
    categories to be added.  

## Technologies Used

    These are the following Technologies that were used to develop the app and are used throughout the app.

### Languages

* [HTML](https://html.com/) This was used as the Markup Language for the app.
* [CSS](https://www.w3.org/Style/CSS/Overview.en.html) CSS was used for styling.
* [Python](https://www.python.org/) This was used in the Backend due to its easy read ability and also at its versatile.
* [JavaScript](https://www.javascript.com/) This was used to manipulate the DOM and to add dynamic Features.

#### Dependencies

    There is a list of Dependencies required to run the app, these packages are listed in the requirements.txt file.
    These can be installed by typing the following statement into the terminal and pressing enter.

### Libraries

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) This is the Micro Web Framework that runs the application.
* [Pymongo](https://pypi.org/project/pymongo/) This was used to help Python access the database.
* [Materialize](https://materializecss.com/) This framework was used to build and style the application.
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) This is the templating Language used by Flask and this is used to display in the HTML by Python.
* [jQuery](https://jquery.com/) This was used for event handling along with JavaScript. 
* [FontAwesome](https://fontawesome.com/) This was used to display some cool icons used in the app. 
* [GoogleFonts](https://fonts.google.com/) This was used for the font throughout the app.

### Tools 

* [MongoDBAtlas](https://www.mongodb.com/cloud/atlas) This was used as the database for the app.
* [GitPod](https://www.gitpod.io) This was used as the IDE to build the app.
* [GitHub](https://github.com/) This was used for hosting software development and version control using Git.
* [Git](https://git-scm.com/) This was used for version control.
* [Balsamiq](https://balsamiq.com/) This was used for wireframes when starting off the planning.

### Hosting

* [Heroku](https://www.heroku.com/) This was used to host the app.

## Testing

    I have thoroughly testing the Log in features as well as Log out, Register, Add Recipe, Edit Recipe and Delete
    Recipe. These are all working as they should and have no issues. I have also asked some friends to check the
    app too and all have been able to use the app easily with no issues.

### Issues and Bugs

## Deployment

## Credits

* Content
* Media 
* Acknowledgements
