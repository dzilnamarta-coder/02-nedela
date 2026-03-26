import random

# UZDEVUMS 5: MINĒŠANAS SPĒLE

print("=== SĀKAM MINĒŠANAS SPĒLI! ===")

# 1. ĀRĒJAIS CIKLS ("Spēlēt vēlreiz" loģika)
while True:
    
    # Tiklīdz sākas jauna spēle, mēs atiestatām datus:
    slepenais_skaitlis = random.randint(1, 100)
    meginajumi = 0
    maksimālie_meginajumi = 10
    
    print("\nEsmu iedomājies skaitli no 1 līdz 100. Tev ir 10 mēģinājumi!")

    # 2. IEKŠĒJAIS CIKLS (Pats minēšanas process)
    while True:
        ievade = input(f"Tavs minējums (atlikuši {maksimālie_meginajumi - meginajumi}): ")
        
        # Pārbaudām, vai ievadīts skaitlis
        try:
            minejums = int(ievade)
        except ValueError:
            print("Kļūda: Lūdzu ievadi tikai ciparus!")
            continue # Šis ir svarīgi! Sākam ciklu no jauna, nepieskaitot mēģinājumu.
            
        # Ja ievade ir veiksmīga, pieskaitām mēģinājumu
        meginajumi += 1
        
        # Pārbaudām pašu minējumu
        if minejums == slepenais_skaitlis:
            print(f" APSVEICU! Tu uzminēji skaitli {slepenais_skaitlis} ar {meginajumi}. mēģinājumu!")
            break # Izlaužamies no iekšējā (minēšanas) cikla
            
        elif minejums < slepenais_skaitlis:
            print("Par mazu!")
            
        else:
            print("Par lielu!")
            
        # Pārbaudām limitu (vai mēģinājumi nav beigušies)
        if meginajumi >= maksimālie_meginajumi:
            print(f" Spēle galā! Tu iztērēji visus mēģinājumus. Pareizais skaitlis bija {slepenais_skaitlis}.")
            break # Izlaužamies no iekšējā cikla, jo zaudējām

    # 3. SPĒLĒT VĒLREIZ PĀRBAUDE (Ārējā cikla beigas)
    print("-" * 25)
    atbilde = input("Vai gribi spēlēt vēlreiz? (j/n): ").lower()
    
    # Ja lietotājs ievada jebko, kas nav 'j', mēs laužam lielo ciklu un beidzam programmu.
    if atbilde != 'j':
        print("Paldies par spēli! Uz redzēšanos!")
        break
    
#PĀRBAUDE - Strādā!

#Esmu iedomājies skaitli no 1 līdz 100. Tev ir 10 mēģinājumi!
#Tavs minējums (atlikuši 10): 5
#Par mazu!
#Tavs minējums (atlikuši 9): 30
#Par lielu!
#Tavs minējums (atlikuši 8): 22
#Par lielu!
#Tavs minējums (atlikuši 7): 10
#Par mazu!
#Tavs minējums (atlikuši 6): 15
#Par lielu!
#Tavs minējums (atlikuši 5): 12
#Par mazu!
#Tavs minējums (atlikuši 4): 13
# APSVEICU! Tu uzminēji skaitli 13 ar 7. mēģinājumu!
#-------------------------
#Vai gribi spēlēt vēlreiz? (j/n): n
#Paldies par spēli! Uz redzēšanos!