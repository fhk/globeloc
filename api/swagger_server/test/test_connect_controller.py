# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.user_uid import UserUID  # noqa: E501
from swagger_server.test import BaseTestCase


class TestConnectController(BaseTestCase):
    """ConnectController integration test stubs"""

    def test_connect_post(self):
        """Test case for connect_post

        Submit your unique api key and register a client
        """
        body = UserUID()
        response = self.client.open(
            '/v1/connect',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
