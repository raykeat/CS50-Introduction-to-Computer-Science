import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    return apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    #check if request method is get
    if request.method=="GET":
        return render_template("buy.html")
    else:

        #check if any symbol was entered into the form
        if not request.form.get("symbol"):
            return apology("please enter symbol")

        #check if symbol exists using lookup function in helper.py
        symbol = request.form.get("symbol")
        if lookup(symbol.upper())==None:
            return apology("Stock symbol does not exist")

        #check if no of shares entered was positive
        shares = int(request.form.get("shares"))
        if shares<=0:
            return apology("Please enter a positive integer")

        #look up a stock's current price
        stock=lookup(symbol.upper())
        price=stock["price"]

        #calculate transaction value
        transaction_value = shares * price

        #select amount of cash user has
        user_id=session["user_id"]
        user_cash_db=db.execute("SELECT cash FROM users WHERE id=user_id")
        user_cash = user_cash_db[0]["cash"]

        if user_cash<transaction_value:
            return apology("NOT ENOUGH CASH TO BUY")

        return redirect("/")







    return apology("TODO")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method=="GET":
        return render_template("quote.html")

    if request.method=="POST":
        symbol=request.form.get("symbol")

        if not symbol:
            return apology("please enter stock tickerrrr")

        stock = lookup(symbol.upper())

        if stock == None:
            return apology("Symbol does not exist")



        return render_template("quoted.html", name = stock["name"], price = usd(stock["price"]), symbol = stock["symbol"])






@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    #check if request method is get
    if request.method=="GET":
        return render_template("register.html")

    #check if request method is post
    if request.method=="POST":


        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        #check if username was entered
        if not username:
            return apology("Please enter username")

        #check if password was entered
        if not password:
            return apology("Please enter password")

        #check if password confirmation was entered
        if not confirmation:
            return apology("Please enter confirmation")

        if password!=confirmation:
            return apology("password and confirmation do not match!")

        #creating a hashed password
        hash = generate_password_hash(password)

        #add user into our SQL database
        try:
            newuser=db.execute("INSERT INTO users(username,hash) VALUES(?,?)", username,hash)
        except:
            return apology("username already exists")

        #remember a user's session lmao
        session["user_id"] = newuser

        return redirect("/")




@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")
