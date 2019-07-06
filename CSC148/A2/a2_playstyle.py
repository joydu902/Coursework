"""
The Playstyle classes for A2.
Docstring examples are not required for Playstyles.

You are responsible for implementing the get_state_score function, as well as
creating classes for both Iterative Minimax and Recursive Minimax.
"""
from typing import Any
import random
from a2_state_stack import StateStack

class Playstyle:
    """
    The Playstyle superclass.
    
    is_manual - Whether the class is a manual Playstyle or not.
    battle_queue - The BattleQueue corresponding to the game this Playstyle is
                   being used in.
    """
    is_manual: bool
    battle_queue: 'BattleQueue'
    
    def __init__(self, battle_queue: 'BattleQueue') -> None:
        """
        Initialize this Playstyle with BattleQueue as its battle queue.
        """
        self.battle_queue = battle_queue
        self.is_manual = True
    
    def select_attack(self, parameter: Any = None) -> str:
        """
        Return the attack for the next character in this Playstyle's
        battle_queue to perform.
        
        Return 'X' if a valid move cannot be found.
        """
        raise NotImplementedError
    
    def copy(self, new_battle_queue: 'BattleQueue') -> 'Playstyle':
        """
        Return a copy of this Playstyle which uses the BattleQueue 
        new_battle_queue.
        """
        raise NotImplementedError

class ManualPlaystyle(Playstyle):
    """
    The ManualPlaystyle. Inherits from Playstyle.
    """
    
    def select_attack(self, parameter: Any = None) -> str:
        """
        Return the attack for the next character in this Playstyle's
        battle_queue to perform.
        
        parameter represents a key pressed by a player.

        Return 'X' if a valid move cannot be found.
        """
        if parameter in ['A', 'S']:
            return parameter

        return 'X'
    
    def copy(self, new_battle_queue: 'BattleQueue') -> 'Playstyle':
        """
        Return a copy of this ManualPlaystyle which uses the 
        BattleQueue new_battle_queue.
        """
        return ManualPlaystyle(new_battle_queue)

class RandomPlaystyle(Playstyle):
    """
    The Random playstyle. Inherits from Playstyle.
    """
    def __init__(self, battle_queue: 'BattleQueue') -> None:
        """
        Initialize this RandomPlaystyle with BattleQueue as its battle queue.
        """
        super().__init__(battle_queue)
        self.is_manual = False
    
    def select_attack(self, parameter: Any = None) -> str:
        """
        Return the attack for the next character in this Playstyle's
        battle_queue to perform.

        Return 'X' if a valid move cannot be found.
        """
        actions = self.battle_queue.peek().get_available_actions()
        
        if not actions:
            return 'X'
        
        return random.choice(actions)
    
    def copy(self, new_battle_queue: 'BattleQueue') -> 'Playstyle':
        """
        Return a copy of this RandomPlaystyle which uses the 
        BattleQueue new_battle_queue.
        """
        return RandomPlaystyle(new_battle_queue)


def get_state_score(battle_queue: 'BattleQueue') -> int:
    """
    Return an int corresponding to the highest score that the next player in
    battle_queue can guarantee.

    For a state that's over, the score is the HP of the character who still has
    HP if the next player who was supposed to act is the winner. If the next
    player who was supposed to act is the loser, then the score is -1 * the
    HP of the character who still has HP. If there is no winner (i.e. there's
    a tie) then the score is 0.

    >>> from a2_battle_queue import BattleQueue
    >>> from a2_characters import Rogue, Mage
    >>> bq = BattleQueue()
    >>> r = Rogue("r", bq, ManualPlaystyle(bq))
    >>> m = Mage("m", bq, ManualPlaystyle(bq))
    >>> r.enemy = m
    >>> m.enemy = r
    >>> bq.add(r)
    >>> bq.add(m)
    >>> m.set_hp(3)
    >>> get_state_score(bq)
    100
    >>> r.set_hp(40)
    >>> print(bq)
    r (Rogue): 40/100 -> m (Mage): 3/100
    >>> get_state_score(bq)
    40
    >>> bq.remove()
    r (Rogue): 40/100
    >>> bq.add(r)
    >>> get_state_score(bq)
    -10
    """
    if battle_queue.is_over():
        return get_score_when_is_over(battle_queue)
    else:
        score_1, score_2 = None, None
        curr_player = battle_queue.peek()
        actions = curr_player.get_available_actions()
        bq1, bq2 = battle_queue.copy(), battle_queue.copy()
        curr_player1, curr_player2 = bq1.remove(), bq2.remove()

        if 'A' in actions:
            curr_player1.attack()
            score_1 = get_state_score(bq1)
        if 'S' in actions:
            curr_player2.special_attack()
            score_2 = get_state_score(bq2)

        max_ = True if curr_player1.get_name() == bq1.peek().get_name() else False
        if max_:
            if score_1 and score_2:
                return max(score_1, score_2)
            else:
                return score_1 if score_1 else score_2 if score_2 else None
        else:
            if score_1 and score_2:
                return -min(score_1, score_2)
            else:
                return -score_1 if score_1 else -score_2 if score_2 else None


