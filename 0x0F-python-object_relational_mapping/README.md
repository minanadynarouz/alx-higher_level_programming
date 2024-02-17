# Curriculum
## SE Foundations
**Average:** 115.07%
### 0x0F. Python - Object-relational mapping
- Python
- OOP
- SQL
- MySQL
- ORM
- SQLAlchemy
**By:** Guillaume
**Weight:** 1
**Project will start:** Feb 15, 2024 5:00 AM
**Must end by:** Feb 19, 2024 5:00 AM
**Checker was released at:** Feb 16, 2024 5:00 AM
**An auto review will be launched at the deadline**

### Before you start…
Please make sure your MySQL server is in 8.0 -> [How to install MySQL 8.0 in Ubuntu 20.04](https://example.com)

### Background Context
In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

Without ORM:

```python
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
With an ORM:

python
Copy code
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
Do you see the difference? Cool, right?

The biggest difficulty with ORM is: The syntax!

Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don’t read the entire documentation before starting, just jump on it if you don’t get something.

Resources
Read or watch:

[Object-relational Mappers](https://www.fullstackpython.com/object-relational-mappers-orms.html)
[mysqlclient/MySQLdb documentation](https://mysqlclient.readthedocs.io/)
[Python MySQL Documentation](https://www.mikusa.com/python-mysql-docs/index.html)
[Object Relational Tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
[SQLAlchemy ORM & Core](https://docs.sqlalchemy.org/en/13/)
[mysqlclient source code](https://github.com/PyMySQL/mysqlclient)
[Video intro to mysqlalchemy](https://www.youtube.com/watch?v=woKYyhLCcnU)
[flask alchemy tutorial](https://www.youtube.com/playlist?list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW)
[10 stumbling blocks at SQLAlchemy](http://alextechrants.blogspot.com/2013/11/10-common-stumbling-blocks-for.html)
[SQLAlchemy cheetsheet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)
[SQLAlchemy ORM Tutorial for developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)
[SQLAlchemy base short tutorials](https://overiq.com/sqlalchemy-101/)

Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General

Why Python programming is awesome
How to connect to a MySQL database from a Python script
How to SELECT rows in a MySQL table from a Python script
How to INSERT rows in a MySQL table from a Python script
What ORM means
How to map a Python Class to a MySQL table
How to create a Python Virtual Environment
Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.

Requirements
General

Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
Your files will be executed with MySQLdb version 2.0.x
Your files will be executed with SQLAlchemy version 1.4.x
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc
Python Scripts

All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/env python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.7.*)
All your files must be executable
The length of your files will be tested using wc
More Info
And now, no more SQL! (feel free to reproduce everything we did with the previous tasks)

Use your files task_0.py and task_0.sql, the 0-entry_points.txt file is now empty. We will use MySQLdb to connect to a MySQL server running on your local machine (host: localhost, port: 3306) with the user and password stored in environment variables MYSQL_USER and MYSQL_PWD respectively. The database used with MySQLdb will be different for each task: (’hbtn_0c_0’, ‘hbtn_0c_1’, ‘hbtn_0c_2’)
Requirements:
First things first, let’s make sure that all our code is in the right place. In task_0.py:
Import the module MySQLdb
Import the module sys
Import the module os
Connect to a MySQL server running on localhost at port 3306
Use the database named argv[3] (database name will be passed as argument)
Take your credentials from environment variables MYSQL_USER and MYSQL_PWD
If you try to connect with the wrong credentials, an Access denied for user ... message will be shown. Make sure you have the right credentials.
