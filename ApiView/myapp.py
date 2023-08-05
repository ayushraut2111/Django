import requests
import json

url="http://127.0.0.1:8000/student/"
headers={'content-type':'application/json'}


def read_data():
    d={'id':1}
    jd=json.dumps(d)
    r=requests.get(url=url,data=jd,headers=headers)
    print(r.json())

# read_data()

def create_data():
    d={
        'name':'shivam',
        'roll':49,
        'subject':'data science'
    }
    json_data=json.dumps(d)
    r=requests.post(url=url,data=json_data,headers=headers)
    print(r.json())

# create_data()

def update_data():
    d={
        'id':7,
        'name':'sanjay',
        'roll':20,
        'subject':'ECE'
    }
    jd=json.dumps(d)
    r=requests.put(url=url,data=jd,headers=headers)
    print(r.json())

# update_data()

def delete_data():
    json_data=json.dumps({'id':5})
    r=requests.delete(url=url,data=json_data,headers=headers)
    print(r.json())

delete_data()