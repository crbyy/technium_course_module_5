#1
strings =  ["apple", "kiwi", "banana", "fig"]
sorted_strings = list(filter(lambda x: len(x) > 4, strings))
print(sorted_strings)

#2
students = [
    {"name": "John", "grade": 90},
    {"name": "Jane", "grade": 85},
    {"name": "Dave", "grade": 92}
]

max_student = max(students, key=lambda student: student['grade'])
print(max_student )

#3
tuples = [(1, 5), (3, 2), (2, 8), (4, 3)]
sorted_sums = sorted(tuples, key=lambda x: sum((x[0], x[1])))
print(sorted_sums)


#4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_even = list(filter(lambda x: x % 2 == 0, numbers))
print(filtered_even)

#5
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"


students = [
    Person('Stephen', 38),
    Person('Egor', 19),
    Person('Brian', 27)
]

age_sorted = sorted(students, key=lambda x:x.age)
print(age_sorted)

