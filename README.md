Simple API with Authentication or just authentication if you need

This project was made for use with [Email Auth Template](https://github.com/ThallyssonKlein/EmailAuthAppTemplate) or as a template by itself

Run on template directory:
```
pipenv install;pipenv run python manage.py runserver localhost:8000
```

**Ps:** Needs Python3 + Pipenv. For reasons of Github security policies, I cannot keep the django secret exposed. For this code to work create a .env at the root of the directory and set DJANG_SECRET = [your secret].
