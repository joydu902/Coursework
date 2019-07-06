"""
The BattleQueue class for A1.

A BattleQueue is a queue that lets our game know in what order various 
characters are going to attack. The method headers and descriptions have all 
been provided for you, but the implementation will depend on you.

You must replace the 'Any's in the type annotations as well as add in
the constructors for the docstring examples.
"""
# TODO: In the type annotations, replace Any with the appropriate types.
# To put a class name without importing it, just wrap the name in ''s.
# For example:
# add(self, character: 'Something') -> None:
#
# If there are multiple return types, import Union and use that. For example:
# Union[str, bool]

from typing import Union

class BattleQueue:
    """
    A class representing a BattleQueue.
    """
    
    def __init__(self) -> None:
        """
        Initialize this BattleQueue.
        
        >>> bq = BattleQueue()
        >>> bq.is_empty()
        True
        """
        self._content = []
    
    def add(self, character: 'Character') -> None:
        """
        Add character to this BattleQueue.
        
        >>> bq = BattleQueue()
        >>> from a1_playstyle import ManualPlaystyle
        >>> ps = ManualPlaystyle(bq)
        >>> from a1_character import *
        >>> c = Mage('Sophia', bq, ps)
        >>> bq.add(c)
        >>> bq.is_empty()
        False
        """
        self._content.append(character)
    
    def remove(self) -> 'Character':
        """
        Remove and return the character at the front of this BattleQueue.
        
        >>> bq = BattleQueue()
        >>> from a1_playstyle import ManualPlaystyle
        >>> ps = ManualPlaystyle(bq)
        >>> from a1_character import *
        >>> c = Rogue('Sophia', bq, ps)
        >>> bq.add(c)
        >>> bq.remove()
        Sophia (Rogue): 100/100
        >>> bq.is_empty()
        True
        """
        removed_item = self.peek()
        if removed_item:
            self._content.remove(removed_item)
        return removed_item
    
    def is_empty(self) -> bool:
        """
        Return whether this BattleQueue is empty (i.e. has no players or
        has no players that can perform any actions).
        
        >>> bq = BattleQueue()
        >>> bq.is_empty()
        True
        """
        if self.peek():
            return False
        return True

    def peek(self) -> 'Character':
        """
        Return the character at the front of this BattleQueue but does not
        remove them.
        
        >>> bq = BattleQueue()
        >>> from a1_playstyle import ManualPlaystyle
        >>> ps = ManualPlaystyle(bq)
        >>> from a1_character import *
        >>> c = Rogue('Sophia', bq, ps)
        >>> bq.add(c)
        >>> bq.peek()
        Sophia (Rogue): 100/100
        >>> bq.is_empty()
        False
        """
        for chara in self._content:
            if chara.get_available_actions():
                return chara
        return None

    def is_over(self) -> bool:
        """
        Return whether the game being carried out in this BattleQueue is over 
        or not.
        
        A game is considered over if:
            - Both players have no skills that they can use.
            - One player has 0 HP
            or
            - The BattleQueue is empty.
            
        >>> bq = BattleQueue()
        >>> bq.is_over()
        True
        
        >>> from a1_playstyle import ManualPlaystyle
        >>> ps = ManualPlaystyle(bq)
        >>> from a1_character import *
        >>> c = Rogue('Sophia', bq, ps)
        >>> bq.add(c)
        >>> bq.is_over()
        False
        """
        # Return True if the BattleQueue is empty.
        if self.is_empty():
            return True

        # Return True if One player has 0 HP.
        for chara in self._content:
            if chara.get_hp() == 0:
                return True

        # Return True if Both players have no skills that they can use.
        for chara in self._content:
            if chara.get_available_actions():
                return False
        return True

    def get_winner(self) -> Union['Character', None]:
        """
        Return the winner of the game being carried out in this BattleQueue
        if the game is over. If the game is not over or if there is no winner
        (i.e. there's a tie), return None.
        
        >>> bq = BattleQueue()
        >>> bq.get_winner()
        """
        loser, winner = None, None
        if self.is_over():
            for chara in self._content:
                if chara.get_hp() > 0:
                    winner = chara
                else:
                    loser = chara
            # if winner and loser both exist
            if winner and loser:
                return winner
        return None


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='a1_pyta.txt')
