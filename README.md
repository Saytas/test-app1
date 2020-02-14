# test-app1
<code>$ cd Dev 


$ mkdir -p working_environment_name


$ virtualenv -p python3 . //Creates a virtual environment inside the directory that keeps the requirements seperate
--OR---
$ virtualenv working_environment_name 
--OR---
$ virtualenv working_environment_name -p python3 // Indicating a specific version of python
--OR---
$ virtualenv working_environment_name -p /usr/loal/bin/python3.6.0
--OR---
$ virtualenv . -p python3


$ source bin/activate //To activate the virtual environment)


(trydjango)$ pip install django==2.0.7


$ deactivate // To deactivate - end the virtual environment


$ pip freeze // shows all the available packages


$ pip install Django==1.11.4


$ mkdir -p src


$ django-admin startproject project_name . // To start the project IMPORTANT: DO NOT FORGET .


$ python manage.py runserver // To run the server


$ 


$ 


$ 
<code>