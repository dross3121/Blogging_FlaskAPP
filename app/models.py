from datetime import datetime
from app import db

class User(db.Model):

	'''class created below inherits from db.Model, a base class for all models from Flask-SQLAlchemy. 
	This class defines several fields as class variables.
	'''
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	#represents relationship between user post one to many relationsip
	posts = db.relationship("Post", backref="author", lazy='dynamic')

	def __repr__(self):
		'''
		__repr__ method tells Python how to print objects of this class.
		'''
		return '<User {}>'.format(self.username) 
 

class Post(db.Model):
	'''
	Post class will represents blog posts written by users.
	'''
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(140))
	# timstamp field is index set to true which orders post in chronological order and a default parameter was added and passed datetime.utcnow function which set the users time to there local time
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	# user_id variable was initialized as a foreign key to user.id which means it reference id form the user table in the db
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Post {}>'.format(self.body)
	

