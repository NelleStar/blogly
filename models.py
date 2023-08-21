"""Models for Blogly."""
from datetime import datetime 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
  db.app = app
  db.init_app(app)


class User(db.Model):
  __tablename__ = "users"
 
  id = db.Column(db.Integer,
                 primary_key=True,
                 autoincrement=True)
  first_name = db.Column(db.String(30),
                         nullable=False)
  last_name = db.Column(db.String(30),
                        nullable=False)
  image_url = db.Column(db.Text,
                        default="https://images.unsplash.com/photo-1597589827317-4c6d6e0a90bd?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8c3F1YXJlfGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60")
  
  def __repr__(self):
    """Show info about user"""
    u = self
    return f"<User {u.id} {u.first_name} {u.last_name} {u.image_url}>"
  

  
class Post(db.Model):
  __tablename__ = 'posts'

  id = db.Column(db.Integer,
                 primary_key=True,
                 autoincrement=True)
  title = db.Column(db.String(80),
                    nullable=False)
  content = db.Column(db.Text,
                      nullable=False)
  created_at = db.Column(db.DateTime,
                         nullable=False,
                         default=datetime.utcnow)  #Default value for current timestamp
  user_id = db.Column(db.Integer,
                      db.ForeignKey('users.id'),
                      nullable=False)
  
  # interconnects users table to posts table and backreferences it
  user = db.relationship('User', backref='posts')

  # links the posts_tags table to posts and back again
  assigned = db.relationship('PostTag', backref='post')

  # links tags to posts with a through relationship
  tags = db.relationship('Tag',
                         secondary='posts_tags',
                         backref='posts')

  def __repr__(self):
    """show information about the Post"""
    p = self
    return f'<Post {p.id} {p.title} {p.content} {p.created_at} {p.user_id}>'  


  
class Tag(db.Model):
  """tag model"""
  __tablename__ = "tags" 

  id = db.Column(db.Integer,
                 primary_key = True,
                 autoincrement = True) 
  name = db.Column(db.Text,
                   nullable = False,
                   unique = True)
  

  # set up relationship between tags table and posts_tags table and back
  assigned = db.relationship('PostTag', backref='tag')
  
  def __repr__(self):
    """show information about the tag"""
    t=self 
    return f"Tag {t.id} {t.name}"
  

class PostTag(db.Model):
  """links posts and tags together"""

  __tablename__ = 'posts_tags'

  post_id = db.Column(db.Integer,
                      db.ForeignKey('posts.id'),
                      primary_key = True, 
                      nullable = False)
  tag_id = db.Column(db.Integer,
                     db.ForeignKey('tags.id'),
                     primary_key = True,
                     nullable = False)
  
  def __repr__(self):
    """show the interconnection"""
    pt=self
    return f"<PostTag {pt.post_id} {pt.tag_id}>"
  

