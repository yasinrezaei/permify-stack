import io
import json
import logging
import requests

from fdk import response
from py_zipkin.zipkin import zipkin_span
from py_zipkin.transport import BaseTransportHandler

from py_zipkin.transport import BaseTransportHandler

class HttpTransport(BaseTransportHandler):

    def get_max_payload_bytes(self):
        return None

    def send(self, encoded_span):
        # The collector expects a thrift-encoded list of spans.
        response = requests.post(
            'http://192.168.43.67:9411/api/v2/spans',
            data=encoded_span,
            headers={'Content-Type': 'application/x-thrift'},
        )
        print('Response status code:', response.status_code)
        print('Response text:', response.text)


# Create the transport handler instance
some_handler = HttpTransport()


def handler(ctx, data: io.BytesIO = None):
    with zipkin_span(
        service_name='fn_create_schema_service',
        span_name='create-schema',
        transport_handler=some_handler,
        port=42,
        sample_rate=100.0,  # 100% of the requests will be traced
    ):
        name = "World"
        try:
            body = json.loads(data.getvalue())
            name = body.get("name")
        except (Exception, ValueError) as ex:
            logging.getLogger().info('error parsing json payload: ' + str(ex))

        logging.getLogger().info("Inside Python Hello World function")

        # Prepare the data for the POST request
        post_data = {
        "schema":"entity user {} entity group { relation member @user relation admin @user relation moderator @user action create = member action join = member action leave = member action invite_to_group = admin action remove_from_group = admin or moderator action edit_settings = admin or moderator action post_to_group = member action comment_on_post = member action view_group_insights = admin or moderator } entity post { relation owner @user relation group @group action view_post = owner or group.member action edit_post = owner or group.admin action delete_post = owner or group.admin permission group_member = group.member } entity comment { relation owner @user relation post @post action view_comment = owner or post.group_member action edit_comment = owner action delete_comment = owner } entity like { relation owner @user relation post @post action like_post = owner or post.group_member action unlike_post = owner or post.group_member } entity poll { relation owner @user relation group @group action create_poll = owner or group.admin action view_poll = owner or group.member action edit_poll = owner or group.admin action delete_poll = owner or group.admin } entity file { relation owner @user relation group @group action upload_file = owner or group.member action view_file = owner or group.member action delete_file = owner or group.admin } entity event { relation owner @user relation group @group action create_event = owner or group.admin action view_event = owner or group.member action edit_event = owner or group.admin action delete_event = owner or group.admin action RSVP_to_event = owner or group.member }"
        }

        # Send a POST request to an external API
        api_response = requests.post('http://192.168.43.67:3476/v1/tenants/t1/schemas/write', json=post_data)

        # Parse the API response as JSON
        api_data = api_response.json()

        return response.Response(
            ctx, 
            response_data=json.dumps({
                "message": "Hello {0}".format(name),
                "api_response": api_data  # Include the API response in the function's output
            }),
            headers={"Content-Type": "application/json"}
        )
