# read_csv.py

path = '04/data.csv'

import csv

with open(path, encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    for line in reader:
        print(line)
