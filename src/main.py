#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import statistics

from config import read_config, items


"""
Regrading
"""

def craft_and_regrade(make, name, crafting_cost, min_grade, resplendent_for):
    import crafted_item

    costs = []
    breaks = []
    great_successes = 0

    for i in range(make):
        piece = crafted_item.CraftedItem(name, crafting_cost, resplendent_for)

        while piece.grade != min_grade and piece.grade != min_grade.success_to:
            piece.regrade()

        if piece.grade == min_grade.success_to:
            great_successes += 1

        costs.append(piece.total_cost)
        breaks.append(piece.breaks)

    print('{} ({}) => mean cost: {}, mean break/item: {}, great successes: {}% ({})'.format(
        name,
        min_grade,
        statistics.mean(costs),
        statistics.mean(breaks),
        great_successes / make * 100,
        great_successes
    ))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--grades', required=True, help='configuration file for grades', dest='grades')
    parser.add_argument('-p', '--prices', required=True, help='configuration file for AH prices', dest='prices')
    parser.add_argument('-i', '--items', required=True, help='configuration file for items to make', dest='items')
    parser.add_argument('-m', '--make', required=True, help='number of each item to make', dest='make')
    args = parser.parse_args()

    read_config(args.grades, args.prices, args.items)

    from grades import grades

    print('Making {} of each item:'.format(args.make))
    for section_name in items.sections():
        s = items[section_name]
        craft_and_regrade(
            make=int(args.make),
            name=s['name'],
            crafting_cost=int(s['crafting_cost']),
            min_grade=grades.get(s['min_grade']),
            resplendent_for=[grades.get(g) for g in s['resplendent_for'].split(',')],
        )
