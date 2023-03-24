# Technical interview challenge IEB

## Technologies
***
A list of technologies used within the project:
* [Python](https://www.python.org/): Version 3.10.0 
* [Django](https://www.djangoproject.com/): Version 4.0
* [Django Rest Framework](https://www.django-rest-framework.org/): Version 3.14.0
* [Node Js](https://nodejs.org/en): Version 16.13.0
* [Pytest](https://pypi.org/project/pytest/): Version 7.2.2

## Installation
***
A little intro about the installation. 
```
$ git clone https://github.com/matiasfeliu92/technical_interview_challenge_IEB.git
$ cd technical_interview_challenge_IEB
$ pip install virtualenv
$ virtualenv IEB
$ IEB/Scripts/activate (to activate virtual env)
$ pip install -r requirements.txt
$ npm install
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver (to start the application)
$ npm start (start socket connection, make http request for get data of product)
$ pytest ./service3app/tests.py (make testing of api endpoints)
```