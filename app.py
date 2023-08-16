"""Blogly application."""

from flask import Flask, request, render_template, redirect, flash, session
from models import db, connect_db, User

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


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
    return render_template('details.html', user=user)

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

if __name__ == "__main__":
    app.run(debug=True)

