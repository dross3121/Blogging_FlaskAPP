from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


@login.user_loader
def load_user(id):
	''' 
	Queries the db for User id which is passed as a string and returns converts to interger
	'''
	return User.query.get(int(id))


class User(UserMixin, db.Model):

	'''class created below inherits from db.Model, a base class for all models from Flask-SQLAlchemy. 
	This class defines several fields as class variables.
	'''
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	posts = db.relationship("Post", backref="author", lazy='dynamic')

	def avatar(self, size):
		''' changes user email to lower based on gravatar parameters and encodes users email to bytes
		because md5 supoort works with bytes not strings before passing to hash
		'''
		disgest = md5(self.email.lower().encode('utf-8')).hexdigest()
		return "http://www.gravatar.com/avatar/{}?d=identicon&s={}".format(
			disgest, size)

	def __repr__(self):
		'''
		__repr__ method tells Python how to print objects of this class.
		'''
		return '<User {}>'.format(self.username) 
 	

	def set_password(self, password):
		'''
		 accepts one password and hashes that password
		''' 
		self.password_hash =generate_password_hash(password)

	def check_password(self, password):
		'''
		returns true if password enter matches previously entered password and hash 
		'''
		return check_password_hash(self.password_hash, password)


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
	

