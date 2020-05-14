#!/usr/bin/env python
"""Create the globeloc API and helpers
"""

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
        self.data_sets = []
        self.data_arrays = []

    def __get_item__(self, item):
        """
        Top level key/attribute filtering
        """
        self.data_arrays = [DataArray(self, sub_item) for sub_item in item]
        return self.data_arrays

    def connect(self, api_key):
        """
        In the future this should do some kind of authentication
        """
        self.api_key = api_key

    def load(self, unique_id=None):
        """
        specify which data set we want to use
        if unique_id is None return all the ids and meta data for that user
        """
        self.data_sets.append(unique_id)

    def save(self, my_array):
        """
        Push the data to the backend store and return a unique id
        """
        return "unique_id"

    def parse(self, filename, column=None, metadata=None):
        """
        Convert the GIS file into the globeloc array format
        """
        n_rows = 180 * num_deci_places
        n_cols = 360 * num_deci_places
        f_df = gpd.read_file(filename)

        if column is not None:
            # assuming we always have less data than then number of cells
            for thing in set(f_df['column']):
                da = DataArray(
                        self,
                        thing,
                        metadata
                da.init_array = sparse.lil_matrix((n_rows, n_cols), dtype=np.uint8))
                data_arrays.append(da)

        else:
            pass


class DataArray:
    """
    A specific data set
    """
    def __init__(self, globeloc, sub_item, metadata):
        self.metadata = metadata
        self.globeloc = globeloc
        self.sub_item = sub_item

    def __get_item__(self, item):
        """
        This compute will be done remote in the future
        """
        pass

    def init_array(array):
        self.array = array

