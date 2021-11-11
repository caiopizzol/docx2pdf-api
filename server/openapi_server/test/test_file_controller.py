# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.file import File  # noqa: E501
from openapi_server.test import BaseTestCase


class TestFileController(BaseTestCase):
    """FileController integration test stubs"""

    def test_file_convert(self):
        """Test case for file_convert

        converts a DOCX file into PDF
        """
        file = {
  "fileType" : "DOCX",
  "fileBase64" : "fileBase64"
}
        headers = { 
            'api_key': 'special-key',
        }
        response = self.client.open(
            '/v1/file/convert',
            method='POST',
            headers=headers,
            data=json.dumps(file),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
