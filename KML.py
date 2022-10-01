import p # I dati modificabili sono qui!



# Funzione per cercare substring dentro string
def found(str, search):
    found = False
    ans = str.find(search)
    if ans != -1:
        found = True
    return found

# Variabili
kml_file = open(p.name_file, "r")
