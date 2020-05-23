import connexion
import six

from swagger_server.models.data_uid import DataUID  # noqa: E501
from swagger_server.models.execute import Execute  # noqa: E501
from swagger_server import util

from globeloc.server_impl.controllers_impl import Execute_impl


def get_order_by_id(body):  # noqa: E501
    """execute a single/multi array operation and get the result

     # noqa: E501

    :param body: Stores data and assignes a unique_id if one is not given, otherwise overwrites.
    :type body: dict | bytes

    :rtype: DataUID
    """
    if connexion.request.is_json:
        body = Execute.from_dict(connexion.request.get_json())  # noqa: E501
        Execute_impl()
    return '1'
