from unittest import TestCase
from app import app

from models import db, Pet

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_tests'
app.config['SQLALCHEMY_ECHO'] = False

app.config['TESTING']=True

app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']
app.config['WTF_CSRF_ENGABLED']=False

db.drop_all()
db.create_all()

photo_url='https://images.unsplash.com/photo-1681502413474-1bf318cccf22?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=987&q=80'


class AdoptTestCase(TestCase):
    
    def setUp(self):
        Pet.query.delete()
        

        pet=Pet(name='Bruster', species='dog', photo_url=photo_url, notes="The best boy!")
        db.session.add(pet)
        db.session.commit()    

        self.pet_id=pet.id
        self.pet=pet

    def tearDown(self):
        db.session.rollback()

    def test_list_pets(self):
        with app.test_client() as client:
            resp=client.get("/pets")
            html=resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Bruster', html)

    def test_display_and_edit(self):
        with app.test_client() as client:
            resp=client.get(f"/pets/{self.pet.id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Bruster</h1>', html)
            self.assertIn(self.pet.species, html)
    
    def test_add_user(self):
        with app.test_client() as client:
            d={"name": "BooBoo Simms", "species": "dog", "photo_url": photo_url}
            resp = client.post("/pets/add", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code,200)
            self.assertIn("BooBoo Simms", html)