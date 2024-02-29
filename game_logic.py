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

################## VAIHEET #####################

# Step 1. Alkunäyttö missä kerrotaan pelaajalle mistä on kyse
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


# Step 2. Silmukka kysely kunnes käyttäjä saa oikean vastauksen (oikea maan nimi)
def step_two(oikea_maa):
    print(f"Arvaa oikea maa seuraavista vihjeistä: {tuota_avainsanat(oikea_maa)}")
    while True:
        maa_arvaus = input("Vastaus: ")
        if maa_arvaus == oikea_maa:
            print("Oikein!")
            break
    return True


# Step 3. Annetaan uudet vihjeet käyttäjälle
def step_three():
    print("Noniin, siirrytään seuraavaan vaiheeseen!\nSeuraavaksi sinun pitää etsiä selaimella kartasta oikea lentoasema!")
    print(f"Millainen kohde on kyseessä?: {kohteen_tyyppi}")
    if kohteen_koko != False:
        print(f"Kohteen koko: {kohteen_koko}")
  
    print(f"GPS-koordinaatit lähialueelta: {koordinaatit}")


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