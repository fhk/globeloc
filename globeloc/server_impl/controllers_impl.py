"""
The server endpoint functionality
"""

class Connect_impl():
    def __init__(self, body):
        user_id  = body["user_id"]


class Save_impl():
    def __init__(self, body):
        unique_id = body["uuid"]
        with open(f"{unique_id}.npz", "w") as data_array:
            data_array.write(body["data"])
        return 1


class Load_impl():
    def __init__(self, body):
        unique_id = body["uuid"]
        with open(f"{unique_id}.npz", "rb") as data_array:
            return {"data": {f"unique_id": data_array}, "meta_data": {"test": 1}}


class Execute_impl():
    def __init__(self):
        test = True