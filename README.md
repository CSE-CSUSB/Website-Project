Integrated Club Website Project
===============================

About this Project
------------------

The aim of the project is to develop a central codebase that multiple CSUSB student clubs (currently the ACM, IEEE, and InfoSec clubs) can use for years to come to build and maintain their individual websites. It will provide a central database for storing information on club events, club membership, attendance, etc. To ensure future club members can easily maintain this project, the popular [**Python**](https://docs.python.org/3/) programming language was chosen.

This codebase utilizes the [**Flask**](http://flask.pocoo.org/docs/) microframework, with built-in support for the [**Jinja2**](http://jinja.pocoo.org/docs/dev/) HTML templating engine. Website data is stored in a [**PostgreSQL**](http://www.postgresql.org/docs/) database. Manipulation of the database is done through the [**Flask-SQLAlchemy**](http://pythonhosted.org/Flask-SQLAlchemy/) wrapper to [**SQLAlchemy**](http://www.sqlalchemy.org/library.html#reference), using the [**psycopg2**](http://initd.org/psycopg/) database driver. Database migrations are done using [**Flask-Migrate**](http://flask-migrate.readthedocs.org/en/latest/), a wrapper around [**Alembic**](http://alembic.readthedocs.org/en/latest/tutorial.html). Sessions are handled using a version of [**Flask-KVSession**](http://pythonhosted.org/Flask-KVSession/) modified to use [**scrypt**](https://bitbucket.org/mhallin/py-scrypt/src) for more security.

Clubs will enable whatever modules from the codebase they wish to use, and then have their own HTML templates for the front-end. Clubs are advised to use CSS3 (using SASS), HTML5, and JavaScript for their page design.

Developers
----------

* Mike Korcha, *mkorcha*
* Miguel Saldivar, *miguelsaldivar*
* Yosias Sapari, *yosiassapari*
* Beverly Abadines, *BeverlyAb*
* Mark Holmes, *maholmes1*
* Dylan Allbee, *dallbee*
* Kenneth Johnson <kenpilot@gmail.com>, *securedirective*

Getting Involved
----------------

[Get in contact with the CSE Club webmaster](mailto:webmaster@cse-club.com) to get added to the GitHub team. If added, you will get write access to the repository.

Not in one of the clubs? This project is intended to be a learning experience for club members to pick up new skills and apply those learned in classes. However, bringing something to our attention via the issue tracker or a pull request is always appreciated!

Requirements
------------

* Linux or Mac OS X (using Homebrew to install *python* and *pip*)
* python 3.4.x
* python-virtualenv 12.1.x
* git 2.4.x
* pip 6.1.x
* postgresql 9.4.x

**Note:** Pay close attention to the package names for your distro of Linux...

* For example, on Ubuntu Server you'd use ```python3 virtualenv git python3-pip postgresql```.
* On Manjaro (an Arch-derivative), you'd use ```python python-virtualenv git python-pip postgresql```.

Setting Up
----------

### Linux via Command Line

Clone or pull the project repository:

    cd ~
    git clone https://github.com/CSE-Club/Website-Project.git
    mv Website-Project acm-csusb.org

Create a virtual environment and activate it:

    cd ~/acm-csusb.org
    virtualenv .env

Start PostgreSQL:

    sudo service postgresql start      # the Ubuntu way of doing it

Login to the database as root (postgres) and create a new user for the site. Check the config.py for what username to create.

    psql -U postgres
        CREATE USER dev WITH PASSWORD 'password';
        \q

Create a development database. Check config.py for what database name to use.

    createdb -U postgres clubsitedev

Activate your virtual environment:

    cd ~/acm-csusb.org
    source .env/bin/activate

Install all required python dependencies:

    pip install -r requirements.txt

Use Flask-Migrate to create the tables as specified in the model:

    python manage.py db upgrade

Query the database manually for testing:

    psql -U dev clubsitedev

Other useful functions:

* List all databases: ```\l```
* List all users: ```\du```
* List all tables: ```\d```
* Describe table: ```\d <table>```

### PyCharm IDE (unverified)

* Clone or pull the updated project repository
* Ensure that PyCharm sees your Python environment as __.env__
* Update your dependencies

Ongoing Work
------------

* Always begin your day by pulling the latest revisions from GitHub

* To run the site locally, either press the play button in PyCharm or run ```python start.py``` from the command line in the virtual environment. You should then be able to navigate to __localhost:5000__ to see the development version of the site that you can work on. Check in start.py for the most recent port in use.

* Once your changes are made and you're ready to commit, be sure to update the __requirements.txt__ file as needed, by running ```pip freeze > requirements.txt``` in the base project directory.

* Once that is done, commit and push your changes to GitHub.

Developer notes
---------------

### Database migration
We rarely work directly with the SQL database, once the blank database is created as described above. The Flask-Migration process was first initialized with this command (creates the /migrations folder, alembic.ini, and env.py):

    python manage.py db init

Then run the migrate command. This will compare the models defined in models.py to the actual tables in the database (blank at this point) and build a migration file that will perform the necessary steps to bring your database up-to-date with models.py:

    python manage.py db migrate

If you make any changes to the database model (models.py), simply create a new migration file and update your own database:

    python manage.py db migrate   # Creates a script in /migrations/versions; upload this to GitHub
    python manage.py db upgrade   # Applies the script to the local database

Then, after you push your changes to GitHub, the other developers can upgrade their databases. The upgrade command will see the new migration file and do what is necessary to make the local database consistent with the latest revision:
 
    python manage.py db upgrade

If you have any problems, you can always downgrade. The migration tool keeps track of how to undo every revision:

    python manage.py db downgrade
