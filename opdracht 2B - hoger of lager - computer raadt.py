import random
print('Welkom bij Hoger-Lager!')
gebruiker = int(input('Kies een getal tussen de 1 en 10: '))
computer = random.randint(1,10)
poging = 0

while computer != gebruiker:
    poging += 1
    if computer > gebruiker:
        print('Hoger')
    elif computer < gebruiker:
        print('Lager')
    computer = random.randint(1,10)

print(f'Geraden in {poging}! Het getal was: {computer}')
