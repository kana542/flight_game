from openai import OpenAI #openai kirjasto avainsanojen luomiseen tekoälyn avulla

#funktio joka tuottaa 3kpl avainsanoja saadusta parametrista
def tuota_avainsanat(maa):
    client = OpenAI(api_key = "XXXXXXXXXXXXXXXXXXXX")
    
    completion = client.chat.completions.create(
        model = "gpt-4-0125-preview",
        messages = [{"role": "system", "content": f"Anna suomenkielellä 3 avainsanaa maasta: {maa}. Älä anna maan nimeä suoraan. Anna vastaukset samalla rivillä ja erottele ne pilkulla, älä lisää mitään muuta vastaukseen. "}]
    )

    temp_avainsanat = completion.choices[0].message.content.strip()
    #muutetaan saadut avainsanat listaksi
    avainsanat = [avainsana.strip() for avainsana in temp_avainsanat.split(",")]

    return avainsanat