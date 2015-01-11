CSE Club Website Project
========================

This is the repository for the CSE Club Website project.

About this Project
------------------

The aim of the project is to develop the CSE Club's website which is intended to serve the club for many years to come. It will provide a centralized location for any and all information related to the club. 

This project will be done using the Python programming language, utilizing the Flask microframework, and the PostgreSQL database system. It will also use the standard frontend technologies - CSS3 (using SASS), HTML5, and JavaScript.

Getting Involved
----------------

[Get in contact with the CSE Club webmaster](mailto:webmaster@cse-club.com) to get added to the GitHub team. If added, you will get write access to the repository.

Not in the club? This project is intended to be a learning experience for club members to pick up new skills and apply those learned in classes. However, bringing something to our attention via the issue tracker or a pull request is always appreciated!

Requirements
------------

* Python 3.4.x

* PostgreSQL 9.3.x

Setting Up
----------

### Command Line

***Note*** It is much easier to run this project on Linux or OS X (using Homebrew to install Python and Pip).

* Clone or pull the project repository

* Make sure you have a virtual environment set up: ```virtualenv .env``` or ```virtualenv3 .env``` if you have both python2 and python3 installed on your system

* If you don't have a test database set up locally: ```psql -U csecw < database.sql```. 

    * If you don't have PostgreSQL set up yet, read below.

* Activate your venv: ```source .env/bin/activate```

* Install/update any dependencies that may have changed: ```pip install -r requirements.txt```

### PyCharm IDE

* Clone or pull the updated project repository

* Ensure that PyCharm sees your Python environment as __.env__

* Update your dependencies

### PostgreSQL

The __config.py__ file expects the database to have a user of __csecw__, a password of __csecw__, and a database named __csecw__. The database schema is stored in __database.sql__. There are many tutorials that go into how to do this.

Running
-------

* Either press the play button in PyCharm or run ```python3 start.py```. You should then be able to navigate to __localhost:5000__ to see the development version of the site that you can work on.

Finishing Up
------------

* Once your changes are made and you're ready to commit, be sure to update the __requirements.txt__ file as needed, by running ```pip freeze > requirements.txt``` in the base project directory.

* Once that is done, commit and push your changes to GitHub.


Developers
----------

* Mike Korcha (team lead)
* Miguel Saldivar
* Yosias Sapari
* Beverly Abadines
* Mark Holmes
