import random 

#safley make int
#limit guesses
#too high message
#too low message
#play again

def user_input():
	try:
		chosen_number = int(input("Choose a number between 1 and 10 for the computer to guess: "))		
	except ValueError:
		print("what you entered isnt a number!")
		user_input()

def game():
	flag = True
	while flag:
		try:
			chosen_number = int(input("Choose a number between 1 and 10 for the computer to guess: "))
			flag = False
		except ValueError:
			print("what you entered isnt a number!")
		
	guesses =[]
	computer_guess = random.randint(1, 10)
	guesses.append(computer_guess)
	while len(guesses) < 5:
			#compare computer_guess to chosen_number
			if chosen_number == computer_guess:
				print("You got it you win mr./mrs. computer! my number was {}".format(computer_guess))
				break
			elif chosen_number < computer_guess:
				print("My number is lower than your guessed number {} mr./mrs. computer ".format(computer_guess))
				x = computer_guess-1
				computer_guess = random.randint(1, x)
				guesses.append(computer_guess)
			else:
				print("My number is higher than your guessed number {} mr./mrs. computer".format(computer_guess))
				x = computer_guess+1
				computer_guess = random.randint(x, 10)
				guesses.append(computer_guess)
			#print hit/miss
	else:
		print("You didnt get it! my number was {}".format(chosen_number))
		play_again = input("Do you want to play again? Y/N ")
		if play_again.lower() != 'n' :
			game()
		else:
			print("Bye!")

game()