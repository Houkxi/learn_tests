from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	email = db.Column(db.String(120), unique=True)

	def __init__(self, username, email):
		self.username = username
		self.email = email


class UserSchema(ma.Schema):
	class Meta:
		# Fields to expose
		fields = ('username', 'email')


user_schema = UserSchema()
users_schema = UserSchema(many=True)

# endpoint to create new user
@app.route("/user")
def view():
	return render_template("form.html")

print "Testing this stuff !!!!!"

@app.route("/user", methods=["POST"])
def add_user():
	print "\nPOST request\n"
	print 'username'
	print 'GO', request.data, 'end'
	username = request.json[__getitem__]
	email = request.json['email']
	# username_1 = request.form["text"]
	# email_2 = request.form["text"]
	# username = json.load(username_1)
	# email = json.load(email_2)

	# print ( username, email)
	new_user = User(username, email)

	db.session.add(new_user)
	db.session.commit()
	return jsonify(new_user)


# endpoint to show all users
@app.route("/user", methods=["GET"])
def get_user():
	print "\nGET request\n"
	all_users = User.query.all()
	result = users_schema.dump(all_users)
	return jsonify(result.data)


# endpoint to get user detail by id
@app.route("/user/<id>", methods=["GET"])
def user_detail(id):
	print "\nGET ID request\n"
	user = User.query.get(id)
	return user_schema.jsonify(user)


# endpoint to update user
@app.route("/user/<id>", methods=["PUT"])
def user_update(id):
	print "\nPUT  request\n"
	user = User.query.get(id)
	username = request.json['username']
	email = request.json['email']

	user.email = email
	user.username = username

	db.session.commit()
	return user_schema.jsonify(user)

# endpoint to delete user
@app.route("/user/<id>", methods=["DELETE"])
def user_delete(id):
	print "\nDEL request"
	user = User.query.get(id)
	db.session.delete(user)
	db.session.commit()

	return user_schema.jsonify(user)


if __name__ == '__main__':
    app.run(debug=True)
