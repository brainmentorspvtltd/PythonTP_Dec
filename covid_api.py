Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import json
>>> import urllib.request as url
>>> path = "https://data.covid19india.org/states_daily.json"
>>> response = url.urlopen(path)
>>> data = json.load(response)
>>> type(data)
<class 'dict'>
>>> data.keys()
dict_keys(['states_daily'])
>>> states = data["states_daily"]
>>> len(states)
1563
>>> len(states) / 3
521.0
>>> states[200]
{'an': '0', 'ap': '2', 'ar': '0', 'as': '0', 'br': '0', 'ch': '0', 'ct': '0', 'date': '19-May-20', 'dateymd': '2020-05-19', 'dd': '0', 'dl': '6', 'dn': '0', 'ga': '0', 'gj': '25', 'hp': '1', 'hr': '0', 'jh': '0', 'jk': '2', 'ka': '3', 'kl': '0', 'la': '0', 'ld': '0', 'mh': '76', 'ml': '0', 'mn': '0', 'mp': '6', 'mz': '0', 'nl': '0', 'or': '1', 'pb': '1', 'py': '0', 'rj': '5', 'sk': '0', 'status': 'Deceased', 'tg': '4', 'tn': '3', 'tr': '0', 'tt': '146', 'un': '0', 'up': '5', 'ut': '0', 'wb': '6'}
>>> states[1200]
{'an': '59', 'ap': '6582', 'ar': '20', 'as': '639', 'br': '8690', 'ch': '625', 'ct': '12345', 'date': '18-Apr-21', 'dateymd': '2021-04-18', 'dd': '0', 'dl': '25462', 'dn': '184', 'ga': '951', 'gj': '10340', 'hp': '788', 'hr': '7177', 'jh': '3992', 'jk': '1526', 'ka': '19067', 'kl': '18257', 'la': '60', 'ld': '114', 'mh': '68631', 'ml': '71', 'mn': '72', 'mp': '12248', 'mz': '50', 'nl': '19', 'or': '3664', 'pb': '4900', 'py': '663', 'rj': '10262', 'sk': '105', 'status': 'Confirmed', 'tg': '5093', 'tn': '10723', 'tr': '69', 'tt': '275063', 'un': '0', 'up': '30566', 'ut': '2630', 'wb': '8419'}
>>> path = "https://api.openweathermap.org/data/2.5/weather?q=delhi&appid=83e01e3dce5d28839bb5a177cb51af12"
>>> res = url.urlopen(path)
>>> json.load(res)
{'coord': {'lon': 77.2167, 'lat': 28.6667}, 'weather': [{'id': 711, 'main': 'Smoke', 'description': 'smoke', 'icon': '50d'}], 'base': 'stations', 'main': {'temp': 288.2, 'feels_like': 287.41, 'temp_min': 288.2, 'temp_max': 288.2, 'pressure': 1023, 'humidity': 63}, 'visibility': 1800, 'wind': {'speed': 4.12, 'deg': 290}, 'clouds': {'all': 15}, 'dt': 1639721494, 'sys': {'type': 1, 'id': 9165, 'country': 'IN', 'sunrise': 1639705057, 'sunset': 1639742210}, 'timezone': 19800, 'id': 1273294, 'name': 'Delhi', 'cod': 200}
>>> 