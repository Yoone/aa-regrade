# -*- coding: utf-8 -*-

from configparser import ConfigParser


grades = ConfigParser()
prices = ConfigParser()
items = ConfigParser()

def read_config(grades_path, prices_path, items_path):
    grades.read(grades_path)
    prices.read(prices_path)
    items.read(items_path)
