# Bikeshare Project API

A Flask web app that provides API endpoints to the front end Vue app for analyzing **Bikeshare** cities data project as part of the **Udacity Data Professional** scholarship provided by **EgyFWD**.

A full functioning version of this app is present at https://bikeshare.ihabtag.com

## Execution instructions on localhost
This app is built by Flask as a back-end and Vue.js as front-end.

Both parts should be deployed and proper configuration of Axios requests links in the Vue.js part is necessary for this app to work as expected. 

## The Flask back-end

 Clone the project files to the desired project directory.
   
 Install virtual environment.
 
 ```
$ pip install virtualenv
```
Then create a virtual environment in your project directory.
```
$ virtualenv env
```
Then activate the environment with:
```
$ source env/bin/activate
```
Then install your dependencies with pip.
```
pip install -r requirements.txt
```
Then run the project:

    $ python wsgi.py

Then any time you return to the project, run `source env/bin/activate` again so that the dependencies can be found.

## The Vue.js front-end
Refer to the Vue part README [here](https://github.com/IhabTag/bikeshare-vue/blob/master/README.md) for more instructions.

## Credits
- Answers to a lot of questions on [Stackoverflow.com](https://stackoverflow.com/questions).
- Pandas official [documentation](https://pandas.pydata.org/docs/).
- Creating APIs with Python and Flask from [programminghistorian.org](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask).
- Flask deployment from [flask.palletsprojects.com](https://flask.palletsprojects.com/en/1.1.x/deploying/).
## Third Party Packages
- [Flask](https://github.com/pallets/flask).
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/).
- [Pandas](https://pandas.pydata.org/).
- [NumPy](https://numpy.org/).
- [Gunicorn](https://gunicorn.org/).