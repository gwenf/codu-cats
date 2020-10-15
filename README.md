# Codú Cats

This app provides an API with information about all your favorite cat breeds!

## Setup Steps

### Part 1

1. Must have Python 3 & Postgres version 12.x installed and running
1. `django-admin startproject CoduCats`
1. Create a virtual environment: `python -m venv venv`
1. Go into your virtual environment: `source venv/bin/activate`
1. Rename the CoduCats folder to config
1. Setup Postgres in Django:

```
'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'coducat',
    'USER': 'cc_admin',
    'PASSWORD': '',
    'HOST': 'localhost',
    'PORT': '',
}
```

1. Setup Database in Postgres
    1. Create the database: `CREATE DATABASE coducat;`
    1. Create DB user: `CREATE USER cc_admin;
    1. Grant privilages to user for our database: `GRANT ALL PRIVILEGES ON DATABASE coducat TO cc_admin;`
    1. Run migrations: `python manage.py migrate`
1. Create an admin user for logging into the Django admin interface: `python manage.py createsuperuser`
1. Run the app: `python manage.py runserver`
1. View the API at `localhost:8000` and the admin interface at `localhost:8000/admin`

### Part 2

1. Create apps for Pages and for Breeds
1. Setup URLs
1. Setup templates for home page: `'DIRS': [os.path.join(BASE_DIR, 'apps/templates')]`
1. Create Models
1. Setup Admin interface
1. Setup Views

### Part 3

1. Setup nested routes
1. Pagination
1. Timestamp util for models

## API

**/**

Landing Page

**/api/breeds** & **/api/breeds/:id**

Resource and items for breeds

**/api/breeds/:id/locations** & **/api/breeds/:id/locations/:location_id**

Locations for specific breeds

## Schema

**Breed**

* name
* origin
* body_type
* coat_length
* pattern

**Locations**

* name
* breed
