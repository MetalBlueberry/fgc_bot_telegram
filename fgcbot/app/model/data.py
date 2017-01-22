# -*- coding: utf-8 -*-

import json, os


class Data (object):
	def __init__(self):
		dirname = os.path.dirname
		station_path = os.path.join(dirname(dirname(dirname(__file__))), 'data', 'stations.json')
		lang_path = os.path.join(dirname(dirname(dirname(__file__))), 'data', 'languages.json')

		station_file = file(station_path, 'r')
		lang_file = file(lang_path, 'r')

		self.data = json.loads(station_file.read())
		self.data.update(json.loads(lang_file.read()))
