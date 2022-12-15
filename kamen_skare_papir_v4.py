import random

while True:
    odabir_korisnika_1 = input('Igrač 1: Odaberi "kamen", "škare" ili "papir": ')
    odabir_korisnika_2 = input('Igrač 2: Odaberi "kamen", "škare" ili "papir": ')

    print(f'\nIgrač 1 je izabrao {odabir_korisnika_1}, a Igrač 2 je izabralo {odabir_korisnika_2}!')

    #algoritam kojim se određuje tko je pobijedio
    if odabir_korisnika_1 == odabir_korisnika_2:
        print(f'Neriješeno! Oboje ste izabrali {odabir_korisnika_2}')
    elif odabir_korisnika_1 == 'kamen' and odabir_korisnika_2 == 'škare':
        print(f'Igrač 1 je izabrao {odabir_korisnika_1} i pobijedio je!')
    elif odabir_korisnika_1 == 'kamen' and odabir_korisnika_2 == 'papir':
        print(f'Igrač 2 je izabrao {odabir_korisnika_2} i pobjedio je!')
    elif odabir_korisnika_1 == 'škare' and odabir_korisnika_2 == 'papir':
        print(f'Igrač 1 je izabrao {odabir_korisnika_1} i pobjedio je!')
    elif odabir_korisnika_1 == 'škare' and odabir_korisnika_2 == 'kamen':
        print(f'Igrač 2 je izabralo {odabir_korisnika_2} i pobjedio je!')
    elif odabir_korisnika_1 == 'papir' and odabir_korisnika_2 == 'kamen':
        print(f'Igrač 1 je izabrao {odabir_korisnika_1} i pobjedio je!')
    elif odabir_korisnika_1 == 'papir' and odabir_korisnika_2 == 'škare':
        print(f'Igrač 2 je izabralo {odabir_korisnika_2} i pobjedio je! ')
    
    #traženje korisnika za input želi li nastaviti igru ili ne
    nastavi = input('Želite li nastaviti igru? Odaberi "y" za nastavak ili "n" za prekid: ')
    if nastavi == 'n':
        break

print('Igra je završila')