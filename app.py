"""Adopt application."""

from flask import Flask, render_template, redirect
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm, EditPetForm
from petAPI import get_animal

app = Flask(__name__)
app.config['SECRET_KEY'] = "Johnny Tightlips"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)
connect_db(app)


@app.route('/')
def index():
    """Home Page"""

    animal = get_animal()
    print('**************', animal, '****************************')
    pets = Pet.query.all()
    return render_template('index.html', pets=pets)


@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Add Pets Form"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        age = form.age.data
        notes = form.notes.data
        photo_url = form.photo_url.data if form.photo_url.data else None

        new_pet = Pet(name=name, species=species, age=age,
                      photo_url=photo_url, notes=notes)

        db.session.add(new_pet)
        db.session.commit()

        return redirect('/')

    return render_template('add-pet-form.html', form=form)


@app.route('/<pet_id>', methods=["GET", "POST"])
def edit_pet(pet_id):
    """Pet Information Page"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.photo_url = form.photo_url.data if form.photo_url.data else pet.photo_url
        pet.available = form.available.data == 'True'

        db.session.commit()

        return redirect(f'/')

    return render_template('pet-info.html', pet=pet, form=form)
