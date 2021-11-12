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
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)

# HOME

@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)

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
        }
        mongo.db.users.insert_one(register)

        # PLACE NEW USER INTO 'SESSION COOKIE'
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("my_recipes", username=session["user"]))
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
                            "my_recipes", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")

# LOGOUT
@app.route("/logout")
def logout():
    # REMOVE THE USER SESSION COOKIE
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))

# ADMIN FEATURES

@app.route("/get_admins")
def get_admins():
    admins = list(mongo.db.admins.find())
    return render_template("admins.html", admins=admins)

# ADD ADMINISTRATOR
@app.route("/add_admin", methods=["GET", "POST"])
def add_admin():
    if request.method == "POST":
        admins = {
            "username": request.form.get("admin_username"),
        }
        mongo.db.admins.insert_one(admins)
        flash("Administrator Was Successfully Added To The Website Access List!")
        return redirect(url_for("get_admins", admins=admins))
    
    return render_template("add_admin.html")

# DELETE ADMIN
@app.route("/delete_admin/<admin_id>")
def delete_admin(admin_id):
    mongo.db.admins.remove({"_id": ObjectId(admin_id)})
    flash("Administrator Successfully Deleted")
    return redirect(url_for("get_admins"))

# RECIPE SEARCH FUNCTION
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


# MY RECIPES
@app.route("/my_recipes/<username>", methods=["GET", "POST"])
def my_recipes(username):
    # GET THE USER'S USERNAME FROM THE DATABASE
    user_id = mongo.db.users.find_one({
        "username": session["user"]})["_id"]
    recipes = mongo.db.recipes.find(
        {"submitted_by": user_id})
    count = recipes.count()
    return render_template("my_recipes.html", username=username, recipes=recipes, count=count)

# INDIVIDUAL RECIPE PAGE
@app.route("/open_recipe/<recipe_id>")
def open_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id":  ObjectId(recipe_id)})
    return render_template("open_recipe.html", recipe=recipe)

# RECIPES BY TYPE
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
        return redirect(url_for("my_recipes", username=session["user"]))
    
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
    return redirect(url_for("my_recipes", username=session["user"]))

# CATEGORIES LIST
@app.route("/get_categories", methods=["GET", "POST"])
def get_categories():
# check if admin username exists in db
    admin_user = mongo.db.admins.find_one({"username": session["user"]})
    if admin_user:
        categories = list(mongo.db.categories.find())
        return render_template("categories.html", categories=categories)

    return render_template("no_auth.html")

# ADD CATEGORY
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
# check if admin username exists in db
    admin_user = mongo.db.admins.find_one({"username": session["user"]})
    if admin_user:
        if request.method == "POST":
            category = {
                "category_name": request.form.get("category_name"),
                "category_image": request.form.get("category_image"),
            }
            mongo.db.categories.insert_one(category)
            flash("The Category Was Successfully Added")
            return redirect(url_for("get_categories"))
        return render_template("add_category.html")
    
    return render_template("no_auth.html")

# EDIT CATEGORY
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
# check if admin username exists in db
    admin_user = mongo.db.admins.find_one({"username": session["user"]})
    if admin_user:
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
            
    return render_template("no_auth.html")

# DELETE CATEGORY
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
# check if admin username exists in db
    admin_user = mongo.db.admins.find_one({"username": session["user"]})
    if admin_user:
        mongo.db.categories.remove({"_id": ObjectId(category_id)})
        flash("Category Successfully Deleted")
        return redirect(url_for("get_categories"))
    
    return render_template("no_auth.html")

# ERROR PAGES:
# https://flask.palletsprojects.com/en/2.0.x/errorhandling/

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug="True")

# CHANGE TO FALSE BEFORE FINAL DEPLOYMENT
