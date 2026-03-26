# UZDEVUMS 3: ATBILSTĪBAS PĀRBAUDĪTĀJS

print("=== ATBILSTĪBAS PĀRBAUDĪTĀJS ===")

# 1. VECUMA IEVADE UN KĻŪDU APSTRĀDE 
# Šeit es izmantoju 'while True' ciklu, lai programma neatlaidīgi prasītu vecumu 
# tik ilgi, kamēr lietotājs ievada pareizu ciparu.
# try/except bloks pasargā no programmas nobrukšanas, ja skaitļa vietā netīšām ievada burtus.
# Tāpat es apstrādāju robežgadījumu - vecums taču nevar būt negatīvs!
while True:
    try:
        vecums = int(input("Ievadi vecumu: "))
        if vecums < 0:
            print("Kļūda: Vecums nevar būt negatīvs. Lūdzu, mēģini vēlreiz.")
        else:
            break # Ja viss ir pareizi, es laužos ārā no cikla un eju tālāk
    except ValueError:
        print("Kļūda: Lūdzu, ievadi veselu skaitli!")

# 2. JAUTĀJUMI UN PĀRVEIDOŠANA UZ BOOL
# Lai izvairītos no "viltus pozitīviem" rezultātiem (jo bool("n") Python uztver kā True!),
# es katru atbildi pārbaudu manuāli. Ja ievadīts 'j', mainīgais kļūst par True. 
# Ja ievada jebko citu ('n', atstarpi utt.), tas kļūst par False.
# .lower() metode ir drošībai, ja lietotājs nejauši ievada lielo burtu.

aplieciba_atbilde = input("Vai ir autovadītāja apliecība? (j/n): ").lower()
ir_aplieciba = True if aplieciba_atbilde == 'j' else False

students_atbilde = input("Vai ir students? (j/n): ").lower()
ir_students = True if students_atbilde == 'j' else False

veterans_atbilde = input("Vai ir veterāns? (j/n): ").lower()
ir_veterans = True if veterans_atbilde == 'j' else False

# 3. LOĢISKIE NOSACĪJUMI
# Šajā daļā es veicu visas pārbaudes, izmantojot operatorus and, or un not.

# 1. Balsošana: drīkst, ja vecums ir 18 vai vairāk
if vecums >= 18:
    balsot_teksts = "Jā ✓"
else:
    balsot_teksts = "Nē ✗"

# 2. Auto īre: vajadzīgs gan vecums (>= 21), gan apliecība.
# Es pievienoju papildu elif ar 'not', lai paskaidrotu, kāpēc tieši īre ir atteikta.
if vecums >= 21 and ir_aplieciba:
    auto_teksts = "Jā ✓"
elif vecums >= 21 and not ir_aplieciba: 
    auto_teksts = "Nē ✗ (nav apliecības)"
else:
    auto_teksts = "Nē ✗ (nepietiekams vecums)"

# 3. Senioru atlaide: der jebkurš no nosacījumiem (gadi >= 65 VAI veterāns), tāpēc te lietoju 'or'
if vecums >= 65 or ir_veterans:
    seniors_teksts = "Jā ✓"
else:
    seniors_teksts = "Nē ✗"

# 4. Studentu atlaide: jāiekļaujas vecuma robežās UN obligāti jābūt studentam
if 16 <= vecums <= 26 and ir_students:
    students_teksts = "Jā ✓"
else:
    students_teksts = "Nē ✗"

# --- 4. REZULTĀTU IZVADE ---
# Visbeidzot, es visu izdrukāju vienuviet, smuki sakārtojot ar atstarpēm, 
# lai terminālī izskatītos precīzi tā, kā prasīts mājasdarba paraugā!
print("-" * 25)
print(f"Balsošana:        {balsot_teksts}")
print(f"Auto īre:         {auto_teksts}")
print(f"Senioru atlaide:  {seniors_teksts}")
print(f"Studentu atlaide: {students_teksts}")


#PĀRBAUDE - SANĀCA!
#Ievadi vecumu: 21
#Vai ir autovadītāja apliecība? (j/n): j
#Vai ir students? (j/n): j
#Vai ir veterāns? (j/n): n
#-------------------------
#Balsošana:        Jā ✓
#Auto īre:         Jā ✓
#Senioru atlaide:  Nē ✗
#Studentu atlaide: Jā ✓