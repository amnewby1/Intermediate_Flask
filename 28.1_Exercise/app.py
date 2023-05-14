from flask import Flask, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "amanda1"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route("/")
def home():
    """redirects to a /pets route"""
    return redirect("/pets")

@app.route("/pets")
def list_pets():
    """Home page that lists pets"""
    pets=Pet.query.all()
    return render_template('home_list_pets.html', pets=pets)

@app.route("/pets/add", methods=['GET', 'POST'])
def add_pet():
    form= AddPetForm()

    if form.validate_on_submit():
        name=form.name.data
        species=form.species.data
        photo_url=form.photo_url.data
        age=form.age.data
        notes=form.notes.data

        new_pet=Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"Created new pet: name is {name} and species is {species}")
        return redirect ('/')
    
    else:
        return render_template('add_pet_form.html', form=form)

@app.route('/pets/<int:pet_id>', methods=['GET', 'POST'])
def display_and_edit_pet(pet_id):
    pet=Pet.query.get_or_404(pet_id)
    form=EditPetForm(obj=pet)
 
    if form.validate_on_submit():
        pet.photo_url=form.photo_url.data
        pet.notes=form.notes.data
        pet.available=form.available.data
        db.session.commit()
        return redirect ('/pets')
    else:
        return render_template("display_and_edit_pet.html",form=form, pet=pet)
    
@app.route('/pets/<int:pet_id>/delete', methods=["POST"])
def delete_pet(pet_id):
    """Delete a User"""
    pet = Pet.query.get_or_404(pet_id)
    db.session.delete(pet)
    db.session.commit()

    return redirect("/pets")