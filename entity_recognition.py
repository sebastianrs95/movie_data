import pandas as pd
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
import spacy
import re, csv
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()


df = pd.read_csv('datasets/wiki_movie_plots_deduped.csv')

import pprint
pp = pprint.PrettyPrinter(indent=4)

cnt_entities = Counter()
total = len(df)


i = 0
for plot in df['Plot']:
    doc = nlp(plot)
    current_entities = [(X.text, X.label_) for X in doc.ents]
    print('plot', i, 'of a total of', total)
    # iterate over the entities, and add it to the dictionary
    for entity in current_entities:
        cnt_entities[entity] += 1

    i += 1

with open('entities.csv', mode='w') as csv_file:
    fieldnames = ['entity', 'count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for key, value in cnt_entities.items():
        writer.writerow({'entity': key, 'count':value})