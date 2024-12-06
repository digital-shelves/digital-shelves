# Digital Shelves
Many students depend on their campus libraries to loan them important items such as laptops, headphones, calculators, etc. However, there is not an easy way to find out what resources are available. Though students could go in-person, they may not necessarily be able to do so. As a result, some students may not end up utilizing their library resources which could otherwise boost their academic performance. To fix this issue, we will create a web-based application where students can easily see what items are available without having to physically go to the library.

## Dependencies
.NET 8.0

## Tech Stack
Blazor WebAssembly Application with a SQL database on the backend (subject to change)


## How to install Python backend dependencies
The digital-shelves/backend directory contains the Django project which contains all the boilerplate code for the server. 
To use it you must install [Python 3.12](https://www.python.org/downloads/release/python-3123/). During the install, make sure to check the box to add Python to your PATH enviornment variable. After installing, cd to the digital-shelves directory and run these commands:

```
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

Once that's done, you can navigate to digital-shelves/backend and run 
```
python manage.py runserver
```
The server should then be available to view at http://127.0.0.1:8000

At the moment the database on the server is using SQLite3.
Git good
