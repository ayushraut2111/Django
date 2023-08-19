import json
import requests

headers={'content-type':'application/json'}

url="http://127.0.0.1:8000/details/"

file='jsondata.json'
data=None
with open(file,"r",encoding='utf-8') as json_file:
    data=json.load(json_file)

print(len(data))
for i in data:
    json_data=json.dumps(i)
    r=requests.post(url=url,data=json_data,headers=headers)


# def filter_data():
#     dic={'end_year':2013}
#     # dic=None
#     json_d=json.dumps(dic)
#     r=requests.get(url=url,data=json_d,headers=dic)
#     print(r.json())

# # filter_data()


# def range():
#     url="http://127.0.0.1:8000/details/?region=Europe"
#     r=requests.get(url=url,headers=headers)
#     print(len(r.json()))

# range()

