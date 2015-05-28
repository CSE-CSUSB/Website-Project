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
* Kenneth Johnson, *securedirective*

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
* (the remaining requirements will be installed below using *pip*)

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

*Populate the database with sample data (Optional)*

    python populatesampledata.py

Query the database manually for testing:

    psql -U dev clubsitedev

Other useful functions:

* List all databases: ```\l```
* List all users: ```\du```
* List all tables: ```\dt```
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

### URLs

Each module in /blueprints should declare its url_prefix (ex: */admin*, */members*). Within these modules, route declarations are relative. For example, in /blueprints/members.py *@blueprint.route('/settings')* would be a relative link to *http://site.com/members/settings*.

This leaves /blueprints/content.py to be the catch-all for anything in the root path. A request for *http://site.com/anythinghere* will cause it to look in the *content* table for a page with that url.

Our /blueprints/auth.py module is the only one breaking the above convention. It doesn't use url_prefix, as we didn't want the pages to be *http://site.com/auth/login* and *http://site.com/auth/logout*.

### Pip dependencies

Keep this updated. As of 2015-05-20, here are our root dependencies and what packages they depend on:

1. Flask
    * Werkzeug
    * Jinja2
        - MarkupSafe
    * itsdangerous
2. Flask-SQLAlchemy
    * SQLAlchemy
3. psycopg2
4. Flask-Migrate
    * Alembic
        - Mako
            * MarkupSafe
    * Flask-Script
5. Flask-WTF (used in many of modules in /forms)
    * WTForms
6. scrypt (used by /util/session.py
7. simplekv (used by /util/session.py
    * six
8. CommonMark (used by /blueprints/content.py)

### Database migration

We rarely work directly with the SQL database, once the blank database is created as described above. The Flask-Migration process was first initialized with this command (creates the /migrations folder, alembic.ini, and env.py):

    python manage.py db init

Then run the migrate command. This will compare the models defined in models.py to the actual tables in the database (blank at this point) and build a migration file that will perform the necessary steps to bring your database up-to-date with models.py:

    python manage.py db migrate --message "Initial model"

At any time, you can check the upgrade status of your local database:

    python manage.py db current

If you make any changes to the database model (models.py), simply create a new migration file (migrate command) and of course apply it to your own local database (upgrade command):

    python manage.py db migrate --message "Description of changes"
    python manage.py db upgrade

After you've pushed your changes to GitHub, other developers can upgrade their databases too using this command alone:
 
    python manage.py db upgrade

If you have any problems, you can always downgrade. The migration tool keeps track of how to undo every revision:

    python manage.py db downgrade
