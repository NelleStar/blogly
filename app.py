"""Blogly application."""

from flask import Flask, request, render_template, redirect, flash, session
from models import db, connect_db, User, Post

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False #True if I want to see the sql commands


app.app_context().push()

connect_db(app)
db.create_all()

@app.route('/')
def home_page():
    """shows list of all users in db"""

    users = User.query.all()
    return render_template('list.html', users=users)

@app.route('/users')
def list_users():
    """list users"""

    users = User.query.all()
    return render_template('list.html', users=users)

@app.route('/users/<int:id>')
def user_detail(id):
    """show details about single user"""
    user = User.query.get_or_404(id)
    posts = Post.query.filter_by(user_id=id).all()
    return render_template('details.html', user=user, posts=posts)

@app.route('/users/new')
def new_user():
    """show new user form - GET request"""
    return render_template('new.html')

@app.route('/users/new', methods=["POST"])
def create_user():
    """process the new user form - POST request"""

    first = request.form["first_name"]
    last = request.form["last_name"]
    url = request.form["image_url"]

    new_user = User(first_name=first, last_name=last, image_url=url)
    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:id>/edit')
def edit_user(id):
    """take user to edit profile page"""
    user = User.query.get_or_404(id)
    return render_template('edit.html', user=user)

@app.route('/users/<int:id>/edit', methods=['POST'])
def save_changes(id):
    """allows user to change name or url"""
    user = User.query.get_or_404(id)

    user.first_name = request.form["first_name"]
    user.last_name = request.form["last_name"]
    user.image_url = request.form["image_url"]

    db.session.commit()

    return redirect(f'/users/{id}')


@app.route('/users/<int:id>/delete', methods=['POST'])
def delete_user(id):
  """delete a user"""
  
  user = User.query.get_or_404(id)
  
  db.session.delete(user)
  db.session.commit()

  return redirect('/users')


@app.route('/users/<int:id>/posts/new')
def make_new_post(id):
    """go to page with new post form on it"""

    user = User.query.get_or_404(id)
    return render_template('post_form.html', user=user)

@app.route('/users/<int:id>/posts/new', methods=['POST'])
def save_new_post(id):
    """save a new post for the specific user"""

    user = User.query.get_or_404(id)
    title = request.form["title"]
    content = request.form["content"]

    new_post = Post(title=title, content=content, user_id=user.id)
    db.session.add(new_post)
    db.session.commit()

    return redirect(f'/posts/{new_post.id}')


@app.route('/posts/<int:id>')
def post_details(id):
    """show page with specific post on it"""

    post = Post.query.get_or_404(id)
    user = User.query.get_or_404(post.user_id)
    return render_template('post_details.html', post=post, user=user)

@app.route('/posts/<int:id>/edit')
def edit_post(id):
    """take user to edit blog page"""

    post = Post.query.get_or_404(id)
    return render_template('post_edit.html', post=post)

@app.route('/posts/<int:id>/edit', methods=['POST'])
def save_blog_changes(id):
    """allows user to change blog information"""
    post = Post.query.get_or_404(id)

    post.title = request.form["title"]
    post.content = request.form["content"]


    db.session.commit()

    return redirect(f'/posts/{id}')


@app.route('/posts/<int:id>/delete', methods=['POST'])
def delete_post(id):
    """delete a specific post from that posts page"""

    post = Post.query.get_or_404(id)
    user = User.query.get_or_404(post.user_id)
  
    db.session.delete(post)
    db.session.commit()

    return redirect(f'/users/{user.id}')



if __name__ == "__main__":
    app.run(debug=True)

