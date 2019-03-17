# -*- coding: utf-8 -*-

import os

from config import grades, prices
import charms


"""
Converted prices
"""

REGRADE_SCROLL_PRICE = int(prices['prices']['regrade_scroll'])
RESPLENDENT_REGRADE_SCROLL_PRICE = int(prices['prices']['resplendent_regrade_scroll'])


"""
Grades
"""

class Grade:
    def __init__(
        self,
        name,
        fee=0,
        success=0,
        success_to=None,
        downgrade=0,
        destroy=0,
        charm=None,
    ):
        self.name = name
        self.fee = fee
        self.base_success = success
        self.success_to = success_to
        self.base_downgrade = downgrade
        self.base_destroy = destroy
        self.charm = charm

        self.success = self.base_success
        self.downgrade = self.base_downgrade
        self.destroy = self.base_destroy
        self.base_try_cost = self.fee
        if self.charm is not None:
            self.success *= self.charm.chance
            self.downgrade /= self.charm.chance
            self.destroy /= self.charm.chance
            self.base_try_cost += self.charm.price

    def set_downgrade_to(self, downgrade_to):
        self.downgrade_to = downgrade_to

    def regrade(self, use_resplendent=False):
        """
        Returns: (cost, new_grade)
        """

        try_cost = self.base_try_cost
        if use_resplendent:
            try_cost += RESPLENDENT_REGRADE_SCROLL_PRICE
        else:
            try_cost += REGRADE_SCROLL_PRICE

        chance = int.from_bytes(os.urandom(4), byteorder='big', signed=False) / 0xFFFFFFFF

        if use_resplendent and chance <= self.success / 5:
            return (try_cost, self.success_to.success_to)  # Great Success!
        elif chance <= self.success:
            return (try_cost, self.success_to)  # Success!
        elif self.downgrade > 0 and chance <= self.success + self.downgrade:
            return (try_cost, self.downgrade_to)  # Downgraded
        elif self.destroy > 0 and chance <= self.success + self.downgrade + self.destroy:
            return (try_cost, None)  # Destroyed
        else:
            return (try_cost, self)  # Nothing happened

    def __str__(self):
        return self.name

# TODO: Charms and fees in user config
mythic_grade = Grade(
    'Mythic',
)

legendary_grade = Grade(
    'Legendary',
    # TODO: Add chances
    success_to=mythic_grade,
)

epic_grade = Grade(
    'Epic',
    fee=70,
    success=float(grades['grades']['epic_success']),
    success_to=legendary_grade,
    destroy=float(grades['grades']['epic_destroy']),
    charm=charms.sup_red_charm,
)

divine_grade = Grade(
    'Divine',
    fee=49,
    success=float(grades['grades']['divine_success']),
    success_to=epic_grade,
    destroy=float(grades['grades']['divine_destroy']),
    charm=charms.sup_red_charm,
)

celestial_grade = Grade(
    'Celestial',
    fee=37,
    success=float(grades['grades']['celestial_success']),
    success_to=divine_grade,
    downgrade=float(grades['grades']['celestial_downgrade']),
    destroy=float(grades['grades']['celestial_destroy']),
    charm=charms.sup_red_charm,
)

unique_grade = Grade(
    'Unique',
    fee=31,
    success=float(grades['grades']['unique_success']),
    success_to=celestial_grade,
    # charm=charms.red_charm,
)

heroic_grade = Grade(
    'Heroic',
    fee=27,
    success=float(grades['grades']['heroic_success']),
    success_to=unique_grade,
    charm=charms.blue_charm,
)

arcane_grade = Grade(
    'Arcane',
    fee=25,
    success=float(grades['grades']['arcane_success']),
    success_to=heroic_grade,
    charm=charms.green_charm,
)
celestial_grade.set_downgrade_to(arcane_grade)

rare_grade = Grade(
    'Rare',
    fee=22,
    success=float(grades['grades']['rare_success']),
    success_to=arcane_grade,
)

grand_grade = Grade(
    'Grand',
    fee=18,
    success=float(grades['grades']['grand_success']),
    success_to=rare_grade,
)


"""
Grades dict
"""

grades = {
    'mythic': mythic_grade,
    'legendary': legendary_grade,
    'epic': epic_grade,
    'divine': divine_grade,
    'celestial': celestial_grade,
    'unique': unique_grade,
    'heroic': heroic_grade,
    'arcane': arcane_grade,
    'rare': rare_grade,
    'grand': grand_grade,
}
