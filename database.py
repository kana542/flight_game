import mysql.connector
from mysql.connector import Error

# yhteyden muodostaminen tietokantaan + virheenhallinta
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

# SQL execution/suoritus kaikille yhden rivin hauille + virheenhallinta
def sql_suoritus_fetchone(sql, params=None):
    try:
        yhteys = uusi_yhteys()
        if yhteys is not None:
            with yhteys:
                with yhteys.cursor() as kursori:
                    kursori.execute(sql, params)
                    tulos = kursori.fetchone()
                    return tulos
    except Error as er:
        print(f"Error while fetching (one): {er}")
        return None
    
# SQL execution/suoritus kaikille useamman rivin hauille + virheenhallinta
def sql_suoritus_fetchall(sql, params=None):
    try:
        yhteys = uusi_yhteys()
        if yhteys is not None:
            with yhteys:
                with yhteys.cursor() as kursori:
                    kursori.execute(sql, params)
                    tulokset = kursori.fetchall()
                    return tulokset
    except Error as er:
        print(f"Error while fetching (all): {er}")
        return None
# SQL execution/suoritus tallentamista varten + virheenhallinta
def sql_suoritus_insert(sql, params=None):
    try:
        yhteys = uusi_yhteys()
        if yhteys is not None:
            with yhteys.cursor() as kursori:
                kursori.execute(sql, params)
                yhteys.commit()
            yhteys.close()
    except Error as er:
        print(f"Error while inserting to the database: {er}")

# random maan hakeminen tietokannasta
def maa_random():
    sql = "SELECT name, iso_country FROM country WHERE continent = %s ORDER BY RAND() LIMIT 1"
    return sql_suoritus_fetchone(sql, ('EU',))

# random lentoaseman hakeminen halutusta maasta (parametri i) tietokannasta
def lentoasema_random(i):
    sql = "SELECT name FROM airport WHERE iso_country = %s AND type != 'closed' ORDER BY RAND() LIMIT 1"
    return sql_suoritus_fetchone(sql, (i,))[0]

# halutun (parametri n) lentoaseman/heliportin koordinaattien hakeminen tietokannasta
def lentoasema_koordinaatit(n):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE name = %s"
    return sql_suoritus_fetchone(sql, (n,))

# halutun (parametri n) lentoaseman/heliportin tyypin hakeminen tietokannasta
def lentoasema_tyyppi(n):
    sql = "SELECT type FROM airport WHERE name = %s"
    return sql_suoritus_fetchone(sql, (n,))[0]

# pelaajien nimien ja aikojen hakeminen tietokannasta
def tulosta_pelaajat():
    sql = "SELECT username, time FROM players ORDER BY time ASC LIMIT 5"
    tulokset = sql_suoritus_fetchall(sql,)
    if tulokset:
        for rivi in tulokset:
            print(f"{rivi[0]} | {rivi[1]}")
    else:
        print("No players yet in the database.")

# pelaajan nimen ja ajan tallentaminen tietokantaan
def tallenna_aika(pelaajan_nimi, kulunut_aika):
    sql = "INSERT INTO players (username, time) VALUES (%s, %s)"
    parametrit = (pelaajan_nimi, kulunut_aika)
    sql_suoritus_insert(sql, parametrit)