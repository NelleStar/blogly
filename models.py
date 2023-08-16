"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
  db.app = app
  db.init_app(app)


class User(db.Model):
  __tablename__ = "users"
 
  def __repr__(self):
    """Show info about user"""

    u = self
    return f"<User {u.id} {u.first_name} {u.last_name} {u.image_url}>"
  
  

  id = db.Column(db.Integer,
                 primary_key=True,
                 autoincrement=True)
  first_name = db.Column(db.String(30),
                         nullable=False)
  last_name = db.Column(db.String(30),
                        nullable=False)
  image_url = db.Column(db.Text,
                        default="https://images.unsplash.com/photo-1597589827317-4c6d6e0a90bd?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8c3F1YXJlfGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60")