import requests


import json
import requests

url = "http://localhost:3476/v1/tenants/t2/permissions/check"
headers = {"Content-Type": "application/json"}

payload = {
    "metadata": {
        "snap_token": "qFwGj5MweBc=",
        "schema_version": "cj6fk88ochac73dd3ptg",
        "depth": 100
    },
    "entity": {
        "type": "post",
        "id": "p1"
    },
    "permission": "view_post",
    "subject": {
        "type": "user",
        "id": "u1"
    }
}
response = requests.post(url, headers=headers, data=json.dumps(payload))

if response.status_code == 200:
    print("Status = ",response.text)
else:
    print("Error", response.text)