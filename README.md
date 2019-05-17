# Instachat

A lightweight, PostgreSQL/Python Flask/Angular5-based chat app. Has support for images, texts, hashtags and replies on texts.

## How to run

* Make sure you have Node.JS, PostgreSQL and Python Flask installed.

* Clone the project folder into your machine.

* Run npm install in the project's root folder. Let that process finish.

* Included in this release, there is a file called **schema.sql**. This schema will provide the appropriate database to the application. To install it, run the following commands in order:

    * sudo -i -U postgres (in a UNIX-based CLI)
    
    * createdb instachat
    
    * createuser -e -P instadev, with password InstaC
    
    * cd /path/to/project/

    * psql -d instachat -f schema.sql

* Using a Python IDE or the Python CLI, run Main.py.

* navigate your browser to the route http://localhost:4200/



## Who are the creators?

* <a href='https://github.com/enrique-amt/'>Enrique A. Marrero</a>
* <a href='https://github.com/brianmunoz/'>Brian Muñoz</a>
* <a href='https://github.com/eduardonieves/'>Eduardo Nieves</a>


