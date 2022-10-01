// This is the original KML file in C++ without the connection to MQTT


// KMLParser.cpp : This file contains the 'main' function. Program execution begins and ends there.
// Josephine Esposito | 23/05/2022



// Librerie
#include <iostream>

#include <vector>
#include <fstream>  // per leggere il file
#include <string>   // getline()
// #include "MQTTClient.h"

using namespace std;

// Time complexity: O(n)
// Riceve la string e la sua substring da cercare
// Ritorna un True o False a seconda di se l'ha trovata o meno
bool found(string str, string search) {
    bool found = false;
    int ans = str.find(search);
    if (ans != string::npos) {
        found = true;
    }
    return found;
}

int main()
{
    // Variabili
    fstream file("A90E80.kml", fstream::in);
    string str;
    vector <string> coordinates;

    bool running = true;
    int count = 0;


    // apriamo il file KML e lo leggiamo riga per riga fino all'invio
    // dopo controlliamo se arriva tutto su una linea o separatamente
    while (getline(file, str, '\n')) {
        
        // Controllare in quale formato arriva la String (tutto su una linea o separate)
        string temp = "";
        string chars = "\t";    // carattere speciale a rimuovere
        
        if (found(str, chars)) {     // Rimuovo i caratteri speciali
            for (char c : chars) {
                str.erase(remove(str.begin(), str.end(), c), str.end());
            }
        }
        

        if (found(str, "<coordinates>")) {
            count++;
        }

        if (count > 0 && str != "</coordinates>") {
            chars = "<coordinates>";
            temp = "</coordinates>";

            for (char c : chars) {
                str.erase(remove(str.begin(), str.end(), c), str.end());    // stiamo eliminando le lettere dalla riga
            }
            string temp2 = str; // non modifichiamo la string originale per poter controllare quando finisce dopo (rimane solo il carattere /)
            for (char c : temp) {
                temp2.erase(remove(temp2.begin(), temp2.end(), c), temp2.end());
            }

            coordinates.push_back(temp2);
        }

        if (count > 0 && found(str, "/")) { // Dopo aver rimosso le lettere dai numeri controlliamo se é rimasto il carattere / per poter uscire
            count -= 1;
        }
    }
    file.close();
    /////////////////////////////////////////////////////////////////////////////
    

    // Prende solo l'ultimo elemento che contiene l'insieme dei punti
    string coords = coordinates.at(coordinates.size() - 1);

    string delimiter = ",0";
    vector<string> sets;
    size_t pos = 0;

    // Dividiamo ciascuna coppia di coordinate e le mettiamo in un vettore
    while ((pos = coords.find(delimiter)) != string::npos) {
        sets.push_back(coords.substr(0, pos - 1));
        coords.erase(0, pos + delimiter.length());
    }
    /////////////////////////////////////////////////////////////////////////////
    

    delimiter = ",";
    // Due vettori per salvarmi latitudine e longitudine dei singoli punti
    vector<string> lat;
    vector<string> lon;

    // Con un for loop dividiamo latitudine e longitudine in due vettori
    for (int i = 0; i < sets.size(); i++) {
        while ((pos = sets.at(i).find(delimiter)) != string::npos) {
            lat.push_back(sets.at(i).substr(0, pos - 1));
            sets.at(i).erase(0, pos + delimiter.length());
        }
        lon.push_back(sets.at(i));
    }
    /////////////////////////////////////////////////////////////////////////////


    // salva in un documento
    ofstream coordinateFile("Coordinate.txt", ofstream::out);

    if (coordinateFile.is_open()) {
        for (int i = 0; i < lat.size(); i++) {
            coordinateFile << lat.at(i) << "\t" << lon.at(i) << "\n";
        }
        coordinateFile.close();
    }
    else cout << "[Error 0] Problem with opening file";
    /////////////////////////////////////////////////////////////////////////////

    // invia a MQTT





    cout << "Fine programma!!";
}
