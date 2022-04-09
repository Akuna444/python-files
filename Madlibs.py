import random


def random_message():

    the_word = input('Put your word here: ')
    word = [ f'Your country is {the_word} country',
             f'I am {the_word} person',
             f'I hate to do {the_word}',
             f'All people are {the_word}',
             f'{the_word} is the most thing I hate'
             ]
    return ''.join(random.sample(word, 1))


counter = 0
while True:
    counter = counter + 1
    print(random_message())
    if counter == 5:
        break

print('Game over come again another time')




