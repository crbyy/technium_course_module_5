import csv

with open('prices.txt', 'r', encoding = 'utf-8') as txt_f:
    txt_lines = [line.strip().split('\t') for line in txt_f]

with open('prices.csv', 'w', encoding = 'utf-8', newline= '') as csv_f:
    writer = csv.writer(csv_f, delimiter=';')
    writer.writerows(txt_lines)

data = []

for item in txt_lines:
    data.append({
        'Наименование': item[0],
        'Количество': item[1],
        'Цена': item[2]
    })

with open('prices.csv', 'w', encoding = 'utf-8') as csv_f:

    fieldnames = ['Наименование', 'Количество', 'Цена']
    writer = csv.DictWriter(csv_f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

with open('prices.csv', 'r', encoding = 'utf-8') as csv_f:
    reader = csv.DictReader(csv_f, delimiter = ',')
    print('Ваш заказ: ')
    for row in reader:
        sum_item = (int(row['Цена']) * int(row['Количество']))
        print(row['Наименование'], row['Количество'], 'шт.' , row['Цена'], 'р./шт.', '=', sum_item)

    summ = sum(int(row[1]) * int(row[2]) for row in txt_lines)
    print(f'Сумма заказа: {summ}р.')






