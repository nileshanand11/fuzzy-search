#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals
from Levenshtein.StringMatcher import StringMatcher

# import pandas as pd
import csv
import operator
import json

WORD_LIMIT = 25

def get_suggetions(word):
    if(word is None):
        return ''
    words = {}
    with open('data/word_search.tsv') as cfile:
        reader =  csv.reader(cfile, delimiter='\t')
        for row in reader:
            w = row[0]
            m = StringMatcher(None,word,w)
            ratio = m.ratio()
            if(ratio > 0):
                words[w] = ratio
    sorted_values = sorted(words.items(), key=operator.itemgetter(1), reverse=True)
    lists = [k for k,v in sorted_values]

    return lists[:WORD_LIMIT]

