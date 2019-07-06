# Use these constants in your code 

MIN_SHIP_SIZE = 1
MAX_SHIP_SIZE = 10
MAX_GRID_SIZE = 10
UNKNOWN = '-'
EMPTY = '.'
HIT = 'X'
MISS = 'M'


def read_ship_data(game_file):

    """ (file open for reading) -> list of list of objects

    Return a list containing the ship characters in game_file as a list 
    of strings at index 0, and ship sizes in game_file as a list of ints 
    at index 1.
    """
    ship_char = game_file.readline().split()
    ship_size = game_file.readline().split()
    size_list = []
    for num in ship_size:
        size_list.append(int(num))
    return [ship_char, size_list]



def has_ship(fleet_grid, row, column, ch_ship, size_ship):
    
    """(list of list of str, int, int, str, int) -> bool
    
    Return True iff the ship appears with the correct size, completely in a 
    row or a completely in a column at the given starting cell.
        
    >>> fleet_grid = [['a', 'a', 'a'], ['b', 'b', '.'], ['.', '.', '.']]
    >>> has_ship(fleet_grid, 0, 0, 'a', 3)
    True
    >>> has_ship(fleet_grid, 0, 0, 'a', 2)
    False
    >>> fleet_grid = [['b', 'b', '.'], ['.', 'a', 'a'], ['.', '.', '.']]
    >>> has_ship(fleet_grid, 1, 1, 'a', 2)
    True
    >>> has_ship(fleet_grid, 0, 0, 'b', 2)
    True
        
    >>> fleet_grid = [['b', 'b', 'c'], ['.', '.', 'c'], ['.', '.', 'c']]
    >>> has_ship(fleet_grid, 0, 2, 'c', 3)
    True
    >>> has_ship(fleet_grid, 0, 0, 'b', 2)
    True
        
    >>> fleet_grid = [['.', '.', '.', '.', '.'], ['a', 'b', 'd', '.', '.'], \
        ['.', '.', 'e', '.', '.'], ['c', '.', '.', '.', '.'], \
        ['c', '.', '.', '.', '.']]
    >>> has_ship(fleet_grid, 1, 0, 'a', 1)
    True
    """
    #correct size
    char_list = gather_list(fleet_grid)
    if char_list.count(ch_ship) != size_ship:
        return False
    
    #check if the size of ship is valid
    if len(fleet_grid[0]) < size_ship:
        return False
    
    size_length = len(fleet_grid[0])
    
    row_bool = True
    if column + size_ship > size_length:
        row_bool = False
    else:
        for num in range(size_ship):
            if fleet_grid[row][column + num] != ch_ship:
                row_bool = False
        
    column_bool = True
    if row + size_ship > size_length:
        row_bool = False
    else:
        for num in range(size_ship):
            if fleet_grid[row + num][column] != ch_ship:
                column_bool = False
    
    return row_bool or column_bool


#helper function 
#to gather the lists in fleet grid into one list
def gather_list(fleet_grid):
    """list of list of str -> list of str
    
    >>> fleet_grid = [['a','a','.'],['.','.','.'],['.','.','.']]
    >>> gather_list(fleet_grid)
    ['a', 'a', '.', '.', '.', '.', '.', '.', '.']
    >>> fleet_grid = [['.','.','.'],['b','.','b'],['.','.','.']]
    >>> gather_list(fleet_grid)
    ['.', '.', '.', 'b', '.', 'b', '.', '.', '.']
    """
    gather_list=[]
    for list in fleet_grid:
        for ch in list:
            gather_list.append(ch)
    return gather_list
    
    
    
