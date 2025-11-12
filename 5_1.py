f = open('test.txt', 'w')

# Запишем в файл строку
f.write("This is a test string")

# обязательно нужно закрыть файл иначе он будет заблокирован ОС
f.close()

f = open('test.txt', 'r')

data = f.read()

print(data)

f.close()




f = open('test.txt', 'w')

f.write('This is ANOTHER string')

f.close()


f = open('test.txt', 'r')

data = f.read()

print(data)


f = open('test.txt', 'a')


f.write('\nThis is ANOTHER ANOTHER string бтв на русском вот так')

f = open('text.txt', 'r')
data = f.read()
print(data)

f.close()

f = open('text.txt', 'w')

sequence = ["Первая строка\n", "Вторая строка\n", "Третья строка\n"]

f.writelines(sequence)
f.close()

f = open('text.txt', 'r')

print(f.readlines())


f = open('numbers.txt', 'r')

# = f.readlines()
#data = [int(i) for i in data]
data = list(map(int,f.readlines()))
print(data)

f.close()

f = open('numbers.txt')
for line in f:
    print(line.strip())

f.close()

open('test_1.txt', 'w')

with open('test_1.txt', 'r') as ONE:
    with open("test_new.txt", "w") as SECOND:
        for line in ONE:
            SECOND.write(line)




