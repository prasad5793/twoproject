Django Tutorial
-->	Create a Virtual Environment (py -m venv venv)
-->	Install Django  (-py -m pip install Django)
-->	Django Create Project (Django-admin startproject testproject)
-->	Django Create App (py manage.py startapp testapps)
        mode to VCode (code .)
-->	Django Views
                * update setting file -add apps
                * create template folder and html Files
                * create urls.py file under apps folder
                * project urls update-  path('', include('index.html')),   include
                * from django.urls import path/ from . import views
                * urlpatterns= [path('testapps/', views.testapps, name='testapps'),
]
-->	Django URLs
-->	Django Templates
-->	Django Models
-->	Django Insert Data
-->	Django Update Data
-->	Django Delete Data
-->	Django Update Model



Display Data
Prepare Template and View
Add Link to Details
Add Master Template
Add Main Index Page
Django 404 Template
Add Test View

Admin
Django Admin
Create User
Include Models
Set List Display
Update Members
Add Members
Delete Members

Django Syntax
Django Variables
Django Tags
Django If Else
Django For Loop
Django Comment
Django Include

QuerySets
QuerySet Introduction
QuerySet Get
QuerySet Filter
QuerySet Order By

Static Files
Add Static Files
Install WhiteNoise
Collect Static Files
Add Global Static Files
Add Styles to the Project

PostgreSQL
PostgreSQL Intro
Create AWS Account
Create Database in RDS
Connect to Database
Add Members

Deploy Django
Elastic Beanstalk (EB)
Create requirements.txt
Create django.config
Create .zip File
Deploy with EB
Update Project

More Django
Add Slug Field
Add Bootstrap 5