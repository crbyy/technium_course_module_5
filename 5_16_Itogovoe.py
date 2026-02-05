import json
import csv


with open('student_list.json', 'r', encoding = 'utf-8') as file:
    student_dict = json.load(file)


#1
def get_average_score(student):
    grades = student_dict[student]['grades']
    return sum(grades.values()) / len(grades)

#2
def get_best_student():
     i = list(sorted(avg_list, key= lambda item: item[1], reverse= True))
     return f'\nНаилучший студент: {i[0][0]} (Средний балл: {i[0][1]})'

def get_worst_student():
    i = list(sorted(avg_list, key=lambda item: item[1]))
    return f'\nХудший студент: {i[0][0]} (Средний балл: {i[0][1]})'

#3
def find_student(student):
    if student in student_dict:
        print(f'\nИмя: {student}')
        print(f'Возраст: {student_dict[student]['age']}')
        print(f'Предметы: {student_dict[student]['subjects']}')
        print(f'Оценки: {student_dict[student]['grades']}')
    else:
        print (f'\nСтудент с именем {student} не найден')



avg_list = [] # Для задания №4
for student in student_dict:
    print(f'Средний балл для студента "{student}": {get_average_score(student)}') # Для задания №1
    avg_list.append((student, get_average_score(student))) # Для задания №4

#2
print(get_best_student())
print(get_worst_student())

#3
find_student('John')
find_student('Max')

#4
sorted_avg = list(sorted(avg_list, key= lambda item: item[1], reverse= True))

print('\nСортировка студентов по среднему баллу:')
for i in sorted_avg:
    name = i[0]
    score = i[1]
    print(f'{name}: {score}')


#5
list_student_dict = [{'name': name, **data} for name, data in student_dict.items()]


#6
csv_data = []
for name, data in student_dict.items():
    avg_score = get_average_score(name)
    csv_data.append({
        'name': name,
        'age': data['age'],
        'grade': avg_score
    })

with open('student_list.csv', 'w', encoding= 'utf-8') as csv_file:
    fieldnames = ['name', 'age', 'grade']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(csv_data)


