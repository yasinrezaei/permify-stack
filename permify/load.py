import json
import requests



"""
  This is a test file for workload.
"""


# create schema

create_schema_url = "http://localhost:3476/v1/tenants/t1/schemas/write"
headers = {"Content-Type": "application/json"}
schema = {
    "schema":"entity user {} entity group { relation member @user relation admin @user relation moderator @user action create = member action join = member action leave = member action invite_to_group = admin action remove_from_group = admin or moderator action edit_settings = admin or moderator action post_to_group = member action comment_on_post = member action view_group_insights = admin or moderator } entity post { relation owner @user relation group @group action view_post = owner or group.member action edit_post = owner or group.admin action delete_post = owner or group.admin permission group_member = group.member } entity comment { relation owner @user relation post @post action view_comment = owner or post.group_member action edit_comment = owner action delete_comment = owner } entity like { relation owner @user relation post @post action like_post = owner or post.group_member action unlike_post = owner or post.group_member } entity poll { relation owner @user relation group @group action create_poll = owner or group.admin action view_poll = owner or group.member action edit_poll = owner or group.admin action delete_poll = owner or group.admin } entity file { relation owner @user relation group @group action upload_file = owner or group.member action view_file = owner or group.member action delete_file = owner or group.admin } entity event { relation owner @user relation group @group action create_event = owner or group.admin action view_event = owner or group.member action edit_event = owner or group.admin action delete_event = owner or group.admin action RSVP_to_event = owner or group.member }"
}

response = requests.post(create_schema_url, headers=headers, json=schema)

if response.status_code == 200:
    print("Scheam created successfully!",response.text)
    schema_creation_response = response.json()
else:
    print("Error creating schema: ", response.text)


# create relation

create_relation_url = "http://localhost:3476/v1/tenants/t1/relationships/write"

relation = {
    "metadata": {
        "schema_version": schema_creation_response['schema_version']
    },
    "tuples": [
        {
            "entity": {
                "type": "post",
                "id": "p1"
            },
            "relation": "owner",
            "subject": {
                "type": "user",
                "id": "u1",
                "relation": ""
            }
        }
    ]
}

response = requests.post(create_relation_url, headers=headers, data=json.dumps(relation))

if response.status_code == 200:
    print("Relation created successfully!",response.text)
else:
    print("Error creating relation: ", response.text)


# check access

check_access_url = "http://localhost:3477/v1/tenants/t2/permissions/check"


permission = {
    "metadata": {
        "schema_version": schema_creation_response['schema_version'],
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


response = requests.post(check_access_url, headers=headers, data=json.dumps(permission))

if response.status_code == 200:
    print("Status = ",response.text)
else:
    print("Error", response.text)