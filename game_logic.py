import time
import os

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

def step_two():
    print("""
    Valitse vaikeusaste.

    1. Helppo = Aikaa 5min
    2. Keskivaikea = Aikaa 10min
    3. Vaikea = 15min
    """)

    vaikeusaste = int(input("Anna vaikeusaste (1-3): "))

    time.sleep(1)
    os.system("cls")
    
    return vaikeusaste