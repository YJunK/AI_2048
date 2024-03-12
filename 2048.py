# 2048.py
# importing the logic.py file
# where we have written all the
# logic functions used.
import logic
from Play_2048 import AI_move										# added to import the Play_2048 file - the brige for the game and the AI

# Driver code
if __name__ == '__main__':
	
# calling start_game function
# to initialize the matrix
	mat = logic.start_game()												

while(True):
	# taking the user input
	# for next step
	#x = input("Press the command : ")
	x = AI_move(mat)  									# added to get the move from the AI, and sending the current mat to the AI

	mat_old = mat										# added to store the old matrix before the move

	# we have to move up
	if(x == 'W' or x == 'w'):
		# call the move_up function
		mat, flag = logic.move_up(mat)

		# check validity of move:						# added to check if the move was valid
		if mat == mat_old:
			print("Invalid Move")						# added to print that the move was invalid
			continue
		else:
			pass

		# get the current state and print it
		status = logic.get_current_state(mat)
		print(status)

		# if game not over then continue
		# and add a new two
		if(status == 'GAME NOT OVER'):
			logic.add_new(mat)

		# else break the loop 
		else:
			break

	# the above process will be followed
	# in case of each type of move
	# below

	# to move down
	elif(x == 'S' or x == 's'):
		mat, flag = logic.move_down(mat)

		# check validity of move:						# added to check if the move was valid
		if mat == mat_old:
			print("Invalid Move")						# added to print that the move was invalid
			continue
		else:
			pass

		status = logic.get_current_state(mat)
		print(status)
		if(status == 'GAME NOT OVER'):
			logic.add_new(mat)
		else:
			break

	# to move left
	elif(x == 'A' or x == 'a'):
		mat, flag = logic.move_left(mat)

		# check validity of move:						# added to check if the move was valid
		if mat == mat_old:
			print("Invalid Move")						# added to print that the move was invalid
			continue
		else:
			pass

		status = logic.get_current_state(mat)
		print(status)
		if(status == 'GAME NOT OVER'):
			logic.add_new(mat)
		else:
			break

	# to move right
	elif(x == 'D' or x == 'd'):
		mat, flag = logic.move_right(mat)

		# check validity of move:						# added to check if the move was valid
		if mat == mat_old:
			print("Invalid Move")						# added to print that the move was invalid
			continue
		else:
			pass

		status = logic.get_current_state(mat)
		print(status)
		if(status == 'GAME NOT OVER'):
			logic.add_new(mat)
		else:
			break
	else:
		print("Invalid Key Pressed")

	# print the matrix after each
	# move.
	for row in mat:										# changed from print(mat) to the for loop seen
		print(row)