import p # I dati modificabili sono qui!

# KML Parser library, need to install lxml and pykml first!
import lxml
from pykml import parser
from lxml.etree import tostring

from os import path


# Variabili
tmp = ""

kml_file = open(p.name_file, 'r')

tmp = kml_file.read()

kml_file.close()

tmp_coordinates = tmp.split('  ')

lat = ["0"]
lon = ["0"]
coordinate = [lat, lon]

tmp_coord = ""
num = len(tmp_coordinates)
for i in range(num):
    tmp_coord = tmp_coordinates[i].split('-')
    coordinate.append(tmp_coord)

print(coordinate)
