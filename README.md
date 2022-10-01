# KML_Parser
 A simple KML parser that sends the data into a MQTT Broker
 
 This Programm receives a kml file with the latitude and longitude from a map. It's aim is to convert this KML file into a formatted string that will be sent into a MQTT broker where the server receives said data to simulate a public trasportation moving.
 
 The program is realized entirely in Python and needs the Eclipse Paho library to function. It uses a .env file to store the MQTT information that can be changed accordind to the client preferences.
