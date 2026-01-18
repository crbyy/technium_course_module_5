import itertools

#1
print("#1")
numbers = [1, 2, 3, 4]

for n in itertools.combinations(numbers, 2):
    print(n)


#2
print('\n#2')

text = 'Python'
letters = []
count = []

for l in text:
    letters.append(l)

for p in itertools.permutations(letters):
    print(p)
    count.append(p)
print(len(count))


#3
print('\n#3')

list1 = ['a', 'b']
list2 = [1, 2, 3]
list3 = ['x', 'y']
list_all = []

cycle1 = itertools.cycle(list1)
cycle2 = itertools.cycle(list2)
cycle3 = itertools.cycle(list3)
count = 0

for a, b, c in zip(cycle1, cycle2, cycle3):
    if count == 5:
        break
    list_all.append((a,b,c))
    count+=1
print(list_all)


#4
print('\n#4')

def fib():
    x, y = 0, 1
    for _ in itertools.count():
        yield x
        x, y = y, x + y

print(list(itertools.islice(fib(), 10)))


#5
print('\n#5')

l1 = ['red', 'blue']
l2 = ['shirt', 'shoes']

for l in itertools.product(l1,l2):
    print(l)



