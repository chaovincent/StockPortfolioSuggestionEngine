# stock-portfolio-suggestion-web-app

A stock portfolio suggestion web application using Python's Flask web framework.

## Prerequisites

* Linux, Mac, or Windows machine
* Python (Python 3.5.2 was used for this project)
* Flask web framework

## Getting Started

### Installing Python

Starting off, Python must be installed on your system. Python 3.5.2 was the version used for this project. If your
operating system does not have Python pre-installed, you can head over to Python's official website to download it.

You can check if Python is installed on your system by simply typing ```python``` or ```python3``` in the terminal.

```
$ python
Python 3.5.2 (default, Nov 23 2017, 16:37:01)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> -

```

### Create a Virtual Environment

Creating a virtual environment for your project is an important practice when developing applications. A virtual
environment addresses the issue of maintaining different versions of packages for different applications. Applications
developed with one version of a package may not be fully compatible with another version. A virtual environment can be
created with the following command:

```
$ python3 -m venv my_venv_name
``` 

Next, the virtual environment must be activated as such:

```
$ source my_venv_name/bin/activate
(venv) $ _
```

For Microsoft Windows, the activation command is slightly different:

```bash
$ my_venv_name\Scripts\activate
(venv) $ _
```

### Installing Flask

Python comes with a tool called ```pip``` which is used to easily install Python packages, such as Flask. To install 
the Flask package, you use ```pip``` as follows:

```
$ pip install flask
```

## Running the Application

The Flask application is ran with a localhost server (IP address 127.0.0.1). Network servers usually listen for
connections on a specific port number. Because this application is running in a developmental environment, Flask uses
the freely available port 5000. 

Flask first needs to be told how to import the application, by setting the ```FLASK_APP``` environmental variable:

```
(venv) $ export FLASK_APP=stock-portfolio-suggestion-web-app.py
```

On Microsoft Windows, use ```set``` instead of ```export``` in the command above.

You can now run the application with the following command:

```
(venv) $ flask run
 * Serving Flask app "app"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
