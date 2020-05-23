import connexion
import six

from swagger_server.models.execute import Execute  # noqa: E501
from swagger_server import util

from globeloc.server_impl.controllers_impl import Execute_impl


def get_item_post(body):  # noqa: E501
    """Get a subset of a data set &#x27;slice&#x27; it

    The API call to get data[,] # noqa: E501

    :param body: unique_id for data and slice to get fetched
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Execute.from_dict(connexion.request.get_json())  # noqa: E501
        Execute_impl()
    return '1'
