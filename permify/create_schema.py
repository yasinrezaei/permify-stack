import requests

url = "http://localhost:3476/v1/tenants/t1/schemas/write"
headers = {"Content-Type": "application/json"}
data = {
    "schema":"entity user {} entity group { relation member @user relation admin @user relation moderator @user action create = member action join = member action leave = member action invite_to_group = admin action remove_from_group = admin or moderator action edit_settings = admin or moderator action post_to_group = member action comment_on_post = member action view_group_insights = admin or moderator } entity post { relation owner @user relation group @group action view_post = owner or group.member action edit_post = owner or group.admin action delete_post = owner or group.admin permission group_member = group.member } entity comment { relation owner @user relation post @post action view_comment = owner or post.group_member action edit_comment = owner action delete_comment = owner } entity like { relation owner @user relation post @post action like_post = owner or post.group_member action unlike_post = owner or post.group_member } entity poll { relation owner @user relation group @group action create_poll = owner or group.admin action view_poll = owner or group.member action edit_poll = owner or group.admin action delete_poll = owner or group.admin } entity file { relation owner @user relation group @group action upload_file = owner or group.member action view_file = owner or group.member action delete_file = owner or group.admin } entity event { relation owner @user relation group @group action create_event = owner or group.admin action view_event = owner or group.member action edit_event = owner or group.admin action delete_event = owner or group.admin action RSVP_to_event = owner or group.member }"
}

response = requests.post(url, headers=headers, json=data)
print(response.json())

