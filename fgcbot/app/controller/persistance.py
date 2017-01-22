# -*- coding: utf-8 -*-
import re

from .request import Request
from ..model.data import Data
from datetime import datetime

class Persistance (object):
	def __init__(self):
		self.persistance = Data()
		self.request = Request()

	def get_station_candidates(self, name):
		candidates = []
		name_ascii = re.sub(r'[^\x00-\x7F]+','~', name).lower()
		#print name_ascii
		for i in self.persistance.data['stations'].keys():
			#print i
			stations = self.persistance.data['stations'][i][0]
			stations_string = '*'.join(stations)
			#print stations
			if name_ascii in  re.sub(r'[^\x00-\x7F]+','~', stations_string).lower():
				candidates.append([i, stations[0]])

		return candidates

	def get_language_candidates(self, name):
		candidates = []
		name_ascii = re.sub(r'[^\x00-\x7F]+','~', name).lower()
		#print name_ascii
		for lang in self.persistance.data['languages']:
			if name_ascii in re.sub(r'[^\x00-\x7F]+','~', lang).lower():
				candidates.append([self.persistance.data['languages'].index(lang), lang])
		return candidates

	def is_same_line(self, origin_id, destiny_id):
		return self.persistance.data['stations'][origin_id][1] == self.persistance.data['stations'][destiny_id][1]

	def calculate_trip(self, origin_id, destiny_id, time = None, date = None):
		if not time:
			time = datetime.now().strftime('%H:%M')
		if not date:
			date = datetime.now().strftime('%d/%m/%Y')

		url = self.request.get_url(self.persistance.data['stations'][origin_id][1], origin_id, destiny_id, time, date)
		response = self.request.send_data(url)
		filtered_response = []
		try:
			for train in response:
				filtered_train = {}
				if (len(train)==1): #no transfer
					filtered_train['origin'] = {'time':train[0]['sortida'], 'line': train[0]['linia']}
					filtered_train['destiny'] = {'time': train[0]['arribada'][-8:-3], 'line': train[0]['linia'] }
					filtered_train['transfer'] = []
				
				elif len(train) == 2:
					if not origin_id in train[0]['estacions']:
						continue
					if not destiny_id in train[1]['estacions']:
						continue
					filtered_train['origin'] = {'time':train[0]['sortida'], 'line': train[0]['linia']}
					filtered_train['destiny'] = {'time': train[1]['arribada'][-8:-3], 'line': train[1]['linia'] }
					filtered_train['transfer'] = [train[0]['estacions'][-1]]
					filtered_train['transfer'] = [self.persistance.data['stations'][train[0]['estacions'][-1]][0][0]]
				else:
					print "error parsing the response"

				filtered_response.append(filtered_train)
			for i in filtered_response:
				print i
		except Exception as e:
			print e

		good_results = []
		if time.startswith(("00:","01:","02:","03:")):
			custom_time = "02/01/1900 " + time	
		else:
			custom_time = "01/01/1900 " + time
		for item in filtered_response:
			if (len(item['origin']['time'])>12):
				if item['origin']['time'][12] == ":":
					item['origin']['time'] = item['origin']['time'][:11] + "0" + item['origin']['time'][11:]

				if item['origin']['time'] >= custom_time:
					good_results.append(item)

		sorted_response = sorted(good_results, key=lambda k: k['origin']['time'][-8:-3]) 
		for i in range(len(sorted_response)):
			sorted_response[i]['origin']['time'] = sorted_response[i]['origin']['time'][-8:-3]
		
		return sorted_response
