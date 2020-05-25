import connexion
import six

from swagger_server.models.data_uid import DataUID  # noqa: E501
from swagger_server import util

from globeloc.server_impl.controllers_impl import Save_impl


def save_get(body):  # noqa: E501
    """Save a data set, by unique_id or get a new one

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param files: 
    :type files: strstr
    :param user_id: 
    :type user_id: str
    :param uuid: 
    :type uuid: str
    
    :rtype: None
    """
    if connexion.request.is_json:
        body = DataUID.from_dict(connexion.request.get_json())  # noqa: E501
        Save_impl(body)
    return '1'
