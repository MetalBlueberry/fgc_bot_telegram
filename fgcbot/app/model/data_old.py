# -*- coding: utf-8 -*-
import json
import os

class Data_Old (object):
	def __init__(self):

		self.stations = {
			#S1
			u'NA':[[u"Nacions Unides, Terrassa",u'nacions',u'unides',u'nac'],1],
			u'EN':[[u"Estacio del Nord, Terrassa",u'estacionord',u'nord',u'nor'],1],
			u'VP':[[u"Vallparadís Universitat, Terrassa",u'vallparadís',u'vallparadis',u'val'],1],
			u'TR':[[u"Terrassa Rambla",u'terrassa',u'ter'],1],
			u'FN':[[u"Les Fonts",u"fonts",u"fon"],1],
			u'RB':[[u"Rubí",u'rubí',u'rubi',u'rub'],1],
			u'HG':[[u"Hospital General",u"hospital",u"general",u"hos"],1],
			u'MS':[[u"Mira-sol",u"mira",u"sol",u"mirasol",u"mir"],1],
			#S2
			u'RA':[[u"Sabadell Rambla",u'sabadell',u'ram','sab'],1],
			u'SB':[[u"Sabadell Estació",u'sabadellestació',u'sabadellestacio',u'estacio',u'est'],1],
			u'SQ':[[u"Sant Quirze",u"santquirze",u"quirze",u"qui"],1],
			u'UN':[[u"UAB Bellatera",u'universistat',u'uni',u'uab'],1],
			u'BT':[[u"Bellaterra",u"bellaterra",u"bella",u"bel"],1],
			u'SJ':[[u"Sant Joan",u'santjoan',u'joan',u'joa'],1],
			u'VO':[[u"Volpelleres",u"volpelleres",u"vol"],1],
			#L6
			u'RE':[[u"Reina Elisenda",u"reinaelisenda",u"reina",u"elisenda",u"rei"],1],
			#L7
			u'TB':[[u"Av. Tibidabo",u"avtibidabo",u"tibidabo",u"tib"],1],
			u'EP':[[u"El Putxet",u"putxet",u"put"],1],
			u'PD':[[u'Pàdua',u"pàdua",u"padua",u"pad"],1],
			u'PM':[[u'Plaça Molina',u"molina",u"mol"],1],
			#COMU
			u'SC':[[u"Sant Cugat",u'santcugat',u'cugat',u'cug'],1],
			u'VD':[[u"Valldoreix",u"valldoreix",u"vall"],1],
			u'LF':[[u"La Floresta",u"floresta",u"flo"],1],
			u'LP':[[u"Les Planes",u"planes","pla"],1],
			u'VL':[[u"Baixador de Vallvidrera",u"baixador",u"vallvidrera",u"bai"],1],
			u'PF':[[u"Peu del Funicular",u"peu",u"funicular",u"fun"],1],
			u'SR':[[u"Sarrià","sarria",u"sarrià",u"sar"],1],
			u'TT':[[u"Les Tres Torres",u"tres",u"torres",u"tre"],1],
			u'BN':[[u"La Bonanova",u"bonanova",u"bon"],1],
			u'MN':[[u"Muntaner",u"muntaner",u"mun"],1],
			u'SG':[[u"Sant Gervasi",u"santgervasi",u"gervasi",u"ger"],1],
			u'GR':[[u"Gràcia, BCN",u'gracia',u'gra'],1],
			u'PR':[[u"Provença, BCN", u'provença',u'provenca',u'pro'],1],
			u'PC':[[u"Plaça Catalunya, BCN", u'plaça',u'bcn',u'placa',u'catalunya',u'cat'],1],

			
			u'PE':[[u"Plaça Espanya, BCN", u'plaza españa',u'placa espanya'],2],
			u'MG':[[u"Magòria La Campana"],2],
			u'IC':[[u"Ildefons Cerdà"],2],
			u'EU':[[u"Europa | Fira", u"europa fira"],2],
			u'GO':[[u"Gornal"],2],
			u'SP':[[u"Sant Josep"],2],
			u'LH':[[u"L'Hospitalet Av. Carrilet Cerdà", u"avinguda"],2],
			u'AL':[[u"Almeda"],2],
			u'CO':[[u"Cornellà Riera"],2],
			u'BO':[[u"Sant Boi"],2],
			u'ML':[[u"Molí Nou Ciutat Cooperativa"],2],
			u'CG':[[u"Colònia Güell"],2],
			u'CL':[[u"Santa Coloma de Cervelló"],2],
			u'VH':[[u"Sant Vicenç dels Horts"],2],
			u'CR':[[u"Can Ros"],2],
			u'QC':[[u"Quatre Camins"],2],
			u'PA':[[u"pallejà"],2],
			u'SA':[[u"Sant Andreu de la Barca"],2],
			u'PL':[[u"El Palau"],2],
			u'MV':[[u"Martorell Vila | Castellbisbal", u"Martorell Vila Castellbisbal"],2],
			u'MC':[[u"Martorell Central"],2],
			u'ME':[[u"Martorelll Enllaç"],2],
			u'SE':[[u"Sant Esteve Sesrovires"],2],
			u'BE':[[u"La Beguda"],2],
			u'CP':[[u"Can Parellada"],2],
			u'MQ':[[u"Masquefa"],2],
			u'PI':[[u"Piera"],2],
			u'VA':[[u"Vallbona d'Anoia"],2],
			u'CA':[[u"Capellades"],2],
			u'PO':[[u"La Pobla de Claramunt"],2],
			u'VN':[[u"Vilanova del Camí"],2],
			u'IG':[[u"Igualada"],2],
			u'AB':[[u"Abrera"],2],
			u'OL':[[u"Olesa de Montserrat"],2],
			u'AE':[[u"Aeri de Montserrat"],2],
			u'MO':[[u"Monistrol de Montserrat"],2],
			u'CB':[[u"Castellbell i el Vilar"],2],
			u'SV':[[u"Sant Vicenç | Castellgalí", u"Sant Vicenç Castellgalí"],2],
			u'VI':[[u"Manresa Viladordis"],2],
			u'MA':[[u"Manresa Alta"],2],
			u'MB':[[u"Manresa Baixador"],2],

		}
		self.lines = {
			u'1': [u'Barcelona - Vallès', ['NA', 'EN', 'VP', 'TR', 'FN', 'RB', 'HG', 'MS', 'RA', 'SB', 'SQ', 'UN', 'BT', 'SJ', 'VO', 'RE', 'TB', 'EP', 'PD', 'PM', 'SC', 'VD', 'LF', 'LP', 'VL', 'PF', 'SR', 'TT', 'BN', 'MN', 'SG', 'GR', 'PR', 'PC']]
		}


