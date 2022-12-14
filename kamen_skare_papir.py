#kamen > škare, škare > papir, papir >kamen
import random

odabir_korisnika = input("Odaberi 'kamen', 'škare' ili 'papir'")
akcije = ['kamen', 'škare', 'papir']
odabir_racunala = random.choice(akcije)
print(f'\n Ti si izabrao {odabir_korisnika}, a računalo je izabralo {odabir_racunala}')

if odabir_korisnika == odabir_racunala:
    print(f'Neriješeno! Oboje ste izabrali {odabir_korisnika}')
elif odabir_korisnika == 'kamen':
    if odabir_racunala == 'škare':
        print(f'Bravo, {odabir_korisnika} pobijedio je {odabir_racunala}')
    elif odabir_racunala == 'papir':
        print(f'Racunalo je izabralo {odabir_racunala}! Izgubio si!')
elif odabir_korisnika == 'škare':
    if odabir_racunala == 'papir':
        print(f'Bravo, {odabir_korisnika} pobjeđuje {odabir_racunala}!')
    elif odabir_racunala == 'kamen':
        print(f'Racunalo je izabralo {odabir_racunala}! Izgubio si!')
elif odabir_korisnika == 'papir':
    if odabir_racunala == 'kamen':
        print(f'Bravo, {odabir_korisnika} pobjeđuje {odabir_racunala}!')
    elif odabir_racunala == 'škare':
        print(f'Racunalo je izabralo {odabir_racunala}! Izgubio si!')
