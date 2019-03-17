# -*- coding: utf-8 -*-

import grades


"""
Crafting
"""

class CraftedItem:
    def __init__(
        self,
        name,
        crafting_cost=0,
        resplendent_for=[],
        starting_grade=grades.grand_grade,
    ):
        self.name = name
        self.crafting_cost = crafting_cost
        self.starting_grade = starting_grade
        self.resplendent_for = resplendent_for

        # Accumulative vars
        self.total_cost = crafting_cost
        self.grade = starting_grade
        self.breaks = 0

    def regrade(self):
        regrade_cost, grade = self.grade.regrade(self.grade in self.resplendent_for)
        self.total_cost += regrade_cost

        if grade is None:  # It broke
            self.grade = self.starting_grade
            self.total_cost += self.crafting_cost  # Making a new one
            self.breaks += 1
        else:
            self.grade = grade

    def __str__(self):
        return '{} ({})'.format(self.name, self.grade)
