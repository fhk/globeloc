# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Body(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, upload_array: str=None, user_id: str=None, uuid: str=None):  # noqa: E501
        """Body - a model defined in Swagger

        :param upload_array: The upload_array of this Body.  # noqa: E501
        :type upload_array: str
        :param user_id: The user_id of this Body.  # noqa: E501
        :type user_id: str
        :param uuid: The uuid of this Body.  # noqa: E501
        :type uuid: str
        """
        self.swagger_types = {
            'upload_array': str,
            'user_id': str,
            'uuid': str
        }

        self.attribute_map = {
            'upload_array': 'upload_array',
            'user_id': 'user_id',
            'uuid': 'uuid'
        }
        self._upload_array = upload_array
        self._user_id = user_id
        self._uuid = uuid

    @classmethod
    def from_dict(cls, dikt) -> 'Body':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body of this Body.  # noqa: E501
        :rtype: Body
        """
        return util.deserialize_model(dikt, cls)

    @property
    def upload_array(self) -> str:
        """Gets the upload_array of this Body.

        Stores data and assignes a unique_id if one is not given, otherwise overwrites.  # noqa: E501

        :return: The upload_array of this Body.
        :rtype: str
        """
        return self._upload_array

    @upload_array.setter
    def upload_array(self, upload_array: str):
        """Sets the upload_array of this Body.

        Stores data and assignes a unique_id if one is not given, otherwise overwrites.  # noqa: E501

        :param upload_array: The upload_array of this Body.
        :type upload_array: str
        """
        if upload_array is None:
            raise ValueError("Invalid value for `upload_array`, must not be `None`")  # noqa: E501

        self._upload_array = upload_array

    @property
    def user_id(self) -> str:
        """Gets the user_id of this Body.

        user_id  # noqa: E501

        :return: The user_id of this Body.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        """Sets the user_id of this Body.

        user_id  # noqa: E501

        :param user_id: The user_id of this Body.
        :type user_id: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def uuid(self) -> str:
        """Gets the uuid of this Body.

        uuid  # noqa: E501

        :return: The uuid of this Body.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid: str):
        """Sets the uuid of this Body.

        uuid  # noqa: E501

        :param uuid: The uuid of this Body.
        :type uuid: str
        """
        if uuid is None:
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid
