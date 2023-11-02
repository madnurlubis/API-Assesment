'''
Tebak Angka
---------------------
'''

import random

attempts_list = []


def show_score():
	if not attempts_list:
		print('there is currently no High Score,'
				'it\'s yours for the taking!')

	else:
		print(f'the current High Score is'
			  f' {min(attempts_list)}attempts')

def start_game():
	attempts = 0
	rand_num = random.randint(1, 10)
	print('Hello Traveler!!! Welcome to the game og Guess!')

	player_name = input('What Is your name?')
	wanna_play = input(
				f'Hi, {player_name}, Would You Like To Play'
				f'The Guessing Game? (Enter Yes/No): ')

	if wanna_play.lower() !='yes':
		Print ('That\'s Cool, Thanks!')
		exit()
	else:
		show_score()

		while wanna_play.lower()=='yes':
			try:
				guess = int(input('Masukkan Nomor dari 1 - 10: '))
				if guess < 1 or guess>10 :
					raise ValueError(
						'Please Guess A Number within the Given Range')
				attempts += 1
				attempts_list.append(attempts)

				if guess == rand_num:
					print('Nice! You got it!')
					print(f'It took you {attempts} attempts')
					wanna_play = input('Would you Like to Play again? (Enter Yes/No): ')
					
					if wanna_play.lower() != 'yes':
						print('That\'s cool, have a good one!')
						break
					else:
						attempts = 0
						rand_num = random.randint(1, 10)
						show_score()
						continue
				else:
					if guess > rand_num:
						print('It\'s lower')
					elif guess < rand_num:
						print('It\'s higher')
			except ValueError as err:
				print('Oh no!, that is not a valid value. Try again...')
				print(err)


if __name__ == '__main__':
    start_game()