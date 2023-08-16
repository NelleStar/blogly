from models import User, db
from app import app

# create tables
db.drop_all()
db.create_all()

# empty table just in case
User.query.delete()

# add people
harry = User(first_name='Harry', last_name='Potter', image_url='https://images.unsplash.com/photo-1586796676789-f6fe8cc276f7?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80')
hermione = User(first_name='Hermione', last_name='Granger', image_url='https://images.unsplash.com/photo-1551269901-5c5e14c25df7?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8aGFycnklMjBwb3R0ZXJ8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60')
ron = User(first_name='Ronald', last_name='Weasley')

db.session.add(harry)
db.session.add(hermione)
db.session.add(ron)

db.session.commit()