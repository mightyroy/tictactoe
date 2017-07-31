import random


def generate_computer_choice():
	choices  = [x for x in range(9)]
	random.shuffle(choices)
	return choices


def display(matrix):

	string = str(matrix[0]) + "|" + str(matrix[1]) +  "|" + str(matrix[2]) + "\n" + "-----\n" + \
			 str(matrix[3]) + "|" + str(matrix[4]) +  "|" + str(matrix[5]) + "\n"  + "-----\n" + \
			 str(matrix[6]) + "|" + str(matrix[7]) +  "|" + str(matrix[8]) 

	return string.replace("0", " ")


def checkwin(matrix):

	#row win
	if (matrix[0] == matrix[1] and matrix[1] == matrix[2] and (matrix[0] == "X" or matrix[0]== "O")) or \
	(matrix[3]== matrix[4] and matrix[4] == matrix[5] and (matrix[3] == "X" or matrix[3] == "O")) or \
	(matrix[6]== matrix[7] and matrix[7] == matrix[8] and (matrix[6] == "X" or matrix[6] == "O")) :  
		return True


	#col win
	elif (matrix[0] == matrix[3] and matrix[3] == matrix[6] and (matrix[0]== "X" or matrix[0] == "O")) or \
	(matrix[1]== matrix[4] and matrix[4] == matrix[7] and (matrix[1] == "X" or matrix[1]=="O")) or \
	(matrix[2]== matrix[5] and matrix[5] == matrix[8] and (matrix[2] == "X" or matrix[2] == "O")) : 
		return True

	#diag win
	elif (matrix[0] == matrix[4] and matrix[4] == matrix[8] and (matrix[0] == "X" or matrix[0]=="O")) or \
	(matrix[2]== matrix[4] and matrix[4] == matrix[6] and (matrix[2] == "X" or matrix[2] == "O")):
		return True

	else:
		return False



def xy_convert(x,y):
	index = x + y *3 
	return index




matrix = [0 for x in range(9)] 

print display(matrix)

choices = generate_computer_choice()


counter = 0
print ("Playing Tictactoe with computer")
while counter < 9:

	#player turn
	PlayerInputValid = False
	while PlayerInputValid == False:

		input_var = input("Player's turn. Enter grid index ")
		if input_var not in choices:
			print "Invalid input."
		elif input_var == "":
			print "Could not recognize input."
		else:
			choices.remove(int(input_var))
			PlayerInputValid = True

	matrix[int(input_var)] = "X"
	print display(matrix)
	if checkwin(matrix): 
		print ("Player wins")

		break

	
	#computer turn
	print "Computer's turn."

	chosenpos = choices[0]

	#check for computer winning move

	#print (counter)
	for choice in choices:
		#print (choice)
		#print "Here"
		matrix[choice] = "O"
		if checkwin(matrix):
			chosenpos = choice
			matrix[choice] = " "
			break
		else:
			matrix[choice] = " "

	#block player's winning move

	for choice in choices:
		matrix[choice] = "X"
		if checkwin(matrix):
			chosenpos = choice
			matrix[choice] = " "
			break
		else:
			matrix[choice] = " "
	
	
	matrix[chosenpos] = "O"
	counter += 1

	choices.remove(chosenpos)

	print display(matrix)
	if checkwin(matrix):
		print ("Computer wins")
		break

if checkwin(matrix):
	print ("Computer wins")
	

