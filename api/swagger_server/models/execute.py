# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Execute(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, data_ids: List[str]=None, user_id: str=None, operation: str=None):  # noqa: E501
        """Execute - a model defined in Swagger

        :param data_ids: The data_ids of this Execute.  # noqa: E501
        :type data_ids: List[str]
        :param user_id: The user_id of this Execute.  # noqa: E501
        :type user_id: str
        :param operation: The operation of this Execute.  # noqa: E501
        :type operation: str
        """
        self.swagger_types = {
            'data_ids': List[str],
            'user_id': str,
            'operation': str
        }

        self.attribute_map = {
            'data_ids': 'data_ids',
            'user_id': 'user_id',
            'operation': 'operation'
        }
        self._data_ids = data_ids
        self._user_id = user_id
        self._operation = operation

    @classmethod
    def from_dict(cls, dikt) -> 'Execute':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Execute of this Execute.  # noqa: E501
        :rtype: Execute
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data_ids(self) -> List[str]:
        """Gets the data_ids of this Execute.


        :return: The data_ids of this Execute.
        :rtype: List[str]
        """
        return self._data_ids

    @data_ids.setter
    def data_ids(self, data_ids: List[str]):
        """Sets the data_ids of this Execute.


        :param data_ids: The data_ids of this Execute.
        :type data_ids: List[str]
        """

        self._data_ids = data_ids

    @property
    def user_id(self) -> str:
        """Gets the user_id of this Execute.


        :return: The user_id of this Execute.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        """Sets the user_id of this Execute.


        :param user_id: The user_id of this Execute.
        :type user_id: str
        """

        self._user_id = user_id

    @property
    def operation(self) -> str:
        """Gets the operation of this Execute.


        :return: The operation of this Execute.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation: str):
        """Sets the operation of this Execute.


        :param operation: The operation of this Execute.
        :type operation: str
        """

        self._operation = operation
