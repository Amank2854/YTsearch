# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 19:16:10 2021

@author: Aman
"""

import argparse
from webbrowser import open
from urllib.request import urlopen
from re import findall

parser = argparse.ArgumentParser()
parser.add_argument('string', help="Enter String for search")
parser.add_argument('-n', type=int, default=0, help='Open the preferred positioned search')

args =parser.parse_args()
search = args.string.replace(" ","+")
pos = args.n

link = urlopen("https://www.youtube.com/results?search_query="+search)

vidlist = findall(r"watch\?v=(\S{11})", link.read().decode())

final_link = "https://www.youtube.com/watch?v="+vidlist[pos-1]

open(final_link)

