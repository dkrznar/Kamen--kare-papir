#kamen > škare, škare > papir, papir >kamen
import random

while True:
    #definiranje varijabli 
    odabir_korisnika = input("Odaberi 'kamen', 'škare' ili 'papir' ")
    akcije = ['kamen', 'škare', 'papir']
    odabir_racunala = random.choice(akcije)
    print(f'\n Ti si izabrao {odabir_korisnika}, a računalo je izabralo {odabir_racunala}')

    #algoritam kojim se određuje tko je pobijedio
    if odabir_korisnika == odabir_racunala:
        print(f'Neriješeno! Oboje ste izabrali {odabir_korisnika}')
    elif odabir_korisnika == 'kamen' and odabir_racunala == 'škare':
        print(f'Bravo, {odabir_korisnika} pobijedio je {odabir_racunala}')
    elif odabir_korisnika == 'kamen' and odabir_racunala == 'papir':
        print(f'Racunalo je izabralo {odabir_racunala}! Izgubio si!')
    elif odabir_korisnika == 'škare' and odabir_racunala == 'papir':
        print(f'Bravo, {odabir_korisnika} pobjeđuje {odabir_racunala}!')
    elif odabir_korisnika == 'škare' and odabir_racunala == 'kamen':
        print(f'Racunalo je izabralo {odabir_racunala}! Izgubio si!')
    elif odabir_korisnika == 'papir' and odabir_racunala == 'kamen':
        print(f'Bravo, {odabir_korisnika} pobjeđuje {odabir_racunala}!')
    elif odabir_korisnika == 'papir' and odabir_racunala == 'škare':
        print(f'Racunalo je izabralo {odabir_racunala}! Izgubio si!')
    
    #traženje korisnika za input želi li nastaviti igru ili ne
    nastavi = input('Želiš li nastaviti igru? Odaberi "y" za nastavak ili "n" za prekid: ')
    if nastavi == 'n':
        break

print('Igra je završila')
