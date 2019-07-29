#makes a board with two dimensions of rows and columns 
def create_game_grid(rows, cols):

	grid = []
	for _ in range(rows):
		grid.append(['*'] * cols)
	return grid


#gets pieces to reurn in the boardwith the chosen column or row, and if out of range will give '*'
def get_piece(grid, row, col):

	rows = len(grid)
	cols = len(grid[0])
	
	# check the range
	if row < 0 or row >= rows:
		return '*'
	if col < 0 or col >= cols:
		return '*'
	return grid[row][col]

#accounts for getting four in a row, connected string
def get_direction_line(grid, row, col, deltaX, deltaY):

	line = []
	for _ in range(4):
		row += deltaX
		col += deltaY
		line.append(get_piece(grid, row, col))
	return ''.join(line)





#checks to see of 4 x's or o's are connected to get a win
def has_winner(grid, row, col):

	directions = [
				 (0, 1),  # right
				 (1, 1),  # right up
				 (1, 0),  # up
				 (1, -1), # left up
				 (0, -1), # left
				 (-1, -1),# left down
				 (-1, 0), # down
				 (-1, 1), # right down
				]
	
	# check each direction
	for direction in directions:
		deltaX = direction[0]
		deltaY = direction[1]
		line = get_direction_line(grid, row, col, deltaX, deltaY)
		
		# find a winner
		winner = get_line_winner(line)
		if winner != None:
			return winner
		
	return None



#checks to see if there is a winner	
def get_winner(grid):

	rows = len(grid)
	cols = len(grid[0])
	
	# check each piece
	for row in range(rows):
		for col in range(cols):
			
			# find a winner
			winner = has_winner(grid, row, col)
			if winner != None:
				return winner
	
	return None


#checks for all directions and sees if there is already four connected
def get_line_winner(line):

	if line.find('XXXX') != -1:
		return 'X'
	elif line.find('OOOO') != -1:
		return 'O'
	else:
		return None

#checks to see if the board is full	
def is_full_grid(grid):

	cols = len(grid[0])
	for col in range(0, cols):
		if not is_full_column(grid, col):
			return False
	return True
#checks to see if game os over, winner
def is_game_over(grid):

	winner = get_winner(grid)
	if winner != None:
		return True

	return is_full_grid(grid)
#displays the board
def print_game_board(grid):

	rows = len(grid)
	cols = len(grid[0])

	for row in range(rows - 1, -1, -1):
		print(row, end = "")
		print(' ', end = "")
		for col in range(cols):
			print('%s ' % grid[row][col], end = "")
		print()

	print('  ', end = "")
	for col in range(cols):
		print('%d ' % (col), end = "")

	print()

#checks to see if piece is empty
def is_empty_piece(grid, row, col):

	return grid[row][col] == '*'



#finds a row that works so it canmove
def find_the_top_row(grid, col):

	rows = len(grid)
	for row in range(0, rows):
		# the piece is empty, it is can be moved
		if is_empty_piece(grid, row, col):
			break
	else:
		# not found
		row = -1

	return row




#checks if column is full
def is_full_column(grid, col):

	return find_the_top_row(grid, col) == -1


#moves the piece where it was asked to
def grid_move(grid, col, curr_player):

	row = find_the_top_row(grid, col)
	if row == -1:
		return
	grid[row][col] = curr_player

#asks user for the move	
def select_move_column(curr_player, grid):

	cols = len(grid[0])
	while True:
		try:
			col = input('%s please enter a move: ' % curr_player)
			col = int(col)
			if col >= 0 and col < cols and not is_full_column(grid, col):
				return col
		except:
			pass

if __name__ == "__main__":

	# create game grid
	rows = 6
	cols = 7
	grid = create_game_grid(rows, cols)

	player1 = 'X'
	player2 = 'O'

	curr_player = player1

	print()
	while not is_game_over(grid):
		
		# print game board
		print_game_board(grid)
		print()

		# user to enter the column to be moved
		col = select_move_column(curr_player, grid)
		
		# make move
		grid_move(grid, col, curr_player)

		# take turn player
		curr_player = player2 if curr_player == player1 else player1

	# game is over, print game board
	print_game_board(grid)
	print()
	
	# check winner
	winner = get_winner(grid)
	if winner != None:
		print('%s won the game.' % winner)
	else:
		print('The game ended in a tie.')
