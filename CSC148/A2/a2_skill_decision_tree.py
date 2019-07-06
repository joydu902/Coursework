"""
The SkillDecisionTree class for A2.

You are to implement the pick_skill() method in SkillDecisionTree, as well as
implement create_default_tree() such that it returns the example tree used in
a2.pdf.

This tree will be used during the gameplay of a2_game, but we may test your
SkillDecisionTree with other examples.
"""
from typing import Callable, List, Union
from a2_skills import RogueAttack, RogueSpecial, MageAttack, MageSpecial

class SkillDecisionTree:
    """
    A class representing the SkillDecisionTree used by Sorcerer's in A2.
    
    value - the skill that this SkillDecisionTree contains.
    condition - the function that this SkillDecisionTree will check.
    priority - the priority number of this SkillDecisionTree.
               You may assume priority numbers are unique (i.e. no two
               SkillDecisionTrees will have the same number.)
    children - the subtrees of this SkillDecisionTree.
    """
    value: 'Skill'
    condition: Callable[['Character', 'Character'], bool]
    priority: int
    children: List['SkillDecisionTree']
    
    def __init__(self, value: 'Skill', 
                 condition: Callable[['Character', 'Character'], bool],
                 priority: int,
                 children: List['SkillDecisionTree'] = None):
        """
        Initialize this SkillDecisionTree with the value value, condition
        function condition, priority number priority, and the children in
        children, if provided.
        
        >>> from a2_skills import MageAttack
        >>> def f(caster, target):
        ...     return caster.hp > 50
        >>> t = SkillDecisionTree(MageAttack(), f, 1)
        >>> t.priority
        1
        >>> type(t.value) == MageAttack
        True
        """
        self.value = value
        self.condition = condition
        self.priority = priority
        self.children = children[:] if children else []

    def __repr__(self) -> str:
        """
        Return the representation of SkillDecisionTree.
        >>> from a2_skills import MageAttack
        >>> def f(caster, _):
        ...     return caster.hp > 50
        >>> t = SkillDecisionTree(MageAttack(), f, 1)
        >>> t
        SDT(1, MageAttack)
        """
        return "SDT({}, {})".format(self.priority,
                                    self.value.__class__.__name__)
    
    # Implement a method called pick_skill which takes in a caster and target
    # and returns a skill.

    def pick_skill(self, caster: 'Character', target: 'Character') \
            -> Union['Skill', None]:
        """
        Pick the skill with the highest priority, and fulfills the conditions.

        >>> sdt = create_default_tree()
        >>> from a2_battle_queue import BattleQueue
        >>> bq = BattleQueue()
        >>> from a2_playstyle import ManualPlaystyle
        >>> from a2_characters import Rogue, Mage, Vampire, Sorcerer
        >>> caster = Vampire("Caster", bq, ManualPlaystyle(bq))
        >>> target = Vampire("Target", bq, ManualPlaystyle(bq))
        >>> caster.set_hp(100)
        >>> caster.set_sp(40)
        >>> target.set_hp(50)
        >>> target.set_sp(30)
        >>> sdt.pick_skill(caster, target).__class__.__name__
        'MageSpecial'
        """
        result = None
        for sdt in self.get_satisfied_sdt(caster, target):
            if not result:
                result = sdt
            elif sdt.priority < result.priority:
                result = sdt
        if result:
            return result.value
        return None

    def get_satisfied_sdt(self, caster: 'Character',
                          target: 'Character') -> list:
        """
        Return a list of skills that fulfills the condition.

        >>> sdt = create_default_tree()
        >>> from a2_battle_queue import BattleQueue
        >>> bq = BattleQueue()
        >>> from a2_playstyle import ManualPlaystyle
        >>> from a2_characters import Rogue, Mage, Vampire, Sorcerer
        >>> caster = Vampire("Caster", bq, ManualPlaystyle(bq))
        >>> target = Vampire("Target", bq, ManualPlaystyle(bq))
        >>> caster.set_hp(100)
        >>> caster.set_sp(40)
        >>> target.set_hp(50)
        >>> target.set_sp(30)
        >>> sdt.get_satisfied_sdt(caster, target)
        [SDT(4, RogueSpecial), SDT(2, MageSpecial), SDT(7, RogueSpecial)]
        """

        if not self.children or not self.condition(caster, target):
            return [self]
        result = []
        for child in self.children:
            result += child.get_satisfied_sdt(caster, target)
        return result


def create_default_tree() -> SkillDecisionTree:
    """
    Return a SkillDecisionTree that matches the one described in a2.pdf.

    >>> sdt = create_default_tree()
    >>> from a2_battle_queue import BattleQueue
    >>> bq = BattleQueue()
    >>> from a2_playstyle import ManualPlaystyle
    >>> from a2_characters import Rogue, Mage, Vampire, Sorcerer
    >>> caster = Vampire("Caster", bq, ManualPlaystyle(bq))
    >>> target = Vampire("Target", bq, ManualPlaystyle(bq))
    >>> caster.set_hp(80)
    >>> caster.set_sp(40)
    >>> target.set_hp(20)
    >>> target.set_sp(50)
    >>> sdt.get_satisfied_sdt(caster, target)
    [SDT(6, RogueAttack), SDT(8, RogueAttack), SDT(1, RogueAttack)]
    >>> sdt.pick_skill(caster, target).__class__.__name__
    'RogueAttack'
    """
    def caster_hp_gt_90(caster, _):
        """
        Return True if the caster's HP is > 90
        """
        return caster.get_hp() > 90

    def target_sp_gt_40(_, target):
        """
        Return True if the target's SP is >40
        """
        return target.get_sp() > 40

    def caster_sp_gt_20(caster, _):
        """
        Return True if the caster's SP is > 20
        """
        return caster.get_sp() > 20

    def target_hp_lt_30(_, target):
        """
        Return True if the target's HP is < 30
        """
        return target.get_hp() < 30

    def caster_hp_gt_50(caster, _):
        """
        Return True if the caster's HP is > 50
        """
        return caster.get_hp() > 50

    def no_condition(_, __):
        """
        By default, return True.
        """
        return True

    priority_1 = SkillDecisionTree(RogueAttack(), caster_hp_gt_90, 1)
    priority_2 = SkillDecisionTree(MageSpecial(), target_sp_gt_40, 2)
    priority_3 = SkillDecisionTree(MageAttack(), caster_sp_gt_20, 3)
    priority_4 = SkillDecisionTree(RogueSpecial(), target_hp_lt_30, 4)
    priority_5 = SkillDecisionTree(MageAttack(), caster_hp_gt_50, 5)
    priority_6 = SkillDecisionTree(RogueAttack(), no_condition, 6)
    priority_7 = SkillDecisionTree(RogueSpecial(), no_condition, 7)
    priority_8 = SkillDecisionTree(RogueAttack(), no_condition, 8)

    priority_4.children.append(priority_6)
    priority_3.children.append(priority_4)
    priority_2.children.append(priority_8)
    priority_1.children.append(priority_7)

    priority_5.children = [priority_3, priority_2, priority_1]
    return priority_5


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='a2_pyta.txt')
