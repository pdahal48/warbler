# """User model tests."""

# # run these tests like:
# #
# #    python -m unittest test_user_model.py


# import os
# from unittest import TestCase
# from sqlalchemy import exc


# from models import db, User, Message, Follows

# # BEFORE we import our app, let's set an environmental variable
# # to use a different database for tests (we need to do this
# # before we import our app, since that will have already
# # connected to the database

# os.environ['DATABASE_URL'] = "postgresql:///warbler-test"


# # Now we can import app

# from app import app

# # Create our tables (we do this here, so we only create the tables
# # once for all tests --- in each test, we'll delete the data
# # and create fresh new clean test data

# db.create_all()


# class UserModelTestCase(TestCase):
#     """Test views for messages."""

#     def setUp(self):
#         """Create test client, add sample data."""

#         User.query.delete()
#         Message.query.delete()
#         Follows.query.delete()

#         u1 = User.signup("test1", "email1@email.com", "password", None)
#         uid1 = 1111
#         u1.id = uid1

#         u2 = User.signup("test2", "email2@email.com", "password", None)
#         uid2 = 2222
#         u2.id = uid2

#         u1 = User.query.get(uid1)
#         u2 = User.query.get(uid2)

#         self.u1 = u1
#         self.uid1 = uid1

#         self.u2 = u2
#         self.uid2 = uid2

#         self.client = app.test_client()

#     def tearDown(self):
#         res = super().tearDown()
#         db.session.rollback()
#         return res


#     def test_user_model(self):
#         """Does basic model work?"""

#         u = User(
#             email="test@test.com",
#             username="testuser",
#             password="HASHED_PASSWORD"
#         )

#         db.session.add(u)
#         db.session.commit()

#         # User should have no messages & no followers
#         self.assertEqual(len(u.messages), 0)
#         self.assertEqual(len(u.followers), 0)


#     def test_repr_function(self):
#         """Testing the repr function"""

#         u = User(
#             email="test@test.com",
#             username="testuser",
#             password="HASHED_PASSWORD"
#         )
#         self.assertEqual(str(u), f"<User #{u.id}: {u.username}, {u.email}>")


#     def test_is_following(self):
#         """ Testing following feature """

#         f1 = Follows(user_being_followed_id=self.u1.id, user_following_id=self.u2.id)
#         db.session.add(f1)
#         db.session.commit()

#         self.assertTrue(self.u2.is_following(self.u1))
#         self.assertFalse(self.u1.is_following(self.u2))

#         self.assertTrue(self.u1.is_followed_by(self.u2))
#         self.assertFalse(self.u2.is_followed_by(self.u1))


#     def test_create_user(self):
#         """ Create user """

#         u = User(username='testuser21', email='testemail@noemail.com', password='testpassword1$', image_url="noimage.com")
#         db.session.add(u)
#         db.session.commit()

#         users = User.query.all()
#         self.assertEqual(len(users), 3)

#     def test_invalid_username_signup(self):
#         invalid = User.signup(None, "test@test.com", "password", None)
#         uid = 123456789
#         invalid.id = uid
#         with self.assertRaises(exc.IntegrityError) as context:
#             db.session.commit()

#     def test_invalid_email_signup(self):
#         invalid = User.signup("testtest", None, "password", None)
#         uid = 123789
#         invalid.id = uid
#         with self.assertRaises(exc.IntegrityError) as context:
#             db.session.commit()

#     def test_invalid_password_signup(self):
#         with self.assertRaises(ValueError) as context:
#             User.signup("testtest", "email@email.com", "", None)
        
#         with self.assertRaises(ValueError) as context:
#             User.signup("testtest", "email@email.com", None, None)




