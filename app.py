import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
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

# RECIPE PAGES
# RECIPE BOOK


@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)

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
            "recipe_serving": request.form.get("recipe_serving"),
            "recipe_cook_time": request.form.get("recipe_cook_time"),
            "recipe_difficulty": request.form.get("recipe_difficulty"),
            "recipe_spice": request.form.get("recipe_spice"),
            "recipe_ingredients": request.form.getlist("recipe_ingredients"),
            "recipe_instructions": request.form.getlist("recipe_instructions"),
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Your Recipe Was Successfully Added To The Cookbook!")
        return redirect(url_for("profile", username=session["user"]))
    
    return render_template("add_recipe.html")

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug="True")

# CHANGE TO FALSE BEFORE FINAL DEPLOYMENT
