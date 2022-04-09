import random


chances = 0
boundary = 0
while chances == 0 or boundary == 0:
    try:
        if chances == 0:
            chances = int(input("Enter amount of chance you need to try: "))
        if boundary == 0:
            boundary = int(input('Enter number boundary you need to guess: '))
    except ValueError:
        print('Only numbers are allowed!!!')

secret_number = random.randint(1, boundary)

while chances > 0:
    print(f'you have {chances} chances')
    the_number = 0
    try:
        the_number = int(input(f'Guess number from (1-{boundary}): '))
    except ValueError:
        print('Only numbers are allowed!!!')
        continue
    chances -= 1
    if 1 <= the_number <= boundary:
        if secret_number == the_number:
            print('You have won!')
            break
        elif secret_number > the_number:
            print('your number is too low')
        elif secret_number < the_number:
            print('your number is too high')

else:
    print('You have lost!')
print(f'The number was {secret_number} ')
print('Game over! Come again another time')
