# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.common import util


class File(Model):

    def __init__(self, file_type=None, file_base64=None):  # noqa: E501
        """File - a model defined in OpenAPI

        :param file_type: The file_type of this File.  # noqa: E501
        :type file_type: str
        :param file_base64: The file_base64 of this File.  # noqa: E501
        :type file_base64: str
        """
        self.openapi_types = {
            'file_type': str,
            'file_base64': str
        }

        self.attribute_map = {
            'file_type': 'fileType',
            'file_base64': 'fileBase64'
        }

        self._file_type = file_type
        self._file_base64 = file_base64

    @classmethod
    def from_dict(cls, dikt) -> 'File':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The File of this File.  # noqa: E501
        :rtype: File
        """
        return util.deserialize_model(dikt, cls)

    @property
    def file_type(self):
        """Gets the file_type of this File.

        file type  # noqa: E501

        :return: The file_type of this File.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this File.

        file type  # noqa: E501

        :param file_type: The file_type of this File.
        :type file_type: str
        """
        allowed_values = ["DOCX", "PDF"]  # noqa: E501
        if file_type not in allowed_values:
            raise ValueError(
                "Invalid value for `file_type` ({0}), must be one of {1}"
                .format(file_type, allowed_values)
            )

        self._file_type = file_type

    @property
    def file_base64(self):
        """Gets the file_base64 of this File.

        file's base64  # noqa: E501

        :return: The file_base64 of this File.
        :rtype: str
        """
        return self._file_base64

    @file_base64.setter
    def file_base64(self, file_base64):
        """Sets the file_base64 of this File.

        file's base64  # noqa: E501

        :param file_base64: The file_base64 of this File.
        :type file_base64: str
        """

        self._file_base64 = file_base64