class Data (object):
	def __init__(self):
		dirname = os.path.dirname
		station_path = os.path.join(dirname(dirname(dirname(__file__))), 'data', 'stations.json')
		lang_path = os.path.join(dirname(dirname(dirname(__file__))), 'data', 'languages.json')

		station_file = file(station_path, 'r')
		lang_file = file(lang_path, 'r')

		self.data = json.loads(station_file.read())
		self.data.update(json.loads(lang_file.read()))

		'''
		#print "========"
		#print os.path.dirname(os.path.dirname(os.getcwd()))+"\\data\\stations.json"
		#print "D:\A L E I X\Documents\\fgc_bot\\fgcbot\data"
		#print os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),"data","stations.json")
		#print "========"
		#input_file  = file(os.path.dirname(os.getcwd())+"\\data\\stations.json", "r")
		input_file  = file(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),"data","stations.json"), "r")
		lang_file  = file(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),"data","languages.json"), "r")
		##input_file  = file(os.path.join(os.getcwd(), "fgcbot", "data","stations.json"), "r")
		#output_file = codecs.open("output_file.json", "w", encoding="utf-8")
		self.data = json.loads(input_file.read())#.decode("utf-8-sig"))
		self.data.update(json.loads(lang_file.read()))

		#print self.data
		'''
def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value)
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input		

if __name__ == '__main__':
	print __file__
	print os.path.join(os.path.dirname(__file__),"..")
	print os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

	dirname = os.path.dirname
	print os.path.join(dirname(dirname(dirname(__file__))), 'data', 'stations.json')
	#path = os.path.join(dirname(dirname(__file__)), os.path.join('templates', 'blog1/page.html')
	a = Data_Old()
	#print a.data
	#print a.data['stations'].keys()
	#print a.data['stations']['RA']
	#for i in a.data['stations']
	with open('stations.json', 'w') as outfile:
		json.dump(byteify({"stations":a.stations}), outfile,ensure_ascii=False,indent=4, sort_keys=True,)