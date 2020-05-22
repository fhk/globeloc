# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.data_uid import DataUID  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSaveController(BaseTestCase):
    """SaveController integration test stubs"""

    def test_save_get(self):
        """Test case for save_get

        Save a data set, by unique_id or get a new one
        """
        body = DataUID()
        response = self.client.open(
            '/v1/save',
            method='GET',
            data=json.dumps(body),
            content_type='*/*')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
