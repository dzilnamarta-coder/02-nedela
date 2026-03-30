# MAINĪGO DEFINĒŠANA UN DATU TIPI 
vards = "Marta" # str (teksta virkne)
garums = 1.67 # float (decimāldaļa,reāls skaitlis)
Vecums = 21 # int (vesels skaitlis)
ir_studente = True # bool (loģiska vērtība,var būt tikai True vai False)
hobijs = None # NoneType (šis tips apzīmē, ka mainīgajam nav vērtības vai tas ir tukšs)

# šos viņs automātiski piedāvā izveidot 
print(f"Vērtība: {vards}, Tips: {type(vards)}")
print(f"Vērtība: {garums}, Tips: {type(garums)}")
print(f"Vērtība: {Vecums}, Tips: {type(Vecums)}")
print(f"Vērtība: {ir_studente}, Tips: {type(ir_studente)}")
print(f"Vērtība: {hobijs}, Tips: {type(hobijs)}")

# Python truthy/falsy uzvedības piemēri

# 1. piemērs: Tukša teksta virkne ir Falsy (jo tajā nekā nav)
print(f"1. Vai tukšs teksts '' ir patiess? {bool('')}") # (False) (jo, tas ir tukšs teksts)

# 2. piemērs: Vārds "Marta" ir Truthy, jo jebkura netukša virkne skaitās True
print(f"2. Vai vārds '{vards}' ir patiess? {bool(vards)}") # (True) (jo, tas nav tukšs teksts )

# 3. piemērs: Skaitlis 0 matemātikā un loģikā vienmēr skaitās Falsy
print(f"3. Vai skaitlis 0 ir patiess? {bool(0)}") # (False) (jo, tas ir 00)

# 4. piemērs: Pozitīvs skaitlis, piemēram, 1.67, ir Truthy
print(f"4. Vai skaitlis {garums} ir patiess? {bool(garums)}") # (True) (jo tas nav 0)

# Tiešās datu tipu pārveides un robežgadījumi

# 1. Konversija: str uz int (teksta pārvēršana veselā skaitlī, lai varētu saskaitīt)
teksta_skaitlis = "10"
print(f"1. Teksts '10' pārveidots par int un saskaitīts: {int(teksta_skaitlis) + 5}") # (jo int() pārvērš "10" par 10, un tad mēs saskaitām 5, rezultāts ir 15)

# 2. Konversija: float uz int (daļskaitļa pārvēršana veselā skaitlī)
print(f"2. Garums {garums} pārveidots par veselu skaitli: {int(garums)}") # (jo int() noņem decimāldaļu, un 1.67 kļūst par 1)

# 3. Konversija: int uz float
print(f"3. Vecums {Vecums} pārveidots par daļskaitli: {float(Vecums)}")  # (jo float() pārvērš 21 par 21.0, pievienojot decimāldaļu)

# Robežgadījumi (kas notiek, ja konversija neizdodas)

# Mēģinājums tekstu ar burtiem pārvērst par skaitli print(int(vards)) KĻŪDA! Izmetīs ValueError, jo burtus nevar pārvērst ciparos. 

# Mēģinājums tekstu ar punktu pa taisno pārvērst par veselu skaitli print(int("1.67")) # KĻŪDA! Izmetīs ValueError, jo int() nesaprot punktu tekstā.

# Kā pareizi pārvērst tekstu ar punktu par veselu skaitli:
print(f"Droša '1.67' teksta konversija: {int(float('1.67'))}") # (Vispirms par float, tad par int)

# Interesantie gadījumi no Jūsu piemēriem 
print(0.1 + 0.2 == 0.3)     # False, tapec ka 0.1 un 0.2 nevar precīzi attēlot binārajā formātā, un rezultāts ir nedaudz mazāks par 0.3, tāpēc tas nav vienāds ar 0.3.
print(round(2.5))           # 2 (jo Python izmanto "banker's rounding", kur 2.5 tiek noapaļots uz tuvāko pāra skaitli, kas ir 2)
print(round(3.5))           # 4 (jo 3.5 tiek noapaļots uz tuvāko pāra skaitli, kas ir 4)