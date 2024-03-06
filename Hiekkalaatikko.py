import mysql.connector


def tarkista_lentokentta_laheisyys(yhteys, lat, lon):
    cursor = yhteys.cursor()
    cursor.execute("SELECT nimi, latitude, longitude FROM lentokentat")

    for lentokentta in cursor.fetchall():
        kentan_nimi, kentan_lat, kentan_lon = lentokentta
        etaisyys = haversine(lat, lon, kentan_lat, kentan_lon)

        if etaisyys <= 0.1:  # 100 metriä = 0.1 kilometriä
            print(f"Löytyi lentokenttä {kentan_nimi} {etaisyys * 1000} metrin päässä.")
            return True

    print("Ei löytynyt lentokenttää 100 metrin säteellä.")
    return False


# Yhteys tietokantaan
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='xxx',  # Oikea salasana tähän
    autocommit=True
)

# Esimerkki funktion käytöstä
tarkista_lentokentta_laheisyys(yhteys, 60.317222, 24.963333)  # Helsinki-Vantaan koordinaatit
