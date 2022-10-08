# Script created by Josephine Esposito | 01/10/2022
# The repository can be found on 

from argparse import Namespace
import p # I dati modificabili sono qui!

# KML Parser library, need to install lxml and pykml first! more info on the github
import lxml
from pykml import parser
from pykml.factory import nsmap
from lxml.etree import tostring
from os import path

Namespace = {'ns': nsmap[None]}


# =======================================================================================================================================================================
# kml coordinates format: long - lat - alt
# =======================================================================================================================================================================



def kml_parser():
    # Con pykml ci stiamo salvando solo il contenuto dell'ultimo contenitore </coordinates> che contiene tutte le coordinate del viaggio
    with open(p.name_file) as f:
        root = parser.parse(f).getroot()
        pms = root.xpath(".//ns:Placemark[.//ns:LineString]", namespaces = Namespace)

        for pm in pms:
            # tmp = pm.LineString.coordinates
            for ls in pm.xpath(".//ns:coordinates", namespaces = Namespace):
                tmp = (ls.text.strip().replace('  ', ''))

    # print(tmp)
    # Adesso andiamo a separare ciascun gruppo di coordinate (long, lat e alt) in un array
    temp_coordinate = [""]
    temp_coordinate = tmp.split(" ")   # ciascun gruppo di coordinate viene separato da due spazi bianchi
    # careful up above, the spaces between the coords are not two but one, if you input a non existent char[] it will return the whole str
    ### print(temp_coordinate[-1])

    # =======================================================================================================================================================================

    # Ora dobbiamo separare ciascun gruppo di coordinate in lon, lat e alt e unire questi array in coordinate

    lon = [""]
    lat = [""]
    alt = [""]

    temp_lla = [""]

    for i in range(len(temp_coordinate)):
        temp_lla = temp_coordinate[i].rsplit(',')
        lon.append(temp_lla[0])
        lat.append(temp_lla[1])
        alt.append(temp_lla[2])
        temp_lla.clear()


    # We will need to pop the first element of each list before merging them into coordinate

    lon.pop(0)
    lat.pop(0)
    alt.pop(0)
    coordinate = [lon, lat, alt]
    ###print(coordinate[0][0])

    # =======================================================================================================================================================================

    # Formattiamo i messaggi da inviare
    ''' Formato 
    1 <SET>
    2    <Message_Alive>
    3        <DeviceCode>GTV200:0500</DeviceCode>
    4        <DeviceUid>CE9999_22_6805_1_2</DeviceUid>
    5        <DeviceEthMAC>74:90:50:5f:d8:a4</DeviceEthMAC>
    6        <RecordedAtTime>2022-05-20T16:14:00+02:00</RecordedAtTime>
    7        <VehicleCode>2</VehicleCode>
    8        <Latitude>40.8526649298566</Latitude>
    9        <Longitude>14.2690492527928</Longitude>
    10        <Altitude>238</Altitude>
    11        <GpsSatellitesNumber>5</GpsSatellitesNumber>
    12        <GpsSignalQuality>1</GpsSignalQuality>
    13    </Message_Alive>
    14 </SET>
    '''
    line_1 = "<SET>\n"
    line_2 = "\t<Message_Alive>\n"
    line_3 = "\t\t<DeviceCode>GTV200:0500</DeviceCode>\n"
    line_4 = "\t\t<DeviceUid>CE9999_22_6805_1_2</DeviceUid>\n"
    line_5 = "\t\t<DeviceEthMAC>74:90:50:5f:d8:a4</DeviceEthMAC>\n"
    line_6 = "\t\t<RecordedAtTime>2022-05-20T16:14:00+02:00</RecordedAtTime>\n"
    line_7 = "\t\t<VehicleCode>2</VehicleCode>\n"

    line_11 = "\t\t<GpsSatellitesNumber>5</GpsSatellitesNumber>\n"
    line_12 = "\t\t<GpsSignalQuality>1</GpsSignalQuality>\n"
    line_13 = "\t</Message_Alive>\n"
    line_14 = "</SET>"

    # Variabile che contiene il payload per il messaggio MQTT
    kml_msg = [""]
    line_begin = line_1 + line_2 + line_3 + line_4 + line_5 + line_6 + line_7
    line_end = line_11 + line_12 + line_13 + line_14
    for i in range(len(alt)):
        line_8 = "\t\t<Latitude>" + coordinate[1][i] + "</Latitude>\n"
        line_9 = "\t\t<Longitude>" + coordinate[0][i] + "</Longitude>\n"
        line_10 = "\t\t<Altitude>" + coordinate[2][i] + "</Altitude>\n"
        line_coords = line_8 + line_9 + line_10

        final_msg = line_begin + line_coords + line_end
        kml_msg.append(final_msg)

    kml_msg.pop(0)
    # Inviamo i messaggi formattati come lista 
    ## print(kml_msg[0])
    return kml_msg