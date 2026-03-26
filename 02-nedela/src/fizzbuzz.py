import sys

# UZDEVUMS 4: FIZZBUZZ

# 1. KĻŪDU APSTRĀDE (Robežgadījumi)

# Pārbaudu, vai lietotājs vispār norādīja skaitli.
# Ja komandā ir tikai faila nosaukums, saraksta garums ir mazāks par 2.
if len(sys.argv) < 2:
    print("Kļūda: Lūdzu, norādi skaitli N! Piemēram: python3 fizzbuzz.py 15")
    sys.exit()

# Pārbaudu, vai ievadītais tiešām ir skaitlis, nevis burti.
try:
    n = int(sys.argv[1])
except ValueError:
    print("Kļūda: Ievadītais arguments nav skaitlis!")
    sys.exit()

# 2. CIKLS UN DALĀMĪBA
rezultati = []

# Eju cauri visiem skaitļiem no 1 līdz N (ieskaitot, tāpēc n + 1)
for i in range(1, n + 1):
    
    # SECĪBA IR SVARĪGA:
    # 1. Vispirms pārbaudu, vai dalās ar ABIEM (ar 3 un 5)
    if i % 3 == 0 and i % 5 == 0:
        rezultati.append("FizzBuzz")
        
    # 2. Pēc tam pārbaudu, vai dalās tikai ar 3
    elif i % 3 == 0:
        rezultati.append("Fizz")
        
    # 3. Pēc tam pārbaudu, vai dalās tikai ar 5 (Lūk, kur ir 5!)
    elif i % 5 == 0:
        rezultati.append("Buzz")
        
    # 4. Ja nedalās ne ar 3, ne 5, pievienoju pašu skaitli
    else:
        rezultati.append(str(i))

# 3. REZULTĀTA IZVADE 
# Savienoju visus saraksta elementus ar komatu un atstarpi
print(", ".join(rezultati))


#Pārbaude - Sanāca!
#1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz
