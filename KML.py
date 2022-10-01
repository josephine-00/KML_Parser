import p # I dati modificabili sono qui!

# KML Parser library, need to install lxml and pykml first!
import lxml
from pykml import parser
from lxml.etree import tostring

from os import path

# Funzione per cercare substring dentro string
def found(str, search):
    found = False
    ans = str.find(search)
    if ans != -1:
        found = True
    return found

# Variabili
kml_file = p.name_file

with open(kml_file) as f:
    doc = parser.parse(f)

inner_html = tostring(doc) # Questo é tutto il kml in string
# print(inner_html)
kml_string = inner_html.decode('UTF-8')
a = type(kml_string)
print(a)

i = 0
while i != 0:
    kml_string.pop(-1)
    i = kml_string[-1]

s = "c"
coor_str = "<"
while s != "t":
    coor_str.append(kml_string[-1])
coor_str.append(">")

# Matrice di coordinate: latitudine, longitudine e altitudine
lat = ["0"]
lon = ["0"]
alt = ["0"]
coordinates = [lat, lon, alt]

stop_chr = "<"
# while stop_chr != ">":

print(kml_string)