"""
The Character class for A1.
The Character class is an abstract class and
the Mage and Rouge are subclasses inheritance from this superclass.
"""


class Character:
    """
    A class representing a Character.

    name: The name of the character
    battle_queue: A queue that lets our game know in what order various
        characters are going to attack
    playstyle: Ways for us to choose attacks
    _hp: Health Point
    _sp: Skill Point
    enemy: The enemy to attack
    animation_state: use for tracking the state for get sprite
    attack_cost: cost for attack (reduce how many sp)
    special_attack_cost: cost for special attack (reduce how many sp)
    attack_damage: damage for attack
    special_attack_damage: damage for special attack
    defense: depense point
    """
    name: str
    battle_queue: 'BattleQueue'
    playstyle: 'Playstyle'
    _hp: int
    _sp: int
    enemy: 'Character'
    animation_state: str
    attack_cost: int
    special_attack_cost: int
    attack_damage: int
    special_attack_damage: int
    defense: int

    def __init__(self, name: str, battle_queue: 'BattleQueue',
                 playstyle: 'Playstyle') -> None:
        """
        Initialize this Character with the name, battle_queue, playstyle.
        """
        self.name = name
        self.battle_queue = battle_queue
        self.playstyle = playstyle
        self._hp = 100
        self._sp = 100
        self.enemy = None
        self.animation_state = None

        # Initialize the stats of the Character
        self.attack_cost = 0
        self.special_attack_cost = 0
        self.attack_damage = 0
        self.special_attack_damage = 0
        self.defense = 0

    def get_name(self) -> str:
        """
        Return the name of the Character.

        >>> from a1_battle_queue import *
        >>> bq = BattleQueue()
        >>> from a1_playstyle import *
        >>> ps = ManualPlaystyle(bq)
        >>> c = Rogue('joy', bq, ps)
        >>> c.get_name()
        'joy'
        """
        return self.name

    def get_hp(self) -> int:
        """
        Return the Health Points of the Character.

        >>> from a1_battle_queue import *
        >>> bq = BattleQueue()
        >>> from a1_playstyle import *
        >>> ps = ManualPlaystyle(bq)
        >>> c = Rogue('joy', bq, ps)
        >>> c.get_hp()
        100
        """
        return self._hp

    def get_sp(self) -> int:
        """
        Return the Skill Points of the Character.

        >>> from a1_battle_queue import *
        >>> bq = BattleQueue()
        >>> from a1_playstyle import *
        >>> ps = ManualPlaystyle(bq)
        >>> c = Rogue('joy', bq, ps)
        >>> c.get_sp()
        100

        """
        return self._sp

    def attack(self) -> None:
        """
        The Character attacks its enemy. The Character costs some sp
        and reduces its enemy's hp.
        (unique by different character)

        >>> from a1_battle_queue import *
        >>> bq = BattleQueue()
        >>> from a1_playstyle import *
        >>> ps = ManualPlaystyle(bq)
        >>> c = Rogue('joy', bq, ps)
        >>> c.enemy = Mage('jeff', bq, ps)
        >>> c.attack()
        >>> c.get_sp()
        97
        >>> c.enemy.get_hp()
        93
        """
        if self._sp >= self.attack_cost:
            self.battle_queue.add(self)
            self.animation_state = "A"
            self._sp -= self.attack_cost
            self.enemy._hp -= (self.attack_damage - self.enemy.defense)
            if self.enemy._hp < 0:
                self.enemy._hp = 0

    def special_attack(self) -> None:
        """
        The Character special attacks its enemy.
        The Character costs some sp and reduces its enemy's hp.
        (unique by different character)

        >>> from a1_battle_queue import *
        >>> bq = BattleQueue()
        >>> from a1_playstyle import *
        >>> ps = ManualPlaystyle(bq)
        >>> c = Rogue('joy', bq, ps)
        >>> c.enemy = Mage('jeff', bq, ps)
        >>> c.attack()
        >>> c.get_sp()
        97
        >>> c.enemy.get_hp()
        93
        """
        if self._sp >= self.special_attack_cost:
            self.animation_state = "S"
            self._sp -= self.special_attack_cost
            self.enemy._hp -= (self.special_attack_damage - self.enemy.defense)
            if self.enemy._hp < 0:
                self.enemy._hp = 0

    def is_valid_action(self, action) -> bool:
        """
        Return False when passed a skill and
        when there's not enough sp to use that skill.
        >>> from a1_battle_queue import *
        >>> bq = BattleQueue()
        >>> from a1_playstyle import *
        >>> ps = ManualPlaystyle(bq)
        >>> c = Rogue('joy', bq, ps)
        >>> c.enemy = Mage('jeff', bq, ps)
        >>> c.is_valid_action('A')
        True
        >>> c.is_valid_action('S')
        True
        """
        return action in self.get_available_actions()

    def get_available_actions(self) -> list:
        """
        Return a list of str contains the attacks
        that are available for Character.

        >>> from a1_battle_queue import *
        >>> bq = BattleQueue()
        >>> from a1_playstyle import *
        >>> ps = ManualPlaystyle(bq)
        >>> c = Mage('joy', bq, ps)
        >>> c.enemy = Mage('jeff', bq, ps)
        >>> c.get_available_actions()
        ['A', 'S']
        >>> c.special_attack()
        >>> c.special_attack()
        >>> c.special_attack()
        >>> c.get_available_actions()
        ['A']
        >>> c.attack()
        >>> c.attack()
        >>> c.get_available_actions()
        []
        """
        if self.get_sp() >= self.special_attack_cost:
            return ["A", "S"]
        elif self.get_sp() >= self.attack_cost:
            return ["A"]
        return []

    def __repr__(self) -> str:
        """
        Return a string representing the Character.

        """
        raise NotImplementedError

    def get_next_sprite(self) -> str:
        """
        Return the sprites when in different pose
        depends on the animation state.

        """
        raise NotImplementedError

    def get_next_sprite_helper(self, class_name) -> str:
        """
        The Helper function for get_next_sprite().
        Given the Character's class name (Mage, Rogue)

        Return the sprites when in different pose
        depends on the animation state.

        >>> from a1_battle_queue import *
        >>> bq = BattleQueue()
        >>> from a1_playstyle import *
        >>> ps = ManualPlaystyle(bq)
        >>> c = Rogue('joy', bq, ps)
        >>> expected_sprites = []
        >>> for i in range(10):
        ...     expected_sprites.append("rogue_idle_" + str(i))
        >>> expected_sprites.append("rogue_idle_0")
        >>> actual_sprites = []
        >>> for i in range(11):
        ...     actual_sprites.append(c.get_next_sprite_helper("rogue"))
        >>> print(expected_sprites == actual_sprites)
        True
        """
        if not self.animation_state:
            self.animation_state = "idle_0"
            return "{}_idle_0".format(class_name)
        elif self.animation_state == "A":
            self.animation_state = "attack_0"
            return "{}_attack_0".format(class_name)
        elif self.animation_state == "S":
            self.animation_state = "special_0"
            return "{}_special_0".format(class_name)

        if self.animation_state[-1] == "9":
            self.animation_state = None
            return "{}_idle_0".format(class_name)

        self.animation_state = self.animation_state[0: -1] + \
                               str(int(self.animation_state[-1]) + 1)
        return "{}_{}".format(class_name, self.animation_state)


