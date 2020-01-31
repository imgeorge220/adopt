from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange


class EditPetForm(FlaskForm):
    """Form for adding pets."""

    photo_url = StringField("Link to Photo", validators=[Optional(), URL()])
    notes = StringField("Notes")
    available = SelectField("Available?",
                            choices=[('True', 'Yes'), ('False', 'No')],
                            validators=[InputRequired()])


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species",
                          choices=[
                              ("Cat", "Cat"),
                              ("Dog", "Dog"),
                              ("Porcupine", "Porcupine")],
                          validators=[InputRequired()])
    photo_url = StringField("Link to Photo", validators=[Optional(), URL()])
    age = FloatField("Age (in people years)",
                     validators=[InputRequired(), NumberRange(min=0, max=30)])
    notes = StringField("Notes")
