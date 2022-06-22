# FASTAPI ( Python )

FastAPI is a Web framework for developing RESTful APIs in Python. FastAPI is based on Pydantic and type hints to validate, serialize, and deserialize data, and automatically auto-generate OpenAPI documents. It fully supports asynchronous programming and can run with Uvicorn and Gunicorn.


Clone the project

```
git clone https://github.com/muhammadqazi/UDEMY-FastAPI.git
```

Make env for python, Make sure you have python install in your system. Run the commands below in the project directory

##### WINDOWS USERS

```
python -m venv env
env\Scripts\activate
```

##### MAC || LINUX USERS

```
python3 -m venv env
source ./env/bin/activate
```

Run the dev server

```console
uvicorn main:app --reload --port 8000
```

Here main is the name of the file and app is the instance inside that file.