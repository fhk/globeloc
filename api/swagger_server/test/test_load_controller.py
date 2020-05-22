# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.load import Load  # noqa: E501
from swagger_server.test import BaseTestCase


class TestLoadController(BaseTestCase):
    """LoadController integration test stubs"""

    def test_load_get(self):
        """Test case for load_get

        Load a data set
        """
        body = Load()
        response = self.client.open(
            '/v1/load',
            method='GET',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
