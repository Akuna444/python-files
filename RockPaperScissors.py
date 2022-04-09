import random
print("Enter 's' for Scissors,"
      " Enter 'p' for Paper,"
      " Enter 'r' for Rock,"
      )
possible_values = ['s', 'p', 'r']
rounds = 0
computer_win_count = 0
user_win_count = 0
draw_count = 0
while rounds == 0:
    try:
        rounds = int(input('Enter Amount of Round you want to play: '))
    except ValueError:
        print('Only numbers are Allowed!!!')

while rounds > 0:
    user = input('You: ').lower()
    computer = random.choice(possible_values)
    if user == 's' or user == 'r' or user == 'p':
        rounds -= 1
        if user == computer:
            draw_count += 1
            print(f'Computer: {computer} \nYou both entered {user}. it is a tie!')
        if user == 's':
            if computer == 'r':
                print(f'Computer: {computer} \nRock smash Scissor, Computer Win!')
                computer_win_count += 1
            elif computer == 'p':
                print(f'Computer: {computer} \nScissor cut Paper, You Win!')
                user_win_count += 1

        if user == 'r':
            if computer == 's':
                print(f'Computer: {computer} \nRock smash Scissor, You Win!')
                user_win_count += 1
            elif computer == 'p':
                print(f'Computer: {computer} \nPaper covers Rock, Computer Win!')
                computer_win_count += 1
        if user == 'p':
            if computer == 's':
                print(f'Computer: {computer} \n Scissor cut Paper, Computer Win!')
                computer_win_count += 1
            elif computer == 'r':
                print(f'Computer: {computer} \n Paper covers Rock, You Win!')
                user_win_count += 1
        print(f'{rounds} rounds left')
    else:
        print('Enter proper word!')

print('Game over!\n'
      f'Computer win {computer_win_count} times. \n'
      f'You win {user_win_count} times. \n'
      f'Draw {draw_count} times. \n'       
      'Come again another time')







