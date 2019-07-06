from battleship_functions import *
import random

def generate_fleet_grid(grid_size, ships, sizes):
    """ (int, list of str, list of int) -> list of list of str

    Return a new grid_size by grid_size fleet grid with the ship symbols
    in ships and ship sizes in sizes placed randomly on the fleet grid, either
    horizontally or vertically, and the rest of the cells EMPTY.
    """
    
    grid = make_empty_grid(grid_size)
    
    for index in range(len(ships) - 1, -1, -1):
        # get the ship symbol and its size
        placed = False
        ship = ships[index]
        ship_size = sizes[index]

        while not placed:
            placed = randomly_place_ship(grid, ship, ship_size)         
        
    return grid


def make_empty_grid(grid_size):
    """ (int) -> list of list of str
    
    Return a grid_size by grid_size grid containing EMPTY in every cell.
    """
    
    grid = []
    for row in range(grid_size):
        grid.append([])
        for column in range(grid_size):
            grid[row].append(EMPTY) 
    return grid

def randomly_place_ship(grid, ship, ship_size):
    """ (list of list of str, str, int) -> bool
    
    Return True iff a random attempt to place ship with ship_size in grid
    was successful.
    """
    
    grid_size = len(grid)
    
    # randomly generate a location at which to place the ship
    start_row = random.randint(0, grid_size - 1)
    start_col = random.randint(0, grid_size - 1)
    
    ends = get_end_coordinates(start_row, start_col, ship_size)
    end_row = ends[0]
    end_col = ends[1]
    
    # If the start and end locations are within the bounds of the grid
    # and the cells are not occupied, place the ship.
    if valid_cell(start_row, start_col, grid_size) and \
       valid_cell(end_row, end_col, grid_size) and \
       not is_occupied(start_row, start_col, end_row, end_col, grid):
        place_ship(start_row, start_col, end_row, end_col, grid, ship)
        return True
    return False
        

def get_end_coordinates(start_row, start_col, ship_size):
    """ (int, int, int) -> list of int
    
    Return the end row and end column based on start_row, start_col, and 
    ship_size, for a randomly generated direction.
    """
    
    # randomly determine whether to place horizontally or vertically
    direction = random.randint(0, 1)
    
    if direction == 0:
        # calculate the (row, col) coordinates for horizontal placement
        end_row = start_row
        end_col = start_col + ship_size - 1
    else:
        # calculate the (row, col) coordinates for vertical placement
        end_row = start_row + ship_size - 1
        end_col = start_col
    return [end_row, end_col]


def place_ship(row1, col1, row2, col2, fleet_grid, ship_symbol):
    """ (int, int, int, int, list of list of str, str) -> NoneType

    Pre-condition: len(ship_symbol) == 1

    Place the ship ship_symbol on the grid from (row1, col1) to 
    (row2, col2), inclusive.

    >>> grid = [[EMPTY,EMPTY,EMPTY], [EMPTY,EMPTY,EMPTY], [EMPTY,EMPTY,EMPTY]]
    >>> place_ship(0, 0, 1, 0, grid, 'd')
    >>> grid 
    [['d', '.', '.'], ['d', '.', '.'], ['.', '.', '.']]
    >>> place_ship(0, 1, 0, 2, grid, 'z')
    >>> grid 
    [['d', 'z', 'z'], ['d', '.', '.'], ['.', '.', '.']]
    """

    if row1 == row2:
        # place the ship horizontally
        for col in range(col1, col2 + 1):
            fleet_grid[row1][col] = ship_symbol
    else:
        # place the ship vertically
        for row in range(row1, row2 + 1):
            fleet_grid[row][col1] = ship_symbol
            

def is_occupied(row1, col1, row2, col2, fleet_grid):
    """ (int, int, int, int, list of list of str) -> bool

    Return True if the cells between (row1, col1) and (row2, col2), inclusive, 
    are not all empty, and return False otherwise.
    
    >>> grid = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    >>> is_occupied(1, 1, 2, 2, grid)
    False
    >>> grid = [['.', '.', '.'], ['.', 'a', '.'], ['.', '.', '.']]
    >>> is_occupied(1, 1, 2, 2, grid)
    True
    """

    occupied = False
    
    if col1 == col2:
        for row in range(min(row1, row2), max(row1, row2) + 1):
            if fleet_grid[row][col1] != EMPTY:
                occupied = True
    else:
        for col in range(min(col1, col2), max(col1, col2) + 1):
            if fleet_grid[row1][col] != EMPTY:
                occupied = True
    
    return occupied

def make_computer_move(target_grid):
    """ (list of list of str) -> list of int
    
    Return the randomly generated row and column of the computer's next move.
    """
    
    grid_size = len(target_grid)

    row = random.randint(0, grid_size - 1)    
    col = random.randint(0, grid_size - 1)
    
    while is_not_given_char(row, col, target_grid, UNKNOWN):
        row = random.randint(0, grid_size - 1)    
        col = random.randint(0, grid_size - 1)

    return [row, col]

