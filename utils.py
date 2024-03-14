from openai import OpenAI
from geopy.distance import geodesic
import random
import math

# TUOTETAAN 3 KPL AVAINSANOJA PARAMETRIKSI ANNETUSTA MAASTA OPENAI RAJAPINNAN AVULLA
def tuota_avainsanat(maa):
    client = OpenAI(api_key = "Xxxxxxxxxxxxxxxx")
    
    completion = client.chat.completions.create(
        model = "gpt-4-0125-preview",
        messages = [{"role": "system", "content": f"Anna englannin kielellä 3 avainsanaa maasta: {maa}. ÄLÄ ANNA KOSKAAN MAAN NIMEÄ SUORAAN. Anna vastaukset samalla rivillä ja erottele ne pilkulla, älä lisää mitään muuta vastaukseen."}]
    )

    avainsanat = completion.choices[0].message.content.strip()

    return avainsanat


# TARKISTETAAN ENSIMMÄINEN PARAMETRI VASTAAKO SE TOISTA PARAMETRIA OPENAI RAJAPINNAN AVULLA
def tarkista_arvaus(arvaus, oikea_lentoasema):
    client = OpenAI(api_key = "Xxxxxxxxxxx")
    
    completion = client.chat.completions.create(
        model = "gpt-4-0125-preview",
        messages = [{"role": "system", "content": f"Tarkista vastaako kohde {arvaus}, kohdetta {oikea_lentoasema}. Huom! Jos annettu kohde on kuitenkin oikea, mutta vain eri nimellä tai se muistuttaa vastausta, sen silloin oikein. Tarkista tämä kaksi kertaa että olet todella varma vastauksesta. Jos kohde vastaa, palauta 'ok', jos ei vastaa, palauta 'ei'. Älä palauta mitään muuta."}]
    )

    vastaus = completion.choices[0].message.content.strip()

    return vastaus


# MUUTETAAN PARAMETREIHIN SAATAVAT LAT JA LON TIEDOT HALUTULLA ETÄISYYDELLÄ (KOLMAS PARAMETRI)
def gps_muutos(lat, lon, etäisyys):

    alkuperäinen_paikka = lat, lon

    etäisyys_km = etäisyys / 1000
    kulma = random.uniform(0, 2 * math.pi)

    uudet_koordinaatit = geodesic(kilometers = etäisyys_km).destination(alkuperäinen_paikka, bearing=math.degrees(kulma))

    return f"{uudet_koordinaatit.latitude}, {uudet_koordinaatit.longitude}"