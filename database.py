import mysql.connector
from mysql.connector import Error

def uusi_yhteys():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='flight_game',
            user='root',
            password='apple13'
        )
        return connection
    except Error as er:
        print(f"Virhe: {er}")
        return None

def sql_suoritus(sql, params=None):
    try:
        yhteys = uusi_yhteys()
        if yhteys is not None:
            with yhteys:
                with yhteys.cursor() as kursori:
                    kursori.execute(sql, params)
                    tulos = kursori.fetchone()
                    return tulos
    except Error as er:
        print(f"Virhe: {er}")
        return None

def maa_random():
    sql = "SELECT name, iso_country FROM country WHERE continent = %s ORDER BY RAND() LIMIT 1"
    return sql_suoritus(sql, ('EU',))

def lentoasema_random(i):
    sql = "SELECT name FROM airport WHERE iso_country = %s AND type != 'closed' ORDER BY RAND() LIMIT 1"
    return sql_suoritus(sql, (i,))[0]

def lentoasema_koordinaatit(n):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE name = %s"
    return sql_suoritus(sql, (n,))

def lentoasema_tyyppi(n):
    sql = "SELECT type FROM airport WHERE name = %s"
    return sql_suoritus(sql, (n,))[0]