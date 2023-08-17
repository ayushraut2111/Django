import requests
import json

headers={'content-type':'application/json'}
def gettoken():
    url="http://127.0.0.1:8000/gettoken"
    dt={
        'username':'admin',
        'password':'admin'
    }
    data=json.dumps(dt)
    print(data)
    r=requests.post(url=url,data=data,headers=headers)
    p=r.json()
    print(p)
    return p.get('token')

gettoken()
# http://127.0.0.1:8000/student/ 'Authorization:Token 04d34b422dc54c506ca919e5cefb60851e73289d'
def getdata():
    x=gettoken()
    # url="http://127.0.0.1:8000/student/ 'Authorization:Token "+str(x)+"'"
    url="http://127.0.0.1:8000/student/ 'Authorization:Token 04d34b422dc54c506ca919e5cefb60851e73289d'"
    print(url)
    r=requests.get(url=url,headers=headers)
    print(r.json())

# getdata()



    # {
    #     "name": "anish",
    #     "roll": 2,
    #     "subject": "cse"
    # }
