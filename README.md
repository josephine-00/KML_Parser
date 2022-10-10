# KML_Parser
 A simple KML parser that sends the data into a MQTT Broker

---

This Programm receives a kml file with the latitude and longitude from a map. It's aim is to convert this KML file into a formatted string that will be sent into a MQTT broker where the server receives said data to simulate a public trasportation moving.

The program is realized entirely in Python and needs the Eclipse Paho library to function. It uses p.py file to store the MQTT information that can be changed accordind to the client preferences.

---

## mosquitto
To run mosquitto, paste this command into the folder where you installed mosquitto. This works only on Windows PowerShell

```
.\mosquitto.exe -v
```

To run the python program you can use this command instead. It will work only on Windows PowerShell

```
python mqtt_connection.py -v
```
