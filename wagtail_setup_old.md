<img src="https://docs.wagtail.io/en/v2.12.3/_static/logo.png" data-canonical-src="![wagtail_banner]
(https://docs.wagtail.io/en/v2.12.3/_static/logo.png =250x250)" width="128" height="128" align="right" />

# Wagtail Setup Guide

Wagtail is an open source CMS written in Python and built on the Django web framework.
This README covers getting an instance of Wagtail running on your local device and understanding 
basic features.

### Install dependencies - Wagtail supports Python 3.6, 3.7, 3.8, 3.9

- Check what version of python is installed - confirm with the team that we are using python 3.x:
    - `$ python3 --version`

### Create and activate a Virutal Environments
This will create a virtual environment called mysite where we can standardize our dependencies and prevent any conflicts.
- On Windows (cmd.exe):
    - `$ python3 -m venv mysite\env`
    - `$ mysite\env\Scripts\activate.bat`
- On Unix or MacOS (bash):
    - `$ python3 -m venv mysite/env`
    - `$ source mysite/env/bin/activate`

### Install Wagtail
- With Python installed, we can use 'pip' to install Wagtail.
    - `$ pip install wagtail`
#hj testing

### Generate your site - Wagtail Start Command
Wagtail provides a **start** command similar to `django-admin startproject`. Running `wagtail start mysite` in your project will generate a new mysite folder with a few Wagtail-specific extras, including the required project settings, a “home” app with a blank HomePage model and basic templates, and a sample “search” app.
- Start Wagtail
    - `$ wagtail start mysite mysite`
- Install Project Dependencies
    - `$ cd mysite` #enter the mysite directory you made from above
    - `$ pip install -r requirements.txt` #install the requirements

### Create the database
- If you haven’t updated the project settings, this will be a SQLite database file in the project directory.
    - `$ python manage.py migrate` #This creates the initial database
    - `$ python manage.py createsuperuser` #Creates the admin account to login with
    - `$ python manage.py runserver` #Activates the server to start

### In your browser, open up http://127.0.0.1:8000

<img src="https://docs.wagtail.io/en/v2.12.3/_images/tutorial_1.png">

### Confirm the admin page is running, open up http://127.0.0.1:8000/admin. 

<img src="https://docs.wagtail.io/en/v2.12.3/_images/tutorial_2.png">


# Extend the HomePage model
Out of the box, the “home” app defines a blank HomePage model in models.py, along with a migration that creates a homepage and configures Wagtail to use it.

Edit home/models.py as follows, to add a body field to the model:


### Updates that are made

- `$python manage.py makemigrations`
- 

