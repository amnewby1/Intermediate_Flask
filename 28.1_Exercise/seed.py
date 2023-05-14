"""Seed file to make sample data for db."""
from models import db, Pet
from app import app

"""Drop and create all tables"""
db.drop_all()
db.create_all()


"""Emptied out the tables"""
Pet.query.delete()

"""Add sample pets"""
photo_url_nugget='https://images.unsplash.com/photo-1583337130417-3346a1be7dee?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1064&q=80'
photo_url_floof='https://images.unsplash.com/photo-1629246999700-1e7ad7a1ba03?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1012&q=80'
photo_url_spike='https://plus.unsplash.com/premium_photo-1664304468134-260754f091cc?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=978&q=80'
photo_url_fancy='https://images.unsplash.com/photo-1606715895281-ccdf0143f198?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=987&q=80'

nugget=Pet(name="Nugget", species="dog", notes="Snores like a grown man!", photo_url=photo_url_nugget, available=False)
floof=Pet(name="Floof", species="dog", notes="Sheds enough for two dogs...", photo_url=photo_url_floof, available=True)
spike=Pet(name="Spike", species="porcupine", photo_url=photo_url_spike)
fancy=Pet(name="Fancy", species="cat", notes="Dogs rule and cats drool!", photo_url=photo_url_fancy)

"""Add and commit pets"""

db.session.add_all([nugget, floof, spike, fancy])
db.session.commit()