class Rogue(Character):
    """
    A class representing a Rogue.

    """
    def __init__(self, name, battle_queue, playstyle) -> None:
        """
        Initialize Rogue with the name, battle_queue, playstyle.

        >>> from a1_battle_queue import *
        >>> bq = BattleQueue()
        >>> from a1_playstyle import *
        >>> ps = ManualPlaystyle(bq)
        >>> c = Rogue('joy', bq, ps)
        >>> c.name
        'joy'
        >>> repr(c)
        'joy (Rogue): 100/100'
        """
        super().__init__(name, battle_queue, playstyle)
        self.defense = 10
        self.attack_cost = 3
        self.special_attack_cost = 10
        self.attack_damage = 15
        self.special_attack_damage = 20

    def special_attack(self) -> None:
        """
        The Character special attacks its enemy.
        The Character costs some sp and reduces its enemy's hp.

        >>> from a1_battle_queue import *
        >>> bq = BattleQueue()
        >>> from a1_playstyle import *
        >>> ps = ManualPlaystyle(bq)
        >>> c = Rogue('joy', bq, ps)
        >>> c.enemy = Mage('jeff', bq, ps)
        >>> c.special_attack()
        >>> c.get_sp()
        90
        >>> c.enemy.get_hp()
        88
        """
        super().special_attack()
        self.battle_queue.add(self)
        self.battle_queue.add(self)

    def __repr__(self) -> str:
        """
        Return a string representing the Rogue.

        >>> from a1_battle_queue import *
        >>> bq = BattleQueue()
        >>> from a1_playstyle import *
        >>> ps = ManualPlaystyle(bq)
        >>> c = Rogue('joy', bq, ps)
        >>> repr(c)
        'joy (Rogue): 100/100'
        >>> c.enemy = Mage('jeff', bq, ps)
        >>> c.special_attack()
        >>> repr(c)
        'joy (Rogue): 100/90'
        >>> repr(c.enemy)
        'jeff (Mage): 88/100'
        """
        return "{} ({}): {}/{}".format(self.name, "Rogue", self._hp, self._sp)

    def get_next_sprite(self) -> str:
        """
        Return the sprites for rogue when in different pose
        depends on the animation state.

        >>> from a1_battle_queue import *
        >>> bq = BattleQueue()
        >>> from a1_playstyle import *
        >>> ps = ManualPlaystyle(bq)
        >>> c = Rogue('joy', bq, ps)
        >>> c.enemy = Mage('jeff', bq, ps)
        >>> c.attack()
        >>> expected_sprites = []
        >>> for i in range(10):
        ...     expected_sprites.append("rogue_attack_" + str(i))
        >>> expected_sprites.append("rogue_idle_0")
        >>> actual_sprites = []
        >>> for i in range(11):
        ...     actual_sprites.append(c.get_next_sprite())
        >>> print(expected_sprites == actual_sprites)
        True
        """
        return self.get_next_sprite_helper("rogue")


