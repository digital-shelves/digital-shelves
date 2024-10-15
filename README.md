# How to install Python backend dependencies
The digital-shelves/backend directory contains the Django project which contains all the boilerplate code for the server. 
To use it you must install [Python 3.12](https://www.python.org/downloads/release/python-3123/). During the install, make sure to check the box to add Python to your PATH enviornment variable. After installing, cd to the digital-shelves directory and run these commands:

```
python -m venv .venv
./.venv/Scripts/activate
pip install -r requirements.txt
```

Once that's done, you can navigate to digital-shelves/backend and run 
```
python manage.py runserver
```
The server should then be available to view at https://127.0.0.1:8000

At the moment the database on the server is using SQLite3.