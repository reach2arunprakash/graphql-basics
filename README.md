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




https://medium.com/@marvinkome/creating-a-graphql-server-with-flask-ae767c7e2525


https://api.graph.cool/simple/v1/ck4wmom9u0dbm01248w9ro6xd/?query=%7B%0A%20%20allPersons%20%7B%0A%20%20%20%20name%0A%20%20%20%20age%0A%20%20%7D%0A%7D