class Mage(Character):
    """
    A class representing Mage.

    """
    def __init__(self, name, battle_queue, playstyle) -> None:
        """
        Initialize Mage with the name, battle_queue, playstyle.

        >>> from a1_battle_queue import *
        >>> bq = BattleQueue()
        >>> from a1_playstyle import *
        >>> ps = ManualPlaystyle(bq)
        >>> c = Mage('joy', bq, ps)
        >>> c.name
        'joy'
        >>> repr(c)
        'joy (Mage): 100/100'
        """
        super().__init__(name, battle_queue, playstyle)
        self.defense = 8
        self.attack_cost = 5
        self.special_attack_cost = 30
        self.attack_damage = 20
        self.special_attack_damage = 40

    def special_attack(self) -> None:
        """
        The Character special attacks its enemy.
        The Character costs some sp and reduces its enemy's hp.

        >>> from a1_battle_queue import *
        >>> bq = BattleQueue()
        >>> from a1_playstyle import *
        >>> ps = ManualPlaystyle(bq)
        >>> c = Mage('joy', bq, ps)
        >>> c.enemy = Mage('jeff', bq, ps)
        >>> c.special_attack()
        >>> c.get_sp()
        70
        >>> c.enemy.get_hp()
        68
        """
        super().special_attack()
        self.battle_queue.add(self.enemy)
        self.battle_queue.add(self)

    def __repr__(self) -> str:
        """
        Return a string representing the Mage.

        >>> from a1_battle_queue import *
        >>> bq = BattleQueue()
        >>> from a1_playstyle import *
        >>> ps = ManualPlaystyle(bq)
        >>> c = Mage('joy', bq, ps)
        >>> repr(c)
        'joy (Mage): 100/100'
        >>> c.enemy = Mage('jeff', bq, ps)
        >>> c.special_attack()
        >>> repr(c)
        'joy (Mage): 100/70'
        >>> repr(c.enemy)
        'jeff (Mage): 68/100'
        """
        return "{} ({}): {}/{}".format(self.name, "Mage", self._hp, self._sp)

    def get_next_sprite(self) -> str:
        """
        Return the sprites for mage when in different pose
        depends on the animation state.

        >>> from a1_battle_queue import *
        >>> bq = BattleQueue()
        >>> from a1_playstyle import *
        >>> ps = ManualPlaystyle(bq)
        >>> c = Mage('joy', bq, ps)
        >>> c.enemy = Rogue('jeff', bq, ps)
        >>> c.special_attack()
        >>> expected_sprites = []
        >>> for i in range(10):
        ...     expected_sprites.append("mage_special_" + str(i))
        >>> expected_sprites.append("mage_idle_0")
        >>> actual_sprites = []
        >>> for i in range(11):
        ...     actual_sprites.append(c.get_next_sprite())
        >>> print(expected_sprites == actual_sprites)
        True
        """
        return self.get_next_sprite_helper("mage")


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    import python_ta
    python_ta.check_all(config='a1_pyta.txt')
