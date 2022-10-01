# KML_Parser
 A simple KML parser that sends the data into a MQTT Broker
 
 This Programm receives a kml file with the latitude and longitude from a map. It's aim is to convert this KML file into a formatted string that will be sent into a MQTT broker where the server receives said data to simulate a public trasportation moving.
 
 The program is realized entirely in Python and needs the Eclipse Paho library to function. It uses a .env file to store the MQTT information that can be changed accordind to the client preferences.

The format of the message is:

<Message_Alive>
----<DeviceCode> GTV200:0500 </DeviceCode>
----<DeviceUid> CE9999_22_6805_1_2 </DeviceUid>
----<DeviceEthMAC> 74:90:50:5f:d8:a4 </DeviceEthMAC>
----<RecordedAtTime> 2022-05-20T16:14:00+02:00 </RecordedAtTime>
----<VehicleCode> 2 </VehicleCode>
----<Latitude> 40.8526649298566 </Latitude>
----<Longitude> 14.2690492527928 </Longitude>
----<Altitude> 238 </Altitude>
----<GpsSatellitesNumber> 5 </GpsSatellitesNumber>
----<GpsSignalQuality> 1 </GpsSignalQuality>
</Message_Alive>
