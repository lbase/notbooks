#!/usr/bin/python3
from sys import argv
import os
import pandas as pd
from slugify import slugify

import pandas as pd


def switch_demo(argument):
    switcher = {
        0: "Main",
        1: "Menu 1",
        2: "Menu 2",
        3: "Menu 3",
        4: "Menu 4",
        5: "Menu 5",
        6: "Menu 6",
        7: "Menu 7",
        8: "Menu 8",
        9: "Menu 9",
        10: "Menu 10",
        11: "Menu 11",
        12: "Menu 12",
        13: "Menu 13",
        14: "Menu 14",
        15: "Menu 15"

    }
    return switcher.get(argument, "Invalid month")


msqlfile = open('gqmdb.csv', 'r')
notes = pd.read_csv(msqlfile)
print(notes['Title'][8])
print(notes['Text'][8])
print(notes['Menu_Number'][8])
menu_entry = (notes['Menu_Number'][8])

print(switch_demo(menu_entry))
mycsvfile = open(mymenu.csv, 'w')
menunotes = pd.to_csv