import random
print('Welkom bij Hoger-Lager!')
print('Ik heb een getal tussen 1 en 10 gekozen. Raad eens!')
computer = random.randint(1,10)

gebruiker = int(input('Voer je gok in: '))
poging = 0

while computer != gebruiker:
    poging += 1
    if computer > gebruiker:
        print('Hoger')
    elif computer < gebruiker:
        print('Lager')
    gebruiker = int(input('Voer je gok in: '))

print(f'Geraden in {poging}! Het getal was: {computer}')
