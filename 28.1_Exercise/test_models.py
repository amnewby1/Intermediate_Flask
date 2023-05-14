from unittest import TestCase
from app import app

from models import db, Pet

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_tests'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()

photo_url='https://images.unsplash.com/photo-1681502413474-1bf318cccf22?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=987&q=80'


class UserModelTestCase(TestCase):
    """Tests model for Pet."""

    def setUp(self):
        """Clean up any existing pets."""
        Pet.query.delete()

    def tearDown(self):
        """Clean up any fouled transaction"""
        db.session.rollback()

    def test_User(self):

        pet=Pet(name='Nugget', species='dog', photo_url=photo_url)
        
        self.assertEquals(pet.name, 'Nugget')
        self.assertEqual(pet.photo_url, photo_url)