def get_state_score_iterative(battle_queue: 'BattleQueue') -> int:
    """
    Same as get_state_score but without recursion.

    >>> from a2_battle_queue import BattleQueue
    >>> from a2_characters import Rogue, Mage
    >>> bq = BattleQueue()
    >>> r = Rogue("r", bq, ManualPlaystyle(bq))
    >>> m = Mage("m", bq, ManualPlaystyle(bq))
    >>> r.enemy = m
    >>> m.enemy = r
    >>> bq.add(r)
    >>> bq.add(m)
    >>> m.set_hp(3)
    >>> get_state_score_iterative(bq)
    100
    >>> r.set_hp(40)
    >>> print(bq)
    r (Rogue): 40/100 -> m (Mage): 3/100
    >>> get_state_score_iterative(bq)
    40
    >>> bq.remove()
    r (Rogue): 40/100
    >>> bq.add(r)
    >>> get_state_score_iterative(bq)
    -10
    """
    if battle_queue.is_over():
        return get_score_when_is_over(battle_queue)

    s = StateStack()
    count = 1
    parent_state = State(1, battle_queue.copy())
    s.add(parent_state)

    while not s.is_empty():
        parent_state = s.remove()
        battle_queue = parent_state.bq

        if battle_queue.is_over():
            score = get_score_when_is_over(battle_queue)
            parent_state.score = score
        elif parent_state.children:
            scores = [child.score for child in parent_state.children if child.score]
            score = None
            max_ = True if battle_queue.peek().get_name() == parent_state.children[0].bq.peek().get_name() else False
            if scores:
                if max_:
                    score = max(scores)
                else:
                    score = -min(scores)
            parent_state.score = score
        else:
            s.add(parent_state)
            curr_player = battle_queue.peek()
            actions = curr_player.get_available_actions()
            if 'A' in actions:
                bq1 = battle_queue.copy()
                curr_player1 = bq1.remove()
                curr_player1.attack()
                count += 1
                child_state1 = State(count, bq1)
                parent_state.children.append(child_state1)
                s.add(child_state1)

            if 'S' in actions:
                bq2 = battle_queue.copy()
                curr_player2 = bq2.remove()
                curr_player2.special_attack()
                count += 1
                child_state2 = State(count, bq2)
                parent_state.children.append(child_state2)
                s.add(child_state2)

    return parent_state.score


def get_score_when_is_over(battle_queue):
    """
    Return the score when game is over.

    """
    curr_player = battle_queue.peek()
    winner = battle_queue.get_winner()
    if winner is None:
        return 0
    elif winner.get_name() == curr_player.get_name():
        return winner.get_hp()
    else:
        return -winner.get_hp()


class State:
    def __init__(self, num, bq, score=None) -> None:
        self.num = num
        self.bq = bq
        self.score = score
        self.children = []

    def __repr__(self):
        return 'State: {}, Score: {}'.format(self.num, self.score)


class Minimax(Playstyle):
    def __init__(self, battle_queue):
        super().__init__(battle_queue)
        self.is_manual = False
        self.get_state_score_function = None

    def select_attack(self, parameter: Any = None):
        curr_player = self.battle_queue.peek()

        score_1, score_2 = None, None
        actions = curr_player.get_available_actions()
        bq1, bq2 = self.battle_queue.copy(), self.battle_queue.copy()
        curr_player1, curr_player2 = bq1.remove(), bq2.remove()

        if 'A' in actions:
            curr_player1.attack()
            score_1 = self.get_state_score_function(bq1)
        if 'S' in actions:
            curr_player2.special_attack()
            score_2 = self.get_state_score_function(bq2)

        max_ = True if curr_player1 == bq1.peek() else False
        if max_:
            if score_1 and score_2:
                return 'A' if score_1 > score_2 else 'S'
            else:
                return 'A' if score_1 else 'S'
        else:
            if score_1 and score_2:
                return 'A' if score_1 < score_2 else 'S'
            else:
                return 'A' if score_1 else 'S'

    def copy(self, new_battle_queue: 'BattleQueue') -> 'Playstyle':
        """
        Return a copy of this Minimax Playstyle which uses the
        BattleQueue new_battle_queue.
        """
        raise NotImplementedError


class MinimaxRecursive(Minimax):
    def __init__(self, battle_queue):
        super().__init__(battle_queue)
        self.get_state_score_function = get_state_score

    def copy(self, new_battle_queue: 'BattleQueue') -> 'Playstyle':
        """
        Return a copy of this MinimaxRecursive Playstyle which uses the
        BattleQueue new_battle_queue.
        """
        return MinimaxRecursive(new_battle_queue)


class MinimaxIterative(Minimax):
    def __init__(self, battle_queue):
        super().__init__(battle_queue)
        self.get_state_score_function = get_state_score_iterative

    def copy(self, new_battle_queue: 'BattleQueue') -> 'Playstyle':
        """
        Return a copy of this MinimaxIterative Playstyle which uses the
        BattleQueue new_battle_queue.
        """
        return MinimaxIterative(new_battle_queue)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # import python_ta
    # python_ta.check_all(config='a2_pyta.txt')
