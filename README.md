# djapp-crud - Django app template

This template was created for agile development in the CRUD applications, using Class Based Views and Unit Tests.

## Usage

1. Create app with this command:

```bash
$ python manage.py startapp --template ~/Projects/djapp-crud --extension=py,html <app_name>
```

### Pre requisites

 - django-crispy-forms: [Source Code](https://github.com/maraujop/django-crispy-forms)


### Structure of app

```
appname
├── README.md
├── __init__.py
├── forms.py
├── models.py
├── templates
│   └── app_name
│       ├── confirm_delete.html
│       ├── list.html
│       ├── new.html
│       └── update.html
├── tests.py
├── urls.py
└── views.py
```