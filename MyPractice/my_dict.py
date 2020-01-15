# -*- coding: utf-8 -*-


cities = {'ts': 'tianshui', 'ny': 'newyork', 'bj': 'beijing', 'wd': 'washdon', 'ckg': 'chikago'}


def find_city(themap, city):
    print('start search...')
    if city in themap:
        return themap[city]
    else:
        return 'Not found'


cities['_find'] = find_city

while True:
    city = input('please a str to key of city name：')
    if not city:
        break

    city_found = cities['_find'](cities, city)

    print(city_found)
    print('end search')

