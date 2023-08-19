import unittest
from flask import Flask
from app import app, db, User, Post

class BloglyAppTestCase(unittest.TestCase):

    def setUp(self):
        """Set up the app for testing"""
        app.config['TESTING'] = True
        self.client = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """Tear down the app after testing"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_home_page(self):
        """Test the home_page route"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_list_users(self):
        """Test the list_users route"""
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)

    def test_user_detail(self):
        """Test the user_detail route"""
        # Create a user for testing
        user = User(first_name='John', last_name='Doe', image_url='image.jpg')
        db.session.add(user)
        db.session.commit()

        response = self.client.get(f'/users/{user.id}')
        self.assertEqual(response.status_code, 200)

    def test_new_user(self):
        """Test the new_user route"""
        response = self.client.get('/users/new')
        self.assertEqual(response.status_code, 200)


    # def test_make_new_post(self):
    #   """Test the make_new_post route"""
    #   response = self.client.get('/users/1/posts/new') 
    #   self.assertEqual(response.status_code, 200)


    def test_post_details(self):
        """Test the post_details route"""
        # Create a user and a post for testing
        user = User(first_name='John', last_name='Doe', image_url='image.jpg')
        db.session.add(user)
        db.session.commit()

        post = Post(title='Test Post', content='Test content', user_id=user.id)
        db.session.add(post)
        db.session.commit()

        response = self.client.get(f'/posts/{post.id}')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
