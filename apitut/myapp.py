import requests
import json


url="http://127.0.0.1:8000/student/"

def read_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    
    json_data=json.dumps(data)

    r=requests.get(url=url,data=json_data)

    print(r.json())

# read_data()

def create_data():
    d={
        'name':'ayush',
        'roll':13,
        'subject':'computer'
    }
    json_data=json.dumps(d)

    r=requests.post(url=url,data=json_data)
    print(r.json())


create_data()

def update_data():
    d={
        'id':6,
        'name':'sanjeev',
        'roll':52,
    }
    json_data=json.dumps(d)
    r=requests.put(url=url,data=json_data)
    print(r.json())

# update_data()

def delete_data():
    data={'id':4}
    json_data=json.dumps(data)
    r=requests.delete(url=url,data=json_data)
    print(r.json())

# delete_data()