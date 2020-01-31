from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# Add test pets
pet1 = Pet(name='Rooney', species="Dog", age=16, available=False)
pet2 = Pet(name='Fluffy', species="Cat", age=2,
           photo_url="https://icatcare.org/app/uploads/2018/07/Thinking-of-getting-a-cat.png",
           notes="This is a note about Fluffy", available=True)
pet3 = Pet(name='Bubbles', species="Fish", age=4,
           photo_url="https://assets.bwbx.io/images/users/iqjWHBFdfxIU/iQsZSHFN4AUw/v1/1200x900.jpg",
           notes="Very cuddly!!!!", available=True)
pet4 = Pet(name='Pikachu', species="Friend",
           age=2, notes="Zappy", available=False)

# Add new objects to session, so they'll persist
db.session.add(pet1)
db.session.add(pet2)
db.session.add(pet3)
db.session.add(pet4)

# Commit--otherwise, this never gets saved!
db.session.commit()
