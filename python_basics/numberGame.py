import random 

#safley make int
#limit guesses
#too high message
#too low message
#play again

def game():
	#generate a random number between number between 1 and 10
	secret_num = random.randint(1, 10)
	guesses =[]

	while len(guesses) < 5:
		try:
			# get a number guess from the player
			guess = int(input("Guess a number between 1 and 10: "))
			guesses.append(guess)
		except ValueError:
			print("{} isnt a number!".format(guess))
			break
		else:
			#compare guess to secret number
			if guess == secret_num:
				print("You got it you win! my number was {}".format(secret_num))
				break
			elif guess < secret_num:
				print("My number is higher than your guessed number {} ".format(guess))
			else:
				print("My number is lower than your guessed number{} ".format(guess))
			#print hit/miss
	else:
		print("You didnt get it! my number was {}".format(secret_num))
		play_again = input("Do you want to play again? Y/N ")
		if play_again.lower() != 'n' :
			game()
		else:
			print("Bye!")



game()