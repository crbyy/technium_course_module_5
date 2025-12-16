import json
import csv
from csv import DictReader

#1
with open ('students.json', 'r', encoding = 'utf-8') as students:
    data = json.load(students)
    count_students = []

    python_students = []

    for student in data:
        print(student["имя"])
        count_students.append(student["имя"])
        print(student["возраст"])
        print(student["город"])
        print(student["предметы"])
        if "Python" in student["предметы"]:
            python_students.append(student["имя"])


    print("Количество студентов: ", len(count_students))   #Счетчик студентов

    max_student = max(data, key=lambda x: x["возраст"])
    print("Самый старший студент: ", max_student["имя"], max_student["возраст"], max_student["город"])
    print("Количество студентов изучающих Python: ", len(python_students))



#2
with open('sales.csv', 'r', encoding = 'utf-8') as csv_f:
    reader = csv.DictReader(csv_f, delimiter = ',')

    cost = []
    product_cost = {}
    monthly_sales = {}

    for row in reader:

        date = row["Дата"]
        product = row["Продукт"]
        amount = int(row["Сумма"])

        print(date, product, amount)

        cost.append(amount)

        if product in product_cost:
            product_cost[product] += amount
        else:
            product_cost[product] = amount

        month = date[5:7]

        if month in monthly_sales:
            monthly_sales[month] += amount
        else:
            monthly_sales[month] = amount

    print("\nОбщая сумма: ", sum(cost))
    max_cost = max(product_cost, key=lambda x: product_cost[x])
    print(f"Продукт с самым высоким объемом продаж: {max_cost} - {product_cost[max_cost]}р.\n")

    print("Общая сумма продаж для каждого месяца:")
    for month, value in monthly_sales.items():
        print(f"Месяц: {month}, Сумма: {value}")



#3
with open('employees.json', 'r', encoding='utf-8') as jsonf:
    employees = json.load(jsonf)

with open('performance.csv', 'r') as csvf:
    reader = csv.DictReader(csvf, delimiter = ',')
    performance = {}
    perf_list = []


    for row in reader:
        employee_id = row['employee_id']
        perf = row['performance']

        performance[employee_id] = perf


    for employee in employees:
        emp_id = str(employee['id'])
        if emp_id in performance:
            employee['performance'] = performance[emp_id]

    for employee in employees:
        print("ID:", employee['id'])
        print("Имя:", employee['имя'])
        print("Должность:", employee['должность'])
        print("Производительность:", employee['performance'])
        print()

        perf_list.append(int(employee['performance']))

    avg_perf = sum(perf_list)/ len(perf_list)
    print("Средняя производительность: ", avg_perf)

    best = max(employees, key=lambda x:x['performance'])
    print(f'Лучший сотрудник: {best['имя']}, Производительность: {best['performance']}')


