# Imports
from flask import Flask# app initialization
from flask_sqlalchemy import SQLAlchemy
import os
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from flask_graphql import GraphQLView


app = Flask(__name__)
app.debug = True

basedir = os.path.abspath(os.path.dirname(__file__))

# Configs
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' +    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


# TO-DO# Modules
db = SQLAlchemy(app)
# TO-DO# Models

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(256), index=True, unique=True)
	posts = db.relationship('Post', backref='author')
    
	
	def __repr__(self):
		return '<User %r>' % self.username
		
class Post(db.Model):
	__tablename__ = 'posts'    
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(256), index=True)
	body = db.Column(db.Text)
	author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	
	def __repr__(self):
		return '<Post %r>' % self.title
		

# TO-DO# Schema Objects

class PostObject(SQLAlchemyObjectType):
    class Meta:
        model = Post
        interfaces = (graphene.relay.Node, )
class UserObject(SQLAlchemyObjectType):
   class Meta:
       model = User
       interfaces = (graphene.relay.Node, )
	   
class Query(graphene.ObjectType):
	node = graphene.relay.Node.Field()
	all_posts = SQLAlchemyConnectionField(PostObject)
	all_users = SQLAlchemyConnectionField(UserObject)

schema =graphene.Schema(query=Query)
# TO-DO# Routes

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)
# TO-DO@app.route('/')
def index():
    return '<p> Hello World</p>'
	
if __name__ == '__main__':
	app.run()
