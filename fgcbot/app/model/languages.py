# -*- coding: utf-8 -*-


class Languages(object):
	def __init__(self):
		self.messages = [
				[u'Bienvenido! Por favor, configura tu viaje', u'Benvingut! si us plau, configuri el seu viatje', u'Welcome! please, configure your trip'],
				[u'Introduce el nuevo valor para {0}', u'Introdueix el nou valor de {0}', u'Introduce a new value for {0}'],
				[u'Estacion: {0} guardada', u'Estació: {0} guardada', u'Station: {0} saved'],
				[u'<i>Posibles estaciones:</i>\n{0}\n Trate de ser mas preciso', u'<i>Posibles estacions:</i>\n{0}\n Intenti ser més precís.', u'<i>Multiple stations:</i>\n{0}\n Try to be more accurate.'],
				[u'Estación: <i>{0}</i> desconocida.', u'Estació: <i>{0}</i> desconeguda.', u'Unknown station: <i>{0}</i>'],
				[u'Configura estación de origen y de destino', u'Has de configurar una estació d\'origen i una de destí', u'You need configure origin and destiny stations' ],
				[u'La estación de origen y destino no pueden ser la misma', u'Les estacions d\'origen i destí no poden ser les mateixes', u'Origin and destiny stations cannot be the same station'],
				[u'Las estaciones pertenecen a lineas diferentes', u'Les estacions pertanyen a lineas diferents', u'The stations belongs to differents lines'],
				[u'Idioma: {0} guardado', u'Idioma: {0} guardat', u'Language: {0} saved'],
				[u'<i>Posibles Idiomas:</i>\n{0}\n Trate de ser mas preciso', u'<i>Posibles idiomas:</i>\n{0}\n Intenti ser més precís.', u'<i>Multiple languages:</i>\n{0}\n Try to be more accurate.'],
				[u'<i>Idioma: {0} desconocido.', u'<i>Idioma: {0} desconegut.', u'Unknown language: {0}'],
				[u'Hora configurada correctamente!', u'Hora configurada correctament!', u'Time correctly setted!'],
				[u'Formato incorrecto.\nEjemplos válidos: 12,34 | 12 34 | 12', u'Format incorrecto.\nExemples vàlids: 12,34 | 12 34 | 12', u'Incorrect format.\nValid examples: 12,34 | 12 34 | 12'],
				[u'Fecha configurada correctamente!', u'Data configurada correctament!', u'Date correctly setted!'],
				[u'Formato incorrecto.\nEjemplos válidos: 21,5 | 21 5 | 21 5 2016 | 21', u'Format incorrecto.\nExemples vàlids: 21,5 | 21 5 | 21 5 2016 | 21', u'Incorrect format.\nValid examples: 21,5 | 21 5 | 21 5 2016 | 21'],
				[u'Horarios de: <b>{0}</b> hasta <b>{1}</b>', u'Horaris: <b>{0}</b> fins a <b>{1}</b>:', u'Schedule from {0} to {1}:'],
				[u'\nsalida: <b>{0}</b> llegada: <b>{1}</b>', u'\nsortida: <b>{0}</b> arribada: <b>{1}</b>', u'\nstart: <b>{0}</b> end: {1}'],
				[u'\ncon transbordo en: <b>{0}</b>', u'\namb transbord a: <b>{0}</b>', u'\nwith transfer in <b>{0}</b>']

			]

		self.buttons_text = [
				[u'Origen', u'Origen', u'Origin'],
				[u'Destino', u'Destí', u'Destiny'],
				[u'Ve!', u'Ves!', u'Go!'],
				[u'Español', u'Català', u'English'],
				[u'Hora', u'Hora', u'Time'],
				[u'Fecha', u'Data', u'Date'],
				[u'', u'', u'']
			]

