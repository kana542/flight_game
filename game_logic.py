import database
import time
import os

from openai import OpenAI

################# MUUTTUJAT ####################

oikea_maa = database.maa_random() # tallentaan arvottu maan nimi muuttujaan
oikea_kaupunki = database.kaupunki_random() # tallentaan arvottu maan nimi muuttujaan
oikea_lentoasema = database.lentoasema_random() # tallennetaan arvottu lentoaseman nimi muuttujaan
koordinaatit = database.lentoasema_koordinaatit() # tallennetaan lentoaseman koordinaatit muuttujaan tuplena

kohteen_tyyppi = database.lentoasema_tyyppi() # tallennetaan kohteen tyyppi (lentoasema vai heliport) muuttujaan
kohteen_koko = database.lentoasema_koko() # jos kyseessä lentoasema niin tallennetaan kohteen koko muuttujaan

maa_arvattu = False

#Luodaan pelaajan kierrosajan mittaava funktiot

# def pelin_kulku():
#     # Kysy pelaajan nimeä
#     pelaajan_nimi = input("Anna pelaajan nimi: ")
#
#     # Aloita kierros
#     def aloita_kierros():
#         return time.time()
#
#     def lopeta_kierros(alkuaika):
#         loppuaika = time.time()
#         return loppuaika - alkuaika
#
#     # Tallenna kierrosaika tietokantaan
#     tallenna_aika('pelaajatiedot.db', pelaajan_nimi, kierrosaika)
#
#     print(f"Pelaajan {pelaajan_nimi} kierrosaika {kierrosaika} sekuntia tallennettu onnistuneesti.")

#Funktio kierrosajasta ja pelaajan nimen kutsumisesta
def tallenna_aika():
    yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='rootpass',
        autocommit=True
    )

def pelin_kulku():
    pelaajan_nimi = input("Anna pelaajan nimi: ")

    #Aloitetaan kierros
    alkuaika = time.time()

    kierrrosaika = time.time() - alkuaika




################## STEP ONE ####################
# ALKUNÄYTTÖ MISSÄ SELITETÄÄN PELAAJALLE HOMMAN NIMI

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
                               Tervetuloa skyhawk peliin!

    Tehtävänäsi on paikantaa varastettu lentokone/helikopteri satunnaiselta
    sijainnista euroopassa. Sijainti on joko lentoasemalla tai helikopterialustalla.
    Avaa valmiiksi selaimesta haluamasi karttaselain (suosittelemme google mapsia).
    """)

    time.sleep(12)
    os.system("cls")


################## STEP TWO ####################
# * TUOTETAAN PELAAJALLE 3KPL AVAINSANOJA OPENAI APIN AVULLA
# * JOS PELAAJA ARVAA OIKEIN, LOOPPI MENEE BROKIE JA PELI JATKUU SEURAAVAAN VAIHEESEEN

def step_two(oikea_maa):
    print(f"Arvaa oikea maa seuraavista vihjeistä: {tuota_avainsanat(oikea_maa)}")
    while True:
        maa_arvaus = input("Vastaus: ")
        if maa_arvaus == oikea_maa:
            print("Oikein!")
            maa_arvattu = True
            break

################## STEP THREE ####################
# ANNETAAN PELAAJALLE VIIMEISET VIHJEET ELI KOHTEEN TYYPPI (LENTOASEMA TAI HELIPORT), KOKO JA KOORDINAATIT JOTKA HIEMAN HUMALASSA
        
def step_three():
    print("Noniin, siirrytään seuraavaan vaiheeseen!\nSeuraavaksi sinun pitää etsiä selaimella kartasta oikea lentoasema!")
    print(f"Millainen kohde on kyseessä?: {kohteen_tyyppi}")
    if kohteen_koko != False:
        print(f"Kohteen koko: {kohteen_koko}")
  
    print(f"GPS-koordinaatit lähialueelta: {koordinaatit}")

################## STEP FOUR ####################

def step_four():
    while True:
    

################ MUUT PASKAT ######################

#funktio joka tuottaa 3kpl avainsanoja saadusta parametrista
def tuota_avainsanat(maa):
    client = OpenAI(api_key = "XXXXXXXXXXXXXXXXXXXX")
    
    completion = client.chat.completions.create(
        model = "gpt-4-0125-preview",
        messages = [{"role": "system", "content": f"Anna suomenkielellä 3 avainsanaa maasta: {maa}. Älä anna maan nimeä suoraan. Anna vastaukset samalla rivillä ja erottele ne pilkulla, älä lisää mitään muuta vastaukseen."}]
    )

    temp_avainsanat = completion.choices[0].message.content.strip()
    #muutetaan saadut avainsanat listaksi
    avainsanat = [avainsana.strip() for avainsana in temp_avainsanat.split(",")]

    return avainsanat

# funktio joka tarkistaa onko satunnaisesti tuotettu lentoasema google mapsissa 
def tarkista_lentoasema():
    client = OpenAI(api_key = "XXXXXXXXXXXXXXXXXXXX")
    
    completion = client.chat.completions.create(
        model = "gpt-4-0125-preview",
        messages = [{"role": "system", "content": f"Tarkista seuraava lentoasema/helikopterialusta, löytyykö se google mapsista. Vastaa vain 1 jos löytyy ja 0 jos ei löydy."}]
    )

    temp_avainsanat = completion.choices[0].message.content.strip()
    #muutetaan saadut avainsanat listaksi
    avainsanat = [avainsana.strip() for avainsana in temp_avainsanat.split(",")]

    return avainsanat