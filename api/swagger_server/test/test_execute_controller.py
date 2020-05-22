# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.data_uid import DataUID  # noqa: E501
from swagger_server.models.execute import Execute  # noqa: E501
from swagger_server.test import BaseTestCase


class TestExecuteController(BaseTestCase):
    """ExecuteController integration test stubs"""

    def test_get_order_by_id(self):
        """Test case for get_order_by_id

        execute a single/multi array operation and get the result
        """
        body = Execute()
        response = self.client.open(
            '/v1/execute',
            method='POST',
            data=json.dumps(body),
            content_type='*/*')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
