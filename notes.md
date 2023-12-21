## Day 1 [14-12-23]

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

### Views in Django

Django views are Python functions that takes https requests and returns http response. Views are usually put in a file called `views.py` located on application's folder.

You write functions in this file and hadle request and return the response.

### Urls in Django

You need to create this file in your application folder and then add the respective endpoint and link them with the appropriate views.

There is Urls file in the core folder and you need to link a endpoint with the applications urls file.

The name of the file is commanly is `urls.py`.
