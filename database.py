# funktio joka yhdistää sql-tietokantaan.
def connection():

# funktio joka valitse random maan joka eurossa ja palauttaa sen returnilla
def maa_random():

# funktio joka valitsee random kaupungin maasta ja palauttaa sen returnilla
def kaupunki_random():

# funktio joka valitseee random lentoaseman kaupungista, huom! jos lentoasema on yli 5
def lentoasema_random():
    lentoasema_random_sql = "SELECT name FROM airport ORDER BY RAND() LIMIT 1;"

# funktio joka hakee lentoaseman koordinaatit, muuttaa niitä vähintään 100m erisuuntiin ja palauttaa ne returnilla (gps muodossa)
def lentoasema_koordinaatit():

# funktio joka palauttaa kohteen tyypin (lentoasema tai heliport)
def lentoasema_tyyppi():

# funktio joka palauttaa lentoaseman koon, jos kyseessä on heliport, eli kokoa ei ole niin palautetaan False.
def lentoasema_koko():
    lentoasema_koko_sql = "SELECT type FROM airport;"

    if tulos == "heliport";
        return False
    else:
        return True