def validate_character_count(fleet_grid, list_of_chship, list_of_shipsize):
    
    """(list of list of str, list of str, list of int) -> bool
    
    Return True iff the grid contains the correct number of ship characters 
    for each ship, and the correct number of EMPTY characters.
    
    >>> fleet_grid = [['a', 'a', 'b'],['.', '.', 'b'],['.', '.', 'b']]
    >>> validate_character_count(fleet_grid,['a', 'b'],[2, 3])
    True
    >>> fleet_grid = [['.', 'a', '.'],['.', 'a', '.'],['.', '.', 'a']]
    >>> validate_character_count(fleet_grid,['b'],[3])
    False
    >>> fleet_grid = [['.', 'c', '.'],['.', '.', 'b'],['.', '.', 'b']]
    >>> validate_character_count(fleet_grid,['b', 'c'],[2, 1])
    True
    >>> fleet_grid = [['.', '.', '.'],['b', '.', 'b'],['.', '.', '.']]
    >>> validate_character_count(fleet_grid,['b'],[3])
    False
    
    """
    char_list = gather_list(fleet_grid)
    size_square = (len(fleet_grid[0])) ** 2
    total = 0
    #correct number of ship characters for each ship
    for i in range(len(list_of_chship)):
        if  char_list.count(list_of_chship[i]) != list_of_shipsize[i]:
            return False
    #correct number of EMPTY characters
    for num in list_of_shipsize:
        total = total + num
    
    if char_list.count(EMPTY) != (size_square - total):
            return False
    
    return True


def validate_ship_positions(fleet_grid, list_of_chship, list_of_shipsize):
    
    """(list of list of str, list of str, list of int) -> bool
    
    Return True iff the grid contains each ship aligned completely in a 
    row or column.
    
    >>> fleet_grid = [['a', 'a', 'b'], ['.', '.', 'b'], ['.', '.', 'b']]
    >>> validate_ship_positions(fleet_grid, ['a','b'], [2,3])
    True
    >>> fleet_grid = [['.', 'a', 'a'], ['.', 'a', 'b'], ['.', '.', 'a']]
    >>> validate_ship_positions(fleet_grid, ['a', 'b'], [3, 2])
    False
    >>> fleet_grid = [['.', 'c', '.'], ['.', '.', 'b'], ['.', '.', 'b']]
    >>> validate_ship_positions(fleet_grid, ['b', 'c'], [2, 1])
    True
    >>> fleet_grid = [['.', '.', '.'], ['b', '.', 'b'], ['.', '.', '.']]
    >>> validate_ship_positions(fleet_grid, ['b'], [3])
    False
    
    """
    
    size_length = len(fleet_grid[0])
    char_list = gather_list(fleet_grid)
    
    for i in range(len(list_of_chship)):
        ch = list_of_chship[i]
        #find the index of character
        str_ch = char_list.index(ch)
        #transform the index in str into the row and column index in fleet grid
        row_index = str_ch // size_length
        column_index = str_ch % size_length
        #check each ship is consecutive in a line
        if not has_ship(fleet_grid,row_index,column_index,ch,\
                        list_of_shipsize[i]):
            return False
    return True
        
    
    
def validate_fleet_grid(fleet_grid, list_of_chship,list_of_shipsize):
    
    """(list of list of str, list of str, list of int) - > bool
    
    Return True iff the potential fleet grid is a valid fleet grid with correct 
    number of ship characters and correct number of EMPTY characters. 
    Ships are also placed in consecutive cells. 
    
    >>> fleet_grid = [['a', 'a', 'c'], ['.', '.', 'b'], ['.', '.', 'b']]
    >>> validate_fleet_grid(fleet_grid, ['a', 'b', 'c'], [2, 3, 1])
    False
    >>> fleet_grid = [['.', 'a', '.'], ['.', 'a', 'b'], ['.', '.', 'a']]
    >>> validate_fleet_grid(fleet_grid, ['a', 'b'], [2, 1])
    False
    >>> fleet_grid = [['.', 'c', '.'], ['.', '.', 'b'], ['.', '.', 'b']]
    >>> validate_fleet_grid(fleet_grid, ['b', 'c'], [2, 1])
    True
    >>> fleet_grid = [['.','.','.'], ['b','.','.'], ['.','.','.']]
    >>> validate_fleet_grid(fleet_grid, ['b'], [1])
    True

    """
    
    #correct number of ship characters and correct number of EMPTY character
    #ships are placed in consecutive cells    
    return validate_character_count(fleet_grid,list_of_chship,\
                                    list_of_shipsize) and \
           validate_ship_positions(fleet_grid,list_of_chship,list_of_shipsize)


def valid_cell(row, column, size_of_grid):
    
    """(int, int, int) -> bool
    
    Return True iff the cell is a valid cell inside a square grid of that size.
    
    >>> valid_cell(0, 1, 3)
    True
    >>> valid_cell(3, 0, 3)
    False
    >>> valid_cell(1, 1, 2)
    True
    >>> valid_cell(0, 2, 1)
    False
    """
    
    return row < size_of_grid and column < size_of_grid



