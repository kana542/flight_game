import database
import time
import os
import utils

# MUUTTUJAT
oikea_maa, oikean_maan_iso = database.maa_random() # satunnainen maa ja sen iso-koodi (rajoitettu euroopan maihin)
oikea_lentoasema = database.lentoasema_random(oikean_maan_iso) # satunnainen lentokenttä/helikopterialusta arvotusta maasta
koordinaatti_lat, koordinaatti_lon = database.lentoasema_koordinaatit(oikea_lentoasema) # lentoaseman/helikopterialustan koordinaatit
kohteen_tyyppi = database.lentoasema_tyyppi(oikea_lentoasema) # tallennetaan kohteen tyyppi (lentoasema vai heliport) muuttujaan

maa_arvattu = False

# Alkunäyttö pelaajalle missä kerrotaan pelin idea.
def step_one():

    time.sleep(2)
    os.system('cls')

    print("""
                                     Welcome to the Skyhawk game!

    Your mission is to locate a stolen helicopter from a random airport or heliport across Europe. 
         You need to use the browser map that you prefer to help you locate the helicopter. 
                               We recommend Google Maps and OurAirports.
    """)

    time.sleep(12)
    os.system("cls")


# ANNETAAN PELAAJAN ARVATA SATUNNAISESTI VALITTU MAA OPENAI TUOTTAMILLA AVAINSANOILLA
def step_two():
    global maa_arvattu
    print(f"First you need to guess the correct country where the helicopter might be.\nYour clues are following: {utils.tuota_avainsanat(oikea_maa)}")
    while True:
        maa_arvaus = input("Your answer: ")
        if maa_arvaus == oikea_maa:
            os.system("cls")
            print("Correct!")
            maa_arvattu = True
            time.sleep(2)
            break
        else:
            print("Wrong answer. Try again!")

# ANNETAAN PELAAJAN ARVATA LENTOKENTTÄ/HELIKOPTERIALUSTA KYSEISESTÄ MAASTA
def step_three():
    time.sleep(2)
    os.system("cls")

    # tulostetaan kohteen tyyppi ja muutetaan alkuperäiset koordinaatit halutulla metrimäärällä vaihtelemaan
    print(f"Type of the location: {kohteen_tyyppi}")
    print(f"The coordinates are: {utils.gps_muutos(koordinaatti_lat, koordinaatti_lon, 1000)}")

    while True:
        lentoasema_arvaus = input("Your answer: ")
        arvaus = utils.tarkista_arvaus(lentoasema_arvaus, oikea_lentoasema)
        
        if arvaus == "ok":
            os.system("cls")
            print("Correct! You found the stolen helicopter!")
            time.sleep(4)
            os.system("cls")
            time.sleep(1)
            break
        elif arvaus == "ei":
            print("Wrong answer. Try again!")
        else:
            print("error")

# TALLENNETAAN AIKA TIETOKANTAAN
def tallenna_aika(pelaajan_nimi, kulunut_aika):
    print(f"Your time was {kulunut_aika}!\n")
    database.tallenna_aika(pelaajan_nimi, kulunut_aika)

# HAETAAN KUTSUTAAN FUNKTIO JOKA HAKEE SCOREBOARDING TIETOKANNASTA
def scoreboard():
    print("Scoreboard (top 5 players):\n")
    database.tulosta_pelaajat()