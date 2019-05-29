import pandas as pd
import csv
from ast import literal_eval as make_tuple

df = pd.read_csv('entities.csv')

with open('new_entities.csv', mode='w', encoding='utf8') as csv_file:
    fieldnames = ['phrase', 'entity', 'count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for index, row in df.iterrows():
        curr_tuple = make_tuple(row['entity'])
        writer.writerow({'phrase': curr_tuple[0], 'entity': curr_tuple[1], 'count': row['count']})