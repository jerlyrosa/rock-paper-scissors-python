import random

def play():
    user = input("Choose an option: 'ro' for rock, 'pa' for paper, 'sc' for scissors\n").lower()
    computer = random.choice(['pi', 'pa', 'ti'])

    if user == computer:
        return '¡Empate!'
    if win_user(user, computer) :
        return "¡Ganaste!"
    return '¡Perdiste!'



def win_user(user, opponent):
    if((user == 'ro' and opponent =='sc')
        or (user == 'sc' and opponent =='pa')
        or (user == 'pa' and opponent =='ro')):
        return True
    else:
        return False

print(play())