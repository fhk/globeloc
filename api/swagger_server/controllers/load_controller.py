import connexion
import six

from swagger_server.models.load import Load  # noqa: E501
from swagger_server import util


def load_get(body):  # noqa: E501
    """Load a data set

     # noqa: E501

    :param body: Get a data set by its unique id
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Load.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
