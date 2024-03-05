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
    maa = "select name from country where continent = 'EU' order by name;"
    return

# funktio joka valitsee random kaupungin maasta ja palauttaa sen returnilla
def kaupunki_random():
    kaupunki = "select municipality from airport;"
    return

# funktio joka valitsee random lentoaseman kaupungista, huom! jos lentoasema on yli 5
def lentoasema_random():

# funktio joka hakee lentoaseman koordinaatit, muuttaa niitä vähintään 100m erisuuntiin ja palauttaa ne returnilla (gps muodossa)
def lentoasema_koordinaatit():
    lentoasema_koordinaatti = "SELECT latitude_deg, longitude_deg FROM airport LIMIT 1;"
    return

# funktio joka palauttaa kohteen tyypin (lentoasema tai heliport)
def lentoasema_tyyppi():
    lento_tai_heli = "SELECT type FROM airport;"
# funktio joka palauttaa lentoaseman koon, jos kyseessä on heliport, eli kokoa ei ole niin palautetaan False.
def lentoasema_koko():