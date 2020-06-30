# Glowing lab diary

## Requirements

- Python 3.7
- Django
- Django REST

The library also uses **Vuejs**.

## How to run

Create a virtual env with python 3.7 and install requirements.
```
virtualenv -p python3.7 env
pip install -r requirements.txt
```

Create a `parameters.py` file in **lab_diary** folder.

Initialize django.
```
python manage.py migrate
python manage.py createsuperuser
```
The creation of a super user is needed since the application requires logged in user.

Run!
```
python manage.py runserver
```

## How to start

Log in to the admin interface (usually http://localhost:8000/admin/), create a few tags, at least one status with ID 0 and you're ready!

# What does it look like?

![Homepage example](https://github.com/giliam/glowing-lab-diary/blob/master/docs/example.png)
