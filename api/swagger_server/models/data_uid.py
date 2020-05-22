# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class DataUID(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, data_id: str=None, user_id: str=None):  # noqa: E501
        """DataUID - a model defined in Swagger

        :param data_id: The data_id of this DataUID.  # noqa: E501
        :type data_id: str
        :param user_id: The user_id of this DataUID.  # noqa: E501
        :type user_id: str
        """
        self.swagger_types = {
            'data_id': str,
            'user_id': str
        }

        self.attribute_map = {
            'data_id': 'data_id',
            'user_id': 'user_id'
        }
        self._data_id = data_id
        self._user_id = user_id

    @classmethod
    def from_dict(cls, dikt) -> 'DataUID':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DataUID of this DataUID.  # noqa: E501
        :rtype: DataUID
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data_id(self) -> str:
        """Gets the data_id of this DataUID.


        :return: The data_id of this DataUID.
        :rtype: str
        """
        return self._data_id

    @data_id.setter
    def data_id(self, data_id: str):
        """Sets the data_id of this DataUID.


        :param data_id: The data_id of this DataUID.
        :type data_id: str
        """

        self._data_id = data_id

    @property
    def user_id(self) -> str:
        """Gets the user_id of this DataUID.


        :return: The user_id of this DataUID.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        """Sets the user_id of this DataUID.


        :param user_id: The user_id of this DataUID.
        :type user_id: str
        """

        self._user_id = user_id
