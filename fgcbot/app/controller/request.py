import requests

class Request (object):
	def __init__(self):
		self.fgc_base_url = "https://www.fgc.cat/cercador/cerca.asp?"

	def get_url(self, line, origin, destiny, time, date):
		day, month, year = date.split('/')
		hour, minute = time.split(':')
		url =   self.fgc_base_url
		url +=  "liniasel=" + str(line)
		url +=  "&estacio_origen=" + origin
		url +=  "&estacio_desti=" + destiny
		url +=  "&tipus=S&"
		url +=  "dia=" + day
		url +=  "%2F" + month
		url +=  "%2F" + year
		url +=  "&horas=" + hour
		url +=  "&minutos=" + minute

		return url

	def send_data(self, url):
		response = requests.post(url)
		return response.json()[0][0]