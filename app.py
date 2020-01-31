"""Adopt application."""

from flask import Flask, render_template, redirect
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "Johnny Tightlips"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)
connect_db(app)
db.create_all()


@app.route('/')
def index():
    """Home Page"""

    pets = Pet.query.all()
    return render_template('index.html', pets=pets)


@app.route('/add')
def add_pets_form():
    """Add Pets Form"""

    return render_template('index.html', pets=pets)


@app.route('/add', methods=["POST"])
def add_pets_submit():
    """Add Pets Form"""

    return redirect('/')
