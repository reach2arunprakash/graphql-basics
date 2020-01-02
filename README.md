# graphql-basics
this has contents related to graphql


Setting up your project


$ mkdir flask-graphql-project
$ cd flask-graphql-project

Optional step:
$ virtualenv venv
$ source venv/bin/activate

Mandatory 
$ pip install flask flask-graphql flask-migrate flask-sqlalchemy graphene graphene-sqlalchemy



$ python
>>> from app import db, User, Post
>>> db.create_all()
>>> john = User(username='johndoe')
>>> post = Post()
>>> post.title = "Hello World"
>>> post.body = "This is the first post"
>>> post.author = john
>>> db.session.add(post)
>>> db.session.add(john)
>>> db.session.commit()
>>> User.query.all()
[<User 'johndoe'>]
>>> Post.query.all()
[<Post 'Hello World'>
