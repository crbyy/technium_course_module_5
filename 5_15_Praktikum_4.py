
#1
students_dict = {
 'Саша': 27,
 'Кирилл': 52,
 'Маша': 14,
 'Петя': 36,
 'Оля': 43,
}

sorted_age = dict(sorted(students_dict.items(), key=lambda item: item[1]))

print(sorted_age)


#2 Индекс тела - Вес тела в килограммах/(Рост в метрах∗Рост в метрах)
data = [
    (82, 191),
    (68, 174),
    (90, 189),
    (73, 179),
    (76, 184),
]

index = list(map(lambda item: item[0] / ((item[1] / 100) ** 2), data))
new_data = [(w, h, round(i, 2)) for (w, h), i in zip(data, index)]
sorted_index = list(sorted(new_data, key=lambda x: x[2]))

print(sorted_index)

#3
students_list = [
    {
        "name": "Саша",
        "age": 27,
    },
    {
        "name": "Кирилл",
        "age": 52,
    },
    {
        "name": "Маша",
        "age": 14,
    },
    {
        "name": "Петя",
        "age": 36,
    },
    {
        "name": "Оля",
        "age": 43,
    },
]

sorted_age = list(sorted(students_list, key=lambda student: student['age']))
print(sorted_age[0])



