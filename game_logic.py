import database
import time
import os
from openai import OpenAI
from geopy.distance import geodesic
import random
import math

oikea_maa, oikean_maan_iso = database.maa_random() # satunnainen maa ja sen iso-koodi (rajoitettu euroopan maihin)
oikea_lentoasema = database.lentoasema_random(oikean_maan_iso) # satunnainen lentokenttä/helikopterialusta arvotusta maasta
koordinaatti_lat, koordinaatti_lon = database.lentoasema_koordinaatit(oikea_lentoasema) # lentoaseman/helikopterialustan koordinaatit
kohteen_tyyppi = database.lentoasema_tyyppi(oikea_lentoasema) # tallennetaan kohteen tyyppi (lentoasema vai heliport) muuttujaan

maa_arvattu = False

def step_one():
    time.sleep(2)

    print("""
                                        |
                                        |
                                        |
                                      .-'-.
                                     ' ___ '
                           ---------'  .-.  '---------
           _________________________'  '-'  '_________________________
            ''''''-|---|--/    \==][^',_m_,'^][==/    \--|---|-''''''
                          \    /  ||/   H   \||  \    /
                           '--'   OO   O|O   OO   '--'
      
                                  S K Y H A W K
                                       v.1
    """)

    time.sleep(4)
    os.system('cls')

    print("""
                               Welcome to the Skyhawk game!

    Your mission is to locate a stolen helicopter from a random airport or heliport across Europe. 
         You need to use the browser map that you prefer to help you locate the helicopter. 
                        We recommend Google Maps and OurAirports.
    """)

    time.sleep(12)
    os.system("cls")

def step_two():
    global maa_arvattu
    print(f"First you need to guess the correct country where the helicopter might be.\nYour clues are following: {tuota_avainsanat(oikea_maa)}")
    while True:
        maa_arvaus = input("Your answer: ")
        if maa_arvaus == oikea_maa:
            print("Correct!")
            maa_arvattu = True
            break
        else:
            print("Wrong answer. Try again!")

def step_three():
    print(f"Type of the location: {kohteen_tyyppi}")
    print(f"The coordinates are: {gps_muutos(koordinaatti_lat, koordinaatti_lon, 100)}")

    while True:
        lentoasema_arvaus = input("Your answer: ")
        arvaus = tarkista_arvaus(lentoasema_arvaus, oikea_lentoasema)
        
        if arvaus == "ok":
            print("Correct! You win the game!")
            break
        elif arvaus == "ei":
            print("Wrong answer. Try again!")
        else:
            print("error")

def tuota_avainsanat(maa):
    client = OpenAI(api_key = "xxxxx")
    
    completion = client.chat.completions.create(
        model = "gpt-4-0125-preview",
        messages = [{"role": "system", "content": f"Anna englannin kielellä 3 avainsanaa maasta: {maa}. ÄLÄ ANNA KOSKAAN MAAN NIMEÄ SUORAAN. Anna vastaukset samalla rivillÃ¤ ja erottele ne pilkulla, älä lisää mitään muuta vastaukseen."}]
    )

    avainsanat = completion.choices[0].message.content.strip()

    return avainsanat

def tarkista_arvaus(arvaus, oikea_lentoasema):
    client = OpenAI(api_key = "xxxxx")
    
    completion = client.chat.completions.create(
        model = "gpt-4-0125-preview",
        messages = [{"role": "system", "content": f"Tarkista vastaako kohde {arvaus}, kohdetta {oikea_lentoasema}. Huom! Jos annettu kohde on kuitenkin oikea, mutta vain eri nimellä tai se muistuttaa vastausta, sen silloin oikein. Tarkista tämä kaksi kertaa että olet todella varma vastauksesta. Jos kohde vastaa, palauta 'ok', jos ei vastaa, palauta 'ei'. Älä palauta mitään muuta."}]
    )

    vastaus = completion.choices[0].message.content.strip()

    return vastaus

def gps_muutos(lat, lon, etäisyys):

    alkuperäinen_paikka = lat, lon

    etäisyys_km = etäisyys / 1000
    kulma = random.uniform(0, 2 * math.pi)

    uudet_koordinaatit = geodesic(kilometers = etäisyys_km).destination(alkuperäinen_paikka, bearing=math.degrees(kulma))

    return f"{uudet_koordinaatit.latitude}, {uudet_koordinaatit.longitude}"