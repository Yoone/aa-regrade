aa-regrade
==========

This project is aimed at ArcheAge players who want to simulate gear regrades.

It allows simulating successive regrades to know how much gold it takes on average to regrade an item. It is possible to customize grade chances, the use of charms (or not), AH prices and crafting costs for an item.

Here is how it works if "I want to make 1000 Epic Obsidian Jerkins":

* It will run through simulations until it has made 1000 Epic Obsidian Jerkins
* For each downgrade or broken item throughout the process, it will count the crafting cost of the item towards the total price of making that one item and only add the item to the total count once it has reached Epic
* It will then display the average results (cost, break/item, great success ratio when using resplendent)

Setup & Requirements
--------------------

All you need is Python 3.

Usage
-----

* Run everything: `make`
* Run with a specific config file: `make v2.9` (runs with v2.9.cfg, only works for files following the `v.*\.cfg` format)
* Run without the use of the [Makefile](Makefile): `./src/main.py -g GRADES -p PRICES -i ITEMS -m MAKE`

What's missing?
---------------

* [ ] Regrade fees in config
* [ ] Chances on all grades
* [ ] Being able to choose to use charms or not through a config file
