# Django_blog
Awesome blog 

This is a blog app. User can create his account and share his thaughts to other users.

# Requirements

* python > 3.5


Create virtual environment in django_blog folder and activate it. (optional)
```
python -m venv .env
.env/Scripts/activate
``` 

Install required packages
```
pip install -r requirments.txt
```

Now make required migrations & migrate
```
python manage.py makemigrations
python manage.py migrate
```

Now simply run
```
python manage.py runserver
```
