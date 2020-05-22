import connexion
import six

from swagger_server.models.user_uid import UserUID  # noqa: E501
from swagger_server import util


def connect_post(body):  # noqa: E501
    """Submit your unique api key and register a client

     # noqa: E501

    :param body: User unique api key
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = UserUID.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
