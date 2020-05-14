#!/usr/bin/env python
"""Create the globeloc API and helpers
"""



__author__ = "Fabion Kauker"
__copyright__ = "Copyright 2020, globeloc"
__credits__ = []
__license__ = "Super Secret Squirrel"
__version__ = "0.0.1"
__maintainer__ = ""
__email__ = "support@globeloc.com"
__status__ = "Protype"



class GlobeLoc:
	def __init__(self):
		api_key = None
		data_sets = []
		data_arrays = []

	def __get_item__(self, item):
		return [DataArray(self, sub_item) for sub_item in item]

	def connect(self, api_key):
		pass

	def load(self, unique_id):
		pass

	def save(self, my_array):
		return "unique_id"

	def parse(self, filename):
		pass


class DataArray:
	def __init__(self, globeloc, sub_item):
		pass

	def __get_item__(self, item):
		pass

