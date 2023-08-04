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
        service_name='fn_create_relation_service',
        span_name='create-relation',
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
        return response.Response(
            ctx, response_data=json.dumps(
                {"message": "Hello {0}".format(name)}),
            headers={"Content-Type": "application/json"}
        )
