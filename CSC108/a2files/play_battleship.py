import os
import battleship_functions as bf

# This code won't work until you've completed your functions in the
# battleship_functions module. 
# All functions called in here of the form bf.function_name are ones
# that you will write.

# ========= Some functions that are called to play the game follow. ======
# ========= You may find it helpful to read and understand all of   ======
# ========= the code below these lines.  Do NOT change any of it!   ======


# These functions read the game file
def read_game_file():
    """ () -> list of list of objects
    
    Return the ship and symbol grid data from a game file provided by the user.
    """
    filename = get_valid_filename('Game filename: ')
    game_file = open(filename)
    ships_data = bf.read_ship_data(game_file)
    ships = ships_data[0]
    sizes = ships_data[1]
    fleet_grid = read_fleet_grid(game_file)
    game_file.close()
    return [ships, sizes, fleet_grid]


def get_valid_filename(msg):
    """ (str) -> str
    
    Return the name of a valid file entered by the user when prompted with msg.
    This file should exist in the same directory as this file. Keep prompting
    the user until a valid filename is entered.
    """
    
    filename = input(msg)
    while not os.path.exists(filename):
        print('That file does not exist.')
        filename = input(msg)

    return filename


def read_fleet_grid(game_file):
    """ (file open for reading) -> list of list of str

    Return the fleet grid that is found in game_file.
    """
   
    grid = []
   
    for line in game_file:
        line = line.strip()
        sublist = []
        for char in line:
            sublist.append(char)
        grid.append(sublist)

    return grid


# These functions validate the game
def is_valid_game(fleet_grid, ships, sizes):
    """ (list of list of str, list of str, list of int) -> bool
    
    Return True iff the game parameters fleet_grid, ships, and sizes are 
    valid, and fleet_grid is a valid game.
    
    >>> grid = [['.','b','.'], ['.','b','.'], ['a','a','a']]
    >>> ships = ['a', 'b']
    >>> sizes = [3, 2]
    >>> is_valid_game(grid, ships, sizes)
    True
    >>> grid = [['b','.','.'], ['.','b','.'], ['a','a','a']]
    >>> ships = ['a', 'b']
    >>> sizes = [3, 2]
    >>> is_valid_game(grid, ships, sizes)
    False
    """
    return validate_game_parameters(fleet_grid, ships, sizes) and \
           bf.validate_fleet_grid(fleet_grid, ships, sizes)   


def validate_game_parameters(grid, ships, sizes):
    """ (list of list of str, list of str, list of int) -> bool

    Return True if and only if grid is square with at least one cell and at
    most MAX_GRID_SIZE cells per row, the number of ship characters in ships is 
    the same as the number of ships in sizes, that there is at least one ship, 
    all ships have a valid size, and all ships have a valid, unique character
    label.

    >>> grid = [['.','b','.'], ['.','b','.'], ['a','a','a']]
    >>> ships = ['a', 'b']
    >>> sizes = [3, 2]
    >>> validate_game_parameters(grid, ships, sizes)
    True
    >>> grid = []
    >>> ships = ['a', 'd', 'h', 'i', 'n']
    >>> sizes = [1, 1, 1, 2, 1]
    >>> validate_game_parameters(grid, ships, sizes)
    False
    """

    # Confirm that the grid has a valid number of rows.
    if len(grid) == 0 or len(grid) > bf.MAX_GRID_SIZE:
        return False
    
    # Confirm that the grid is square.
    for row in range(len(grid)):
        if len(grid[row]) != len(grid):
            return False

    # Confirm that number of ships is the same as the number of ship sizes.
    if len(ships) != len(sizes):
        return False

    # Confirm that the ships and sizes lists are not empty.
    if len(ships) == 0:
        return False

    # Confirm that each ship has a valid size.
    for i in range(len(sizes)):
        if sizes[i] < bf.MIN_SHIP_SIZE or sizes[i] > bf.MAX_SHIP_SIZE:
            return False

    # Confirm that each ship has a valid unique character label.
    for i in range(len(ships)):
        if len(ships[i]) > 1:
            return False
        else:
            for j in range(len(ships)):
                if i != j and ships[i] == ships[j]:
                    return False

    return True 


