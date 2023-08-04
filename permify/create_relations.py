import requests


import json
import requests

url = "http://localhost:3476/v1/tenants/t1/relationships/write"
headers = {"Content-Type": "application/json"}

payload = {
    "metadata": {
        "schema_version": "cj01icetel4c73aa6830"
    },
    "tuples": [
        {
            "entity": {
                "type": "organization",
                "id": "1"
            },
            "relation": "admin",
            "subject": {
                "type": "user",
                "id": "1",
                "relation": ""
            }
        }
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

if response.status_code == 200:
    print("Relation created successfully!",response.text)
else:
    print("Error creating relation: ", response.text)

