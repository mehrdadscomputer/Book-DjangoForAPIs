Book Title: Django for APIs
Author: William S. Vincent
Started: 2025-12-11 (Have already finished reading this book once)
Finished: YYYY-MM-DD

# 🧩 1. Scripts

## 1.1. Windows

```powershell
# returns the computer name/username
whoami
# the command for outputting a basic text message to the console
Write-Host "Hello, World!"
# print working directory
pwd
# change directory
cd subfolder\subsubfolder
# to make a new directory
mkdir directoryName
# to exit
exit
# to see Python version
python --version
# to exit Python (or Ctrl + z)
exit()
# to create a virtual environment
python -m venv .venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# to shows all directories and files
ls
# to activate the virtual environment
.venv\Scripts\Activate.ps1
# to deactivate the virtual environment
deactivate
# to install Django
python -m pip install django
# to update pip to the latest version
python -m pip install --upgrade pip
# to install django rest framework
python -m pip install djangorestframework
# to output the modules installed to a text file
pip freeze > requirements.txt
# extentions to install on VSCode
pip install black
# to get Git version
git --version
# create a new Django project
django-admin startproject django_project .
# sync the database with Django’s default settings
python manage.py migrate
# start up the local Django web server
python manage.py runserver
# stop the local server
Ctrl + c
# create a Django app
python manage.py startapp books
# make migration file and then migrate the changes to the database
python manage.py makemigrations NAMEOFTHEAPP
python manage.py migrate
# create a superuser in Django
python manage.py createsuperuser
# run the tests
python manage.py test
```