# These functions set up and display the game
def get_target_grid(grid_size):
    """ (int) -> list of list of str

    Return a grid_size by grid_size grid of UNKNOWN characters.
    
    >>> get_target_grid(2)
    [['-', '-'], ['-', '-']]
    >>> get_target_grid(3)
    [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    """
    
    target_grid = []
    for i in range(grid_size):
        target_grid.append([])
        for j in range(grid_size):
            target_grid[i].append(bf.UNKNOWN)
            
    return target_grid


def display_grids(target_grid, fleet_grid):
    """ (list of list of str, list of list of str) -> NoneType

    Display the target_grid and the fleet_grid that belong to a player.
    """

    print('\nMy target grid.               My fleet grid.\n')
    gap_between_grids = ' ' * (28 - len(target_grid))
    
    # Display the column numbers
    print(' ', end='')
    for col in range(len(target_grid)):
        print(col, end='')
    print(gap_between_grids + ' ', end='')
    for col in range(len(target_grid)):
        print(col, end='')
    print()

    # Display row numbers and cell contents.
    for row in range(len(target_grid)):
        print(row, end='')
        for col in range(len(target_grid)):
            print(target_grid[row][col], end='')
        print(gap_between_grids + str(row), end='')
        for col in range(len(fleet_grid)):
            print(fleet_grid[row][col], end='')
        print()

    print()
    print(' ' + bf.HIT + ' means hit,                Upper-case means hit.')
    print(' ' + bf.MISS + ' means miss.')  


# These functions help play the game by getting and making moves    
def get_valid_player_move(target_grid):
    """ (list of list of str) -> list of int
    
    Return a two item list that contains the player's move.
    """  
    
    grid_size = len(target_grid)
    
    # Get initial move
    row = input('Please enter the row: ')
    col = input('Please enter the column: ')
    if row.isdigit() and col.isdigit():
        row = int(row)
        col = int(col)
    else:
        row = -1
        col = -1
    
    # Keep asking until user enters valid move
    while (not bf.valid_cell(row, col, grid_size) or 
                bf.is_not_given_char(row, col, target_grid, bf.UNKNOWN)): 
        print('Invalid move!\n')
    
        new_row = input('Please enter the row: ')
        new_col = input('Please enter the column: ')
        if new_row.isdigit() and new_col.isdigit():
            row = int(new_row)
            col = int(new_col)
    
    return [row, col] 

    
def make_move(row, col, fleet_grid, ships, sizes, hits_list, target_grid):
    """ (int, int, list of list of str, list of str, list of int, 
                                 list of int, list of list of str) -> str
    
    Return 'hit a ship' and update hits_list and fleet_grid, using ships and
    sizes, if there is a ship at row and col, or return 'missed' if there is
    no ship at row and col. Update target_grid in both cases.

    >>> hits_list = [0]   
    >>> fleet_grid = [['.', 'a'], ['.', 'a']]
    >>> target_grid = [['-', '-'], ['-', '-']]
    >>> make_move(0, 0, fleet_grid, ['a'], [2], hits_list, target_grid)
    'missed'
    >>> hits_list
    [0]
    >>> fleet_grid 
    [['.', 'a'], ['.', 'a']]
    >>> target_grid 
    [['M', '-'], ['-', '-']]
    >>> make_move(0, 1, fleet_grid, ['a'], [2], hits_list, target_grid)
    'hit a ship'
    >>> hits_list
    [1]
    >>> fleet_grid 
    [['.', 'A'], ['.', 'a']]
    >>> target_grid 
    [['M', 'X'], ['-', '-']]
    """
    
    if bf.is_not_given_char(row, col, fleet_grid, bf.EMPTY):
        bf.update_fleet_grid(row, col, fleet_grid, ships, sizes, hits_list) 
        bf.update_target_grid(row, col, target_grid, fleet_grid)
        return 'hit a ship'
    else:
        bf.update_target_grid(row, col, target_grid, fleet_grid)
        return 'missed'
    

