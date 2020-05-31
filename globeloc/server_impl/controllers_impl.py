"""
The server endpoint functionality
"""
import uuid

from flask import Flask, send_from_directory

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
    def __init__(self, data_id, user_id):
        self.data_id = data_id
        self.user_id = user_id

    def load(self):
        response = send_from_directory(directory='.', filename=f'{self.data_id}')
        response.headers['meta_data'] = '{"test": 213}'

        return response

class Execute_impl():
    def __init__(self):
        test = True