# Glowing lab diary

## Requirements

- Python 3.7
- Django
- Django REST

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

## What does it look like?

![Homepage example](https://github.com/giliam/glowing-lab-diary/blob/master/docs/example.png)
