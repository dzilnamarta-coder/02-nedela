# Vienību konvertors
KM_TO_MI = 0.621371 # 1 kilometrs ir aptuveni 0.621371 jūdzes
KG_TO_LB = 2.20462  # 1 kilograms ir aptuveni 2.20462 mārciņas
L_TO_GAL = 0.264172 # 1 litrs ir aptuveni 0.264172 galonu
USD_TO_EUR = 0.84235020 # 1 ASV dolārs ir aptuveni 0.84235020 eiro (šī vērtība var mainīties atkarībā no valūtas kursa)

# Izvēlies konversiju: 1) km<->mi  2) kg<->lb  3) L<->gal
# > 1
# Virziens: 1) km -> mi  2) mi -> km
# > 1
# Ievadi vērtību: 42
# 42.00 km = 26.10 mi

# Konversijas izvele
print("Izvēlies konversiju: 1) km<->mi  2) kg<->lb  3) L<->gal  4) $<->€") 

# Es izmantoju input() funkciju, lai paprasītu lietotāja izvēli.
# Tā kā input() vienmēr atgriež tekstu (str), mana 'izvele' būs teksta formātā.
izvele = input("> ")

# Šeit es pasargāju savu programmu no nepareizas ievades.
# Ja lietotājs ievada kaut ko, kas nav '1', '2', '3' vai '4', es apturu programmu ar exit(), 
# lai vēlāk matemātikas daļā nerastos kļūdas.
if izvele not in ['1', '2', '3', '4']:
    print("Kļūda: Nepareiza izvēle. Lūdzu, ievadi 1, 2, 3 vai 4.")
    exit()

# Konversijas virziena izvēle

# Atkarībā no pirmās izvēles, es piedāvāju atbilstošo konversijas virzienu.
if izvele == '1':
    print("Virziens: 1) km -> mi  2) mi -> km")
elif izvele == '2':
    print("Virziens: 1) kg -> lb  2) lb -> kg")
elif izvele == '3':
    print("Virziens: 1) L -> gal  2) gal -> L")
elif izvele == '4':
    print("Virziens: 1) $ -> €  2) € -> $")
virziens = input("> ") # Šeit es atkal pasargāju savu programmu no nepareizas ievades.
# Vēl viena pārbaude – es pārliecinos, ka lietotājs tiešām ievadīja '1' vai '2'.
if virziens not in ['1', '2']:
    print("Kļūda: Nepareizs virziens. Lūdzu, ievadi 1 vai 2.")
    exit()  



# Vērtības ievade un konversija 
#Šeit man vajadzēja apstrādāt robežgadījumu, ja lietotājs skaitļa vietā ievada burtus.
# Tā kā float() tādā gadījumā izmestu ValueError un programma uzkārtos, 
# es izmantoju try/except bloku, lai noķertu kļūdu un izvadītu informatīvu paziņojumu.
try:
    vertiba = float(input("Ievadi vērtību: "))
except ValueError:
    print("Kļūda: Ievadītā vērtība nav skaitlis! ...")
    exit()
    
# Aprēķini un rezultāta izvadīšana

# Tagad notiek pats rēķināšanas process. 
# Ja virziens ir 1 (uz priekšu), es reizinu savu ievadīto vērtību ar attiecīgo konstanti. 
# Ja virziens ir 2 (atpakaļ), es dalu savu ievadīto vērtību ar konstanti.
# Rezultātu es formatēju ar f-string un :.2f, kas manu skaitli glīti noapaļo līdz 2 decimālzīmēm.

# 1. kategorija (Kilometri un Jūdzes)
if izvele == '1':
    vieniba_1, vieniba_2 = "km", "mi"
    koeficients = KM_TO_MI
elif izvele == '2':
    vieniba_1, vieniba_2 = "kg", "lb"
    koeficients = KG_TO_LB
elif izvele == '3':
    vieniba_1, vieniba_2 = "L", "gal"
    koeficients = L_TO_GAL
elif izvele == '4':
    vieniba_1, vieniba_2 = "$", "€"
    koeficients = USD_TO_EUR
  
# Šajā daļā es veicu pašus aprēķinus atkarībā no lietotāja izvēles un virziena.
# Mana loģika ir vienāda visām četrām kategorijām (garums, svars, tilpums, valūta):
# 1. Ja virziens ir "uz priekšu" (1), es reizinu ievadīto skaitli ar konstanti.
# 2. Ja virziens ir "atpakaļ" (2), es dalu ievadīto skaitli ar konstanti.
# 
# Rezultātu izvadīšanai es izmantoju f-stringus. Lai cipari ekrānā izskatītos 
# glīti un profesionāli, es visur pieliku ":.2f", kas manus skaitļus automātiski 
# noapaļo līdz tieši 2 decimālzīmēm aiz komata.
print("-" * 25)

if izvele == '1':
    if virziens == '1':
        print(f"{vertiba:.2f} km = {vertiba * KM_TO_MI:.2f} mi")
    else:
        print(f"{vertiba:.2f} mi = {vertiba / KM_TO_MI:.2f} km")

elif izvele == '2':
    if virziens == '1':
        print(f"{vertiba:.2f} kg = {vertiba * KG_TO_LB:.2f} lb")
    else:
        print(f"{vertiba:.2f} lb = {vertiba / KG_TO_LB:.2f} kg")

elif izvele == '3':
    if virziens == '1':
        print(f"{vertiba:.2f} L = {vertiba * L_TO_GAL:.2f} gal")
    else:
        print(f"{vertiba:.2f} gal = {vertiba / L_TO_GAL:.2f} L")

elif izvele == '4':
    if virziens == '1':
        print(f"{vertiba:.2f} $ = {vertiba * USD_TO_EUR:.2f} €")
    else:
        print(f"{vertiba:.2f} € = {vertiba / USD_TO_EUR:.2f} $")

print("-" * 25)

#PĀRBAUDE - STRĀDĀ!
#Izvēlies konversiju: 1) km<->mi  2) kg<->lb  3) L<->gal  4) $<->€
#> 2
#Virziens: 1) kg -> lb  2) lb -> kg
#> 2
#Ievadi vērtību: 23
#-------------------------
#23.00 lb = 10.43 kg
#-------------------------



 