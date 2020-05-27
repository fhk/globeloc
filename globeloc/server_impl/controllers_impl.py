"""
The server endpoint functionality
"""
import uuid

class Connect_impl():
    def __init__(self, body):
        user_id  = body["user_id"]


class Save_impl():
    def __init__(self, upload_array, user_id, uuid):
        self.upload_array = upload_array
        self.user_id = user_id
        self.uuid = uuid

    def save(self):
        unique_id = uuid.uuid1()
        with open(f"{unique_id}.npz", "wb") as array:
            self.upload_array.save(array)
            return str(unique_id)

class Load_impl():
    def __init__(self, body):
        unique_id = body["uuid"]
        with open(f"{unique_id}.npz", "rb") as data_array:
            return {"data": {f"unique_id": data_array}, "meta_data": {"test": 1}}


class Execute_impl():
    def __init__(self):
        test = True