def get_num_moves(target_grid):
    """ (list of list of str) -> int

    Return the number of moves made so far for the board target_grid, based on
    the number of non-UNKNOWN elements.
    
    >>> get_num_moves([['-', '-'], ['-', '-']])
    0
    >>> get_num_moves([['-', 'M'], ['X', '-']])
    2
    """

    count_moves = 0
    
    for row in target_grid:
        for symbol in row:
            if symbol != bf.UNKNOWN:
                count_moves += 1
    
    return count_moves


# These are two different functions to play either a single player game,
# or a game versus a computer opponent                
def play_single_player():
    """ () -> NoneType

    A single player game with no opponent. This may be used for the purpose
    of testing our functions.
    """
    
    # Read the game file
    ships, sizes, fleet_grid = read_game_file()

    # Make sure the game is valid
    if not is_valid_game(fleet_grid, ships, sizes):
        print('The supplied game is not valid.  Game exiting.')
        return
    
    # Set up the game
    target_grid = get_target_grid(len(fleet_grid))
    display_grids(target_grid, fleet_grid)
    hits_list = [0] * len(sizes)

    # Play the game until it's over
    while not bf.is_win(sizes, hits_list):
        
        print('\nTake a turn.')
        [row, col] = get_valid_player_move(target_grid) 
        print()
        
        message = make_move(row, col, fleet_grid, ships, 
                            sizes, hits_list, target_grid)
        print('You {0}!'.format(message))        
        display_grids(target_grid, fleet_grid)
        
    # Game is over, display results
    print('\nYou won in {0} move(s)!'.format(get_num_moves(target_grid)))


def play_versus_computer():
    """ () -> NoneType

    A two player game with computer opponent.
    """
    
    # Read the game file    
    ships, sizes, fleet_grid_player = read_game_file()
    
    # Make sure the game is valid
    if not is_valid_game(fleet_grid_player, ships, sizes):
        print('The supplied game is not valid.  Game exiting.')
        return
    
    # Set up the game
    # Need view and fleet grid for player and computer, and flag to take turns
    grid_size = len(fleet_grid_player)
    target_grid_player = get_target_grid(grid_size)
    hits_player = [0] * len(sizes)
    fleet_grid_computer = cf.generate_fleet_grid(grid_size, ships, sizes)
    target_grid_computer = get_target_grid(grid_size)
    hits_computer = [0] * len(sizes)
    player_turn = True
    
    # Play the game until it's over
    while not bf.is_win(sizes, hits_player) and \
          not bf.is_win(sizes, hits_computer):
        
        print('\n\n\n' + ':' * 40 + '\n')
        if player_turn:        
            fleet_grid = fleet_grid_computer
            target_grid = target_grid_player
            display_grids(target_grid_player, fleet_grid_player)
            print('Your turn.')
            [row, col] = get_valid_player_move(target_grid_player)
            hits_list = hits_player
        else:
            fleet_grid = fleet_grid_player
            target_grid = target_grid_computer
            display_grids(target_grid_player, fleet_grid_player)
            [row, col] = cf.make_computer_move(target_grid)
            hits_list = hits_computer
                    
        print()
        
        message = '{0} {1}!'
        result = make_move(row, col, fleet_grid, ships, 
                           sizes, hits_list, target_grid)
        if player_turn:
            message = message.format('You', result)
        else:
            message = message.format('Computer', result)
        print(message)
                
        display_grids(target_grid_player, fleet_grid_player)
        input('Press enter.\n')
        player_turn = not player_turn
    
    # Game is over, display results    
    print()
    if bf.is_win(sizes, hits_player):
        print('You won in {0} move(s)!'.format(
            get_num_moves(target_grid_player)))
    else:
        print('The computer won in {0} move(s).  Please try again.'.format(
            get_num_moves(target_grid_computer)))
    
if __name__ == '__main__':
    # uncomment these two lines to run the docstring examples
    #import doctest
    #doctest.testmod()
       
    # set play_computer to True to play against the computer
    # set play_computer to False to play single-player
    play_computer = False
    if play_computer:
        import computer_functions as cf
        play_versus_computer()
    else:
        play_single_player()
