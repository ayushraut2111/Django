import requests
import json
# url="http://127.0.0.1:8000/student/1"
# r=requests.get(url=url)
# data=r.json()
# print(data)
url="http://127.0.0.1:8000/studentdata"
dic={
    'name':'arvind',
    'roll':'4',
    'subject':'commerce'
}
json_data=json.dumps(dic)
# print(json_data)
r=requests.post(url=url,data=json_data)
