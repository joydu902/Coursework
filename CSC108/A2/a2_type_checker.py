import builtins

# Check for use of functions print and input.

our_print = print
our_input = input

def disable_print(*args):
    raise Exception("You must not call print anywhere in your functions!")

def disable_input(*args):
    raise Exception("You must not call input anywhere in your functions!")

builtins.print = disable_print
builtins.input = disable_input

import battleship_functions as bf

def is_grid(lst):
    """ (object) -> bool
    
    Return True iff lst is a list of list of str.
    
    >>> is_grid([['a', 'b', 'c']])
    True
    """
    
    if not isinstance(lst, list):
        return False
        
    for element in lst:
        if not isinstance(element, list):
            return False
        for s in element:
            if not isinstance(s, str):
                return False
    return True
    

# Get the initial value of the constants
constants_before = [1, 10, '-', '.', 'X', 'M']

# Type check bf.read_ship_data
import io
game_file = io.StringIO('t\n1\nt')
result = bf.read_ship_data(game_file)
assert isinstance(result, list), \
       '''bf.read_ship_data should return a list, but returned {0}
       .'''.format(type(result))
assert isinstance(result[0][0], str), \
       '''bf.read_ship_data should return a list where the first element 
       is a list of str, but the first element is a list of {0}
       .'''.format(type(result[0][0]))
assert isinstance(result[1][0], int), \
       '''bf.read_ship_data should return a list where the second element 
       is a list of int, but the second element is a list of {0}
       .'''.format(type(result[1][0]))

# Type check bf.has_ship
fleet_grid = [['a', 'a', 'a'], ['b', 'b', '.'], ['.', '.', '.']]
result = bf.has_ship(fleet_grid, 0, 0, 'a', 3)
assert isinstance(result, bool), \
       '''bf.has_ship should return a bool, but returned {0}
       .'''.format(type(result))

# Type check bf.validate_character_count
fleet_grid = [['a', 'a', 'a'], ['b', 'b', '.'], ['.', '.', '.']]
ships = ['a', 'b']
sizes = [3, 2]
result = bf.validate_character_count(fleet_grid, ships, sizes)
assert isinstance(result, bool), \
       '''bf.validate_character_count should return a bool, but returned {0}
       .'''.format(type(result))

# Type check bf.validate_ship_positions
fleet_grid = [['a', 'a', 'a'], ['b', 'b', '.'], ['.', '.', '.']]
ships = ['a', 'b']
sizes = [3, 2]
result = bf.validate_ship_positions(fleet_grid, ships, sizes)
assert isinstance(result, bool), \
       '''bf.validate_ship_positions should return a bool, but returned {0}
       .'''.format(type(result))

# Type check bf.validate_fleet_grid
fleet_grid = [['a', 'a', 'a'], ['b', 'b', '.'], ['.', '.', '.']]
ships = ['a', 'b']
sizes = [3, 2]
result = bf.validate_fleet_grid(fleet_grid, ships, sizes)
assert isinstance(result, bool), \
       '''bf.validate_fleet_grid should return a bool, but returned {0}
       .'''.format(type(result))

# Type check bf.valid_cell
result = bf.valid_cell(1, 1, 3)
assert isinstance(result, bool), \
       '''bf.valid_cell should return a bool, but returned {0}
       .'''.format(type(result))

# Type check bf.is_not_given_char
result = bf.is_not_given_char(1, 1, [['a','-'], ['-','b']], '-')
assert isinstance(result, bool), \
       '''bf.is_not_given_char should return a bool, but returned {0}
       .'''.format(type(result))

# Type check bf.update_fleet_grid
result = bf.update_fleet_grid(0, 1, [['.', 'a'], ['.', 'a']], ['a'], [2], [0])
assert result is None, \
       '''bf.update_fleet_grid should return None, but returned {0}
       .'''.format(type(result))

# Type check bf.update_target_grid
target_grid = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
fleet_grid = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
result = bf.update_target_grid(0, 0, target_grid, fleet_grid)
assert result is None, \
       '''bf.update_target_grid should return None, but returned {0}
       .'''.format(type(result))

# Type check bf.is_win
result = bf.is_win([1, 2, 3], [1, 2, 3])
assert isinstance(result, bool), \
       '''bf.is_win should return a bool, but returned {0}
       .'''.format(type(result))


# Get the final values of the constants
constants_after = [bf.MIN_SHIP_SIZE, bf.MAX_SHIP_SIZE, bf.UNKNOWN, bf.EMPTY, bf.HIT, bf.MISS]


# Check whether the constants are unchanged.
assert constants_before == constants_after, \
       '''Your function(s) modified the value of one or more constants.
       Edit your code so that the value of the constants are not 
       changed by your functions.'''
    

builtins.print = our_print
builtins.input = our_input    

print("""

The type checker passed.

This means that your functions in battleship_functions.py:
- are named correctly,
- take the correct number of arguments, and
- return the correct types.  

This does NOT mean that the functions are correct!

Be sure to thoroughly test your functions yourself before submitting.""")

