import connexion
import six

from swagger_server.models.load import Load  # noqa: E501
from swagger_server import util

from globeloc.server_impl.controllers_impl import Load_impl

def load_get(body):  # noqa: E501
    """Load a data set

     # noqa: E501

    :param body: Get a data set by its unique id
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Load.from_dict(connexion.request.get_json())  # noqa: E501
        Load_impl()
    return '1'
