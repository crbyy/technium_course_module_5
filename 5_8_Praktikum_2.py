from collections import Counter, namedtuple, defaultdict, deque
import random

#1

num_list = []
nums = '12345'
nums = list(nums)

while len(num_list) <= 10:
    random_choice = random.choice(nums)
    num_list.append(random_choice)

print(num_list)
counter = Counter(num_list)
print(counter)
most_common = counter.most_common(3)
print(most_common)

for number, n in most_common:
    print(f'Число "{number}" встречается "{n}" раз(а)')


#2

Book = namedtuple('Book',  ['title', 'author', 'genre'])

book1 = Book(title='«Война и мир»', author='Лев Николаевич Толстой', genre='роман-эпопея')
book2 = Book(title='«Гарри Поттер и философский камень»', author='Джоан Роулинг', genre='фэнтези')
book3 = Book(title='«1984»', author='Джордж Оруэлл', genre='антиутопия')

print(f'\nКнига №1: {book1.title} \nАвтор: {book1.author} \nЖанр: {book1.genre}')
print(f'\nКнига №2: {book2.title} \nАвтор: {book2.author} \nЖанр: {book2.genre}')
print(f'\nКнига №3: {book3.title} \nАвтор: {book3.author} \nЖанр: {book3.genre}')


#3
students = [("Группа 1", "Артем"), ("Группа 2", "Ирина"), ("Группа 1", "Даниил"),
            ("Группа 2", "Кирилл"), ("Группа 3", "Миша")]

groups = defaultdict(list)

print()

for group, student in students:
    groups[group].append(student)

for key, values in groups.items():
    print(f"{key}: {values}")


#4
print()
queue = deque(['3-й слайд','1-й слайд', '4-й слайд'])
print(f'1.{queue}')

queue.append('5-слайд')
print(f'2.{queue}')

queue.insert(1, queue.popleft())
print(f'3.{queue}')

queue.insert(1, '2-й слайд')
print(f'4.{queue}')

queue.appendleft('Титул')
print(f'5.{queue}')

queue.pop()
print(f'6.{queue}')

queue.append('Заключение')
print(f'7.{queue}')


#5
print()
q = deque()

def append_q(item):
    q.append(item)
    print(f'Добавлен: {item}')

def append_left_q(item):
    q.appendleft(item)
    print(f'Добавлен в начало: {item}')

def pop_q():
    if q:
        item = q.pop()
        print(f'Удален: {item}')
        return item
    else:
        print('Очередь пуста')

def popleft_q():
    if q:
        item = q.popleft()
        print(f'Удален: {item}')
        return item
    else:
        print('Очередь пуста')

append_q('Слайд №2')
append_left_q('Слайд №1')
append_q('Слайд №3')
print(q)

append_q("Вступление")
i = pop_q()
append_left_q(i)
print(q)

popleft_q()
append_left_q("Титул")
print(q)

















