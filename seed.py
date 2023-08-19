from models import User, Post, db
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

# add content
har1 = Post(title="First Post", content="Something interesting", user_id=1)
har2 = Post(title="Second Post", content="Something interesting", user_id=1)
har3 = Post(title="Third Post", content="Something interesting", user_id=1)
herm1 = Post(title="First Post", content="Something interesting", user_id=2)
herm2 = Post(title="Second Post", content="Something interesting", user_id=2)
herm3 = Post(title="Third Post", content="Something interesting", user_id=2)
ron1 = Post(title="First Post", content="Something interesting", user_id=3)
ron2 = Post(title="Second Post", content="Something interesting", user_id=3)
ron3 = Post(title="Third Post", content="Something interesting", user_id=3)

db.session.add_all([harry, hermione, ron])
db.session.commit()

db.session.add_all([har1, har2, har3, herm1, herm2, herm3, ron1, ron2, ron3])
db.session.commit()