def is_not_given_char(row, column, fleet_grid, ch):
    """(int, int, list of list of str, str) -> bool
    
    Return True iff the cell specified by the row and column is not the given 
    character.
    
    >>> fleet_grid = [['a', 'a', 'c'], ['.', '.', 'b'], ['.', '.', 'b']]
    >>> is_not_given_char(0, 1, fleet_grid, 'a')
    False
    >>> fleet_grid = [['.', 'c', '.'], ['.', '.', 'b'], ['.', '.', 'b']]
    >>> is_not_given_char(0, 1, fleet_grid, 'b')
    True
    >>> fleet_grid = [['.', 'a', '.'], ['.', 'a', 'b'], ['.', '.', 'a']]
    >>> is_not_given_char(1, 1, fleet_grid, 'a')
    False
    >>> fleet_grid = [['a', 'a', '.'], ['.', 'a', 'b'], ['.', '.', 'a']]
    >>> is_not_given_char(0, 0, fleet_grid, 'b')
    True
    
    """
    return fleet_grid[row][column] != ch



def update_fleet_grid(row, column, fleet_grid, list_of_chship, size, hits):
    """(int, int, list of list of str, list of str, list of int, list of int) -> 
     NoneType
     
    Call this function when there is a hit in the cell specified by the row 
    and column, then updates the fleet grid and hits list. 
    Make a call to print_sunk_message if a ship is sunk.
    
    >>> fleet_grid = [['b', 'a'], ['.', 'a']]
    >>> hits = [0, 0]
    >>> update_fleet_grid(0, 1, fleet_grid, ['a', 'b'], [2, 1], hits)
    >>> fleet_grid
    [['b', 'A'], ['.', 'a']]
    >>> hits
    [1, 0]
    >>> update_fleet_grid(1, 1, fleet_grid, ['a'], [2], hits)
    The size 2 a ship has been sunk!
    
    """

    if fleet_grid[row][column] in list_of_chship:
    #update the fleet_grid and hits
        ch = fleet_grid[row][column]
        i = list_of_chship.index(ch)
        hits[i] = hits[i] + 1
        fleet_grid[row][column] = fleet_grid[row][column].upper()
     
    #make a call to print_sunk_message if a ship is sunk
        if hits[i] == size[i]:
            print_sunk_message(size[i],list_of_chship[i])


def update_target_grid(row, column, target, fleet_grid):
    """(int, int, list of list of str, list of list of str) -> NoneType
    
    Set HIT to the cell that hits the ship, Set MISS to the cell that miss 
    hitting the ship.
    
    >>> target_grid = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    >>> fleet_grid = [['a', 'a', '.'], ['.', '.', '.'], ['.', '.', '.']]
    >>> update_target_grid(0, 0, target_grid, fleet_grid)
    >>> target_grid
    [['X', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    >>> update_target_grid(1, 0, target_grid, fleet_grid)
    >>> target_grid
    [['X', '-', '-'], ['M', '-', '-'], ['-', '-', '-']]
    >>> fleet_grid
    [['a', 'a', '.'], ['.', '.', '.'], ['.', '.', '.']]
    """
    
    if fleet_grid[row][column] == EMPTY:
        target[row][column] = MISS
    else:
        target[row][column] = HIT
        
        
def is_win(size, hits):
    """(list of int, list of int) -> bool
    
    Return True iff the number of hits for each ship in the hits list is the 
    same as the corresponding size of each ship
    
    >>> is_win([2, 2], [2, 2])
    True
    >>> is_win([1, 2], [0, 2])
    False
    >>> is_win([1, 3], [1, 3])
    True
    >>> is_win([3, 2], [2, 2])
    False
    """
    return size == hits




##################################################
## Helper function to call in update_fleet_grid
## Do not change!
##################################################

def print_sunk_message(ship_size, ship_character):
    """ (int, str) -> NoneType
  
    Print a message telling player that a ship_size ship with ship_character
    has been sunk.
    """

    print('The size {0} {1} ship has been sunk!'.format(ship_size, ship_character))
    
    
if __name__ == '__main__':
    import doctest
    
    # uncomment the line below to run the docstring examples     
    doctest.testmod()
           


    """