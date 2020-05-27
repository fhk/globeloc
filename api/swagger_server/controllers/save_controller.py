import connexion
import six

from swagger_server import util

from globeloc.server_impl.controllers_impl import Save_impl


def save_post(upload_array, user_id, uuid):  # noqa: E501
    """Save a data set, by unique_id or get a new one

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param upload_array: 
    :type upload_array: strstr
    :param user_id: 
    :type user_id: str
    :param uuid: 
    :type uuid: str

    :rtype: None
    """
    save = Save_impl(upload_array, user_id, uuid)

    return save.save()
