from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, NumberRange, url

class AddPetForm(FlaskForm):
    """add pet form"""
    name=StringField("Pet Name", validators=[InputRequired('Pet name cannot be blank')])
    
    species=SelectField("Species", choices=[('cat', 'cat'), ('dog', 'dog'), ('porcupine', 'porcupine')], validators=[InputRequired('Species cannot be left blank')])
    
    photo_url=StringField("Picture of Pet", validators=[url(require_tld=False, message="Please use a valid url for photo")])
    
    age=IntegerField("Age of Pet", validators=[NumberRange(min=0, max=30, message="Age must be at least 0 but no more than 30")])
    
    notes=StringField("Important Notes About Pet")

class EditPetForm(FlaskForm):
        """edit pet form"""
        photo_url=StringField("Picture of Pet", validators=[url(require_tld=False, message="Please use a valid url for photo")])
        
        notes=StringField("Important Notes About Pet")

        available=BooleanField("This pet is available for adoption!")