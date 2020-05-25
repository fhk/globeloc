#!/usr/bin/env python
"""Create the globeloc API and helpers
"""

import uuid
import requests
import json
import tempfile

import numpy as np
import geopandas as gpd
from scipy import sparse


__author__ = "Fabion Kauker"
__copyright__ = "Copyright 2020, globeloc"
__credits__ = []
__license__ = "Super Secret Squirrel"
__version__ = "0.0.1"
__maintainer__ = ""
__email__ = "support@globeloc.com"
__status__ = "Protype"


NUM_DECI_PLACES = 10000


class GlobeLoc:
    """
    The object where everything happens
    """
    def __init__(self):
        self.api_key = None
        self.data_sets = {}
        self.data_arrays = []
        self.attribute_to_array = {}

    def __getitem__(self, item):
        """
        Top level key/attribute filtering
        """
        if type(item) == str:
            return self.data_arrays[self.data_sets[self.attribute_to_array[item]]]


    def connect(self, api_key=None, url=None):
        """
        In the future this should do some kind of authentication
        """
        self.url = url
        self.api_key = api_key

    def load(self, unique_id=None):
        """
        specify which data set we want to use
        if unique_id is None return all the ids and meta data for that user
        """
        if self.url == 'local':
            data = sparse.load_npz(f"./data/{unique_id}.npz")
            da = DataArray(
                self
            )
            da.init_array(data)
            self.data_sets[unique_id] = len(self.data_sets)
            self.data_arrays.append(da)

        else:
            response = requests.get(f"{self.url}/v1/load", data={"uuid": unique_id})
            da = DataArray(
                self
            )
            tmp = tempfile.TemporaryDirectory()
            with open(f'{tmp.name}/{unique_id}.npz', 'wb') as load_array:
                load_array.write(response['files']['saved_array'])
            data = sparse.load_npz(f"{tmp.name}/{unique_id}.npz")
            da.init_array(data)
            self.data_sets[unique_id] = len(self.data_sets)
            self.data_arrays.append(da)

    def save(self, my_array):
        """
        Push the data to the backend store and return a unique id
        """
        unique_id = uuid.uuid1()
        if self.url == 'local':
            sparse.save_npz(f'./data/{my_array}.npz', self.data_arrays[self.data_sets[my_array]].array.tocsr())
            return str(unique_id)
        else:
            tmp = tempfile.TemporaryDirectory()
            sparse.save_npz(f'{tmp.name}/{my_array}.npz', self.data_arrays[self.data_sets[my_array]].array.tocsr())
            with open(f'{tmp.name}/{my_array}.npz', 'rb') as send_array:
                files = {
                    'upload_array': send_array,
                    "uuid": str(unique_id),
                    "data": f'{my_array}.npz',
                    "user_id": 'test'}

                session = requests.Session()
                response = session.post(
                    f"{self.url}/v1/save",
                    files=files)

                return response

    def parse(self, filename, column=None, sub_category=None, metadata=None):
        """
        Convert the GIS file into the globeloc array format
        """
        n_rows = 180 * NUM_DECI_PLACES
        n_cols = 360 * NUM_DECI_PLACES
        f_df = gpd.read_file(filename)
        if f_df.crs != 'EPSG:4326':
            f_df.to_crs('EPSG:4326')
        coords = f_df.geometry
        f_df['x'] = coords.apply(lambda p: p.x) # Lon
        f_df['y'] = coords.apply(lambda p: p.y) # Lat
        f_df['t_x'] = f_df['x'].apply(lambda p: round((p + 180) * NUM_DECI_PLACES), 0)
        f_df['t_y'] = f_df['y'].apply(lambda p: round((p + 90) * NUM_DECI_PLACES), 0)

        # Assuming all data is points and that they should be counted in each cell
        # This will need to be enhance to support geometries and different data stores
        if column is not None:
            # assuming we always have less data than then number of cells
            for thing in set(f_df[column]):
                if filter is not None:
                    if thing != sub_category:
                        continue
                da = DataArray(
                        self,
                        thing,
                        metadata)
                da.init_array(sparse.lil_matrix((n_rows, n_cols), dtype=np.uint8))

                for ix, row in f_df[f_df[column] == thing].iterrows():
                    # TODO: can this be done directly to the da object?
                    da.array[row.t_x, row.t_y] += 1

        else:
            da = DataArray(
                    self,
                    "all",
                    metadata)
            da.init_array(sparse.lil_matrix((n_rows, n_cols), dtype=np.uint8))

            for ix, row in f_df.iterrows():
                # TODO: can this be done directly to the da object?
                da.array[row.t_x, row.t_y] += 1


        self.data_arrays.append(da) # sore this index in the future and add it to data_sets
        unique_id = str(uuid.uuid1())
        if sub_category is None:
            self.attribute_to_array[len(self.data_sets)] = unique_id
        else:
            self.attribute_to_array[sub_category] = unique_id
        self.data_sets[unique_id] = len(self.data_sets) 

        return unique_id


class DataArray:
    """
    A specific data set
    """
    def __init__(self, globeloc, sub_item=None, metadata=None):
        self.metadata = metadata
        self.globeloc = globeloc
        self.sub_item = sub_item

    def __getitem__(self, item):
        """
        This compute will be done remote in the future
        """
        return self.array[item]

    def init_array(self, array):
        self.array = array

