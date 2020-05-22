# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.execute import Execute  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGetItemController(BaseTestCase):
    """GetItemController integration test stubs"""

    def test_get_item_post(self):
        """Test case for get_item_post

        Get a subset of a data set 'slice' it
        """
        body = Execute()
        response = self.client.open(
            '/v1/get_item',
            method='POST',
            data=json.dumps(body),
            content_type='*/*')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
