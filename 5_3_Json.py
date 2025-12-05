import json
import csv

with open('prices.csv', 'r', encoding = 'utf-8') as f_csv:
    reader = csv.DictReader(f_csv, delimiter = ',')
    data = list(reader)
    print(json.dumps(data, indent=4, ensure_ascii = False))
