# -*- coding: utf-8 -*-

from config import prices


"""
Regrade Charms
"""

class Charm:
    def __init__(self, name, chance, price):
        self.name = name,
        self.chance = chance
        self.price = price

    def __str__(self):
        return self.name

green_charm = Charm('Green', chance=1.75, price=int(prices['prices']['green_charm']))
blue_charm = Charm('Blue', chance=1.75, price=int(prices['prices']['blue_charm']))
red_charm = Charm('Red', chance=2, price=int(prices['prices']['red_charm']))
sup_red_charm = Charm('Superior Red', chance=2, price=int(prices['prices']['sup_red_charm']))
