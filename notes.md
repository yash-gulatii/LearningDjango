### What is Django?

**Django**

Free and open-source framework for building web apps with Python. Django is a framework for building web applications.

**Django Features**

- The admin site
- Object-relational mapper (ORM)
- Authentication
- Caching

**Rendering**

Generating the HTML for client(user accessing site) is known as Rendering.

**Server-side Rendering**

The server generated the HTML for a page, which then sent to the client. Example - Django, ASP.Net, and Express.

**Client-side Rendering**

The HTML is generated on the client-side, using JavaScript to render content in the browser. Examples - React, Angular, and Vue.

**Development Environment**

- Python
- Pipenv (module)
- Visual Studio Code

### Setting up Django Project

**Installing Django**

```
pipenv install django
```

**Starting a Project**

```
django-admin startproject {projectname}
```

**Running the Project**

```
python manage.py runserver
```

**Starting a Application whitin the Project**

```
python manage.py startapp {appname}
```

**Add the app to the Project**

To add the app to the project you need to add the name of the app in the "settings.py"

### Reactivate pipenv in shell

`C:\Users\yashg\.virtualenvs\storefront-j-kdlpIn\Scripts\activate.bat`

This will be different for every project.

### Views in Django

Django views are Python functions that takes https requests and returns http response. Views are usually put in a file called `views.py` located on application's folder.

You write functions in this file and hadle request and return the response.

### Urls in Django

You need to create this file in your application folder and then add the respective endpoint and link them with the appropriate views.

There is Urls file in the core folder and you need to link a endpoint with the applications urls file.

The name of the file is commanly is `urls.py`.

### Django Models

A Django model is the built-in feature that Django uses to create tables, their fields, and various constraints. In short, Django Models is the SQL Database one uses with Django. SQL (Structured Query Language) is complex and involves a lot of different queries for creating, deleting, updating, or any other stuff related to a database. Django models simplify the tasks and organize tables into models. Generally, each model maps to a single database table. 

**Tips to make django models for a project**

- Divide different functionalities into different applications
- Don't make depent applications [an application which depends on another applicaiton]
- The application must be self-contained
- There should be zero coupling in the applicaiton
- Don't make all the functionalities in one applicaiton and also don't make an applicaiton for every functionalities
- Application should be highly cohesion [focused]

**[Model Field Reference](https://docs.djangoproject.com/en/5.0/ref/models/fields/#field-types)**

### Creating classes in with Django Models

**Defining classes**

`class className(models.Model):`

**Adding fields**

`fieldName = models.fieldType(attributes)`

**These above code should be written in the applications `models.py` file**

### Creating Generic relations in Django

To make the tag app generic we are adding a app called content type which is build in the django. The importing the app we use it and get the content type of the object and the ID. Then we can relate it to the tags.