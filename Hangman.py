import random

guess_word = ['jaaaaanuary', 'afffffection', 'oraaanges', 'eleephants', 'unconnnditional']
word = random.choice(guess_word)
length = len(word)
count = 0


def game_play():
    dash = length * '_'
    while count < 5:
        user_word = input('Enter your word here: ')
        print(dash.count(user_word))
        letter_count = dash.count(user_word)
        index_counter = 0
        if dash.count(user_word) >= 1:
            index_counter += letter_count
        index_of_word = [index for index, element in enumerate(word) if element == user_word]
        if len(user_word) == 1:
            if user_word in word:
                try:
                    position = index_of_word[index_counter]
                except IndexError:
                    pass

                word_list = list(dash)
                word_list[position] = user_word
                replaced_word = ''.join(word_list)
                dash = replaced_word
                print(dash)
            else:
                print('uu')

            if dash == word:
                print('You win Bro')
                break

        else:
            print('Only one letter allowed!!!')


game_play()
