import connexion
import six

from swagger_server.models.load import Load  # noqa: E501
from swagger_server import util

from globeloc.server_impl.controllers_impl import Load_impl

def load_get():  # noqa: E501
    """Load a data set

     # noqa: E501


    :rtype: None
    """
    if connexion.request.is_json:
        data = connexion.request.json
        load = Load_impl(data["data_id"], data["user_id"])
        return load.load()