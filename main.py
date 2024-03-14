import game_logic
import time
import os

os.system("cls")

while True:

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
          
                               Start a new game (1)
                                  Scoreboard (2)
                                     Quit (3)
    """)

    valinta = int(input("Select option 1-3: "))

    if valinta == 1:
        os.system('cls')

        pelaaja_nimi = input("Please enter your username: ")
        aloitus_aika = time.time()

        os.system("cls")

        game_logic.step_one()
        game_logic.step_two()
        game_logic.step_three() 
        
        # kierros aikojen ylös ottaminen ja muuttaminen oikeaan muotoon
        lopetus_aika = time.time()
        kulunut_aika_sekunnit = lopetus_aika - aloitus_aika - 23
        tunnit, jaannos = divmod(kulunut_aika_sekunnit, 3600)
        minuutit, sekunnit = divmod(jaannos, 60)
        kulunut_aika_str = f"{int(tunnit):02d}:{int(minuutit):02d}:{int(sekunnit):02d}"

        game_logic.tallenna_aika(pelaaja_nimi, kulunut_aika_str)
    
    elif valinta == 2:
        os.system("cls")
        game_logic.scoreboard()
        print()
    
    elif valinta == 3:
        os.system("cls")

        print("Thank you for playing, bye!")
        time.sleep(1)
        break

    else:
        print("Not an option, choose correct one!")