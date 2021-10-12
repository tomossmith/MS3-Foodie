import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# GLOBAL VARIABLES
@app.context_processor
def get_categories():
    categories = list(mongo.db.categories.find())
    return dict(categories=categories)

# LANDING PAGE


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

# USER AUTHENTICATION

# REGISTER


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # CHECK IF USERNAME ALREADY EXISTS IN DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Sorry, This Username already exists!")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email").lower(),
        }
        mongo.db.users.insert_one(register)

        # PLACE NEW USER INTO 'SESSION COOKIE'
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")

# LOGIN


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")

# PROFILE PAGE
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # GET THE USER'S USERNAME FROM THE DATABASE
    username = mongo.db.users.find_one({
        "username": session["user"]})["username"]
    return render_template("profile.html", username=username)

# LOGOUT
@app.route("/logout")
def logout():
    # REMOVE THE USER SESSION COOKIE
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))

# RECIPE BOOK
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)

# INDIVIDUAL RECIPE PAGE
@app.route("/open_recipe/<recipe_id>")
def open_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id":  ObjectId(recipe_id)})
    return render_template("open_recipe.html", recipe=recipe)

# RECIPE PAGE BY TYPE
#@app.route("/recipes_by_type/<category_id>")
#def recipes_by_type(category_id):
#    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
#    recipes = mongo.db.recipes.find({"category_name": category["category_name"]})
#    return render_template("recipes_by_type.html", recipes=recipes,
#    category=category)

@app.route("/recipes_by_type/<category_id>")
def recipes_by_type(category_id):
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    """
    Only return recipes where recipe[category_name]
    matches category[category_name]
    """
    recipes = mongo.db.recipes.find(
        {"category_name": category["category_name"]})
    count = recipes.count()
    return render_template("recipes_by_type.html", recipes=recipes,
                           category=category, count=count)

# ADD RECIPE
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        user = mongo.db.users.find_one({"username": session["user"]})
        recipe = {
            "submitted_by": ObjectId(user["_id"]),
            "recipe_name": request.form.get("recipe_name"),
            "category_name": request.form.get("category_name"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_image_url": request.form.get("recipe_image_url"),
            "recipe_serving": request.form.get("recipe_serving"),
            "recipe_cook_time": request.form.get("recipe_cook_time"),
            "recipe_difficulty": request.form.get("recipe_difficulty"),
            "recipe_spice": request.form.get("recipe_spice"),
            "recipe_ingredients": request.form.getlist("recipe_ingredients"),
            "recipe_instructions": request.form.getlist("recipe_instructions"),
            "recipe_user": session["user"],
            "recipe_create_date": datetime.datetime.now(),
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Your Recipe Was Successfully Added To The Cookbook!")
        return redirect(url_for("profile", username=session["user"]))
    
    return render_template("add_recipe.html")


# EDIT RECIPE
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        user = mongo.db.users.find_one({"username": session["user"]})
        submit = {
            "submitted_by": ObjectId(user["_id"]),
            "recipe_name": request.form.get("recipe_name"),
            "category_name": request.form.get("category_name"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_image_url": request.form.get("recipe_image_url"),
            "recipe_serving": request.form.get("recipe_serving"),
            "recipe_cook_time": request.form.get("recipe_cook_time"),
            "recipe_difficulty": request.form.get("recipe_difficulty"),
            "recipe_spice": request.form.get("recipe_spice"),
            "recipe_ingredients": request.form.getlist("recipe_ingredients"),
            "recipe_instructions": request.form.getlist("recipe_instructions"),
            "recipe_modify_date": datetime.datetime.now(),
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Your Recipe Was Successfully Updated To The Cookbook!")

    recipe = mongo.db.recipes.find_one({"_id":  ObjectId(recipe_id)})
    return render_template("edit_recipe.html", recipe=recipe)


# DELETE RECIPE
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_recipes"))

# CATEGORIES LIST
@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find())
    return render_template("categories.html", categories=categories)

# ADD CATEGORY
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name"),
            "category_image": request.form.get("category_image"),
        }
        mongo.db.categories.insert_one(category)
        flash("The Category Was Successfully Added")
        return redirect(url_for("get_categories"))
    
    return render_template("add_category.html")

# EDIT CATEGORY
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = mongo.db.categories.find_one({"_id":  ObjectId(category_id)})
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "category_image": request.form.get("category_image"),
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("The Category Was Successfully Updated")
        return redirect(url_for("get_categories"))
 
    return render_template("edit_category.html", category=category)

# DELETE CATEGORY
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug="True")

# CHANGE TO FALSE BEFORE FINAL DEPLOYMENT
