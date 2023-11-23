from fastapi import FastAPI
from models import Employee
from mongoengine import connect
import json

app = FastAPI()
connect(db="hrms", host="localhost", port=27017)


@app.get('/')
def home():
    return {"message": "mongodb setup"}


@app.get('/get_all_employees')
def get_all_employees():
    employees = json.loads(Employee.objects().to_json())
    return {"employees": employees}
