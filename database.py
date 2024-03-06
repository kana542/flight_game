# funktio joka yhdistää sql-tietokantaan.
import mysql.connector
def connection():
    def hae(sql):
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        return tulos

    yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='root',
        autocommit=True
    )
# funktio joka valitse random maan joka eurossa ja palauttaa sen returnilla
def maa_random():
    maa = "SELECT name, iso_country FROM country WHERE continent = 'EU' ORDER BY RAND() LIMIT 1;"
    return

# funktio joka valitsee random kaupungin maasta ja palauttaa sen returnilla
def kaupunki_random():
    kaupunki = "SELECT municipality FROM airport ORDER BY RAND() LIMIT 1;"
    return

# funktio joka valitsee random lentoaseman kaupungista, huom! jos lentoasema on yli 5
def lentoasema_random():

# funktio joka hakee lentoaseman koordinaatit, tehdään game_logic.py[muuttaa niitä vähintään 100m erisuuntiin ja palauttaa ne returnilla (gps muodossa)]
def lentoasema_koordinaatit():
    lentoasema_koordinaatti = "SELECT latitude_deg, longitude_deg FROM airport LIMIT 1;"
    return

# funktio joka palauttaa kohteen tyypin (lentoasema tai heliport)
def lentoasema_tyyppi():
    lento_tai_heli = "SELECT type FROM airport JOIN country ON airport.iso_country = country.iso_country WHERE airport.type != 'closed' LIMIT 1;"
    return

# funktio joka palauttaa lentoaseman koon, jos kyseessä on heliport, eli kokoa ei ole niin palautetaan False.
def lentoasema_koko():
    koko =