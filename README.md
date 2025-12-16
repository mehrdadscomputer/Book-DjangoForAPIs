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
# to serve static files
python -m pip install whitenoise
# production webserver
python -m pip install gunicorn
# to make a new project on Rahti
oc new-project djangoapitest  --description="csc_project: 2007342"

python -m pip install django-cors-headers

# Steps to run the project on the cloud. Here, Rahti 2
# 1. configure static files
mkdir static
# 2. install WhiteNoise
python -m pip install whitenoise
# WhiteNoise must be added to django_project/settings.py in the following locations:
    # • whitenoise above django.contrib.staticfiles in INSTALLED_APPS: "whitenoise.runserver_nostatic",
    # • WhiteNoiseMiddleware above CommonMiddleware: "whitenoise.middleware.WhiteNoiseMiddleware",
    # • STATICFILES_STORAGE configuration pointing to WhiteNoise:
        # STATIC_URL = "static/"
        # STATICFILES_DIRS = [BASE_DIR / "static"]
        # STATIC_ROOT = BASE_DIR / "staticfiles"
        # STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
python manage.py collectstatic
# 3. install Gunicorn as the production web server
python -m pip install gunicorn
# 4. create requirements.txt
python -m pip freeze > requirements.txt
# 5. update the ALLOWED_HOSTS configuration
ALLOWED_HOSTS = [".rahtiapp.fi", "localhost", "127.0.0.1"]
# 6. add this Dockerfile:
# Use the official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port
EXPOSE 8000

# Start the Gunicorn server
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
# 7. git add, commit, and push
# 8. login to Rahti2 cmd
# 9. make a new project on Rahti 2
oc new-project djangoapitesttodoapp --description="csc_project: 2007342"
# 10. swithc to that project
oc project djangoapitesttodoapp
# 11. create an  application on Rahti (Docker build)
oc new-app https://github.com/mehrdadscomputer/todo.git --name=django-app-apitest --strategy=docker
# 12. set Django secret key
oc set env dc/django-app-apitest SECRET_KEY='your-secret-key'
# 13. build & deploy
oc start-build django-app-apitest
# 14. Watch
oc logs -f bc/django-app-apitest
# 15. verify pod is running. Expected: 1/1 Running
oc get pods
# 16. service verification (Gunicorn on port 8000)
oc describe svc django-app-apitest
# 17. route creation (HTTPS enabled)
oc delete route django-app-apitest
oc create route edge django-app-apitest --service=django-app-apitest --port=8000-tcp
# 18. access application
https://*.2.rahtiapp.fi
# 19. cleanup old pods & builds (optional)
oc delete pod --field-selector=status.phase==Succeeded
oc delete pod --field-selector=status.phase==Failed
oc delete build --all
# 20. Debug internal server error:
oc get pods -l app=django-app-apitest -o wide
oc logs -f pod/<POD_NAME>
Now refresh:
https://django-app-apitest-djangoapitesttodoapp.2.rahtiapp.fi/api
# 21. Make a secret key for djnago
python -c "import secrets; print(secrets.token_urlsafe(50))"
# 22. set it as a environment variable in Rahti
oc set env dc/django-app-apitest SECRET_KEY='PASTE_THE_VALUE_HERE'



```
