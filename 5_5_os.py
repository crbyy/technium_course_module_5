import os
import shutil

print(os.getcwd())

base_path = os.getcwd()
dname = "Управление_файлами"

os.makedirs(dname, exist_ok=True)

os.chdir(os.path.join(base_path, dname))

print(os.getcwd())

with open('file1.txt', 'w', encoding='utf-8') as f1:
    f1.write("Привет!")

with open('file2.txt', 'w', encoding='utf-8') as f2:
    f2.write("Hello!")

print(os.listdir(os.getcwd()))

file_path  = os.path.join(os.getcwd(), 'file1.txt')
os.remove(file_path)

print(os.listdir(os.getcwd()))

sub_dir = os.path.join(base_path,dname, 'Подпапка')

os.makedirs(sub_dir, exist_ok=True)
print((os.getcwd()))

shutil.move(os.path.join(base_path,dname, 'file2.txt'), sub_dir)

os.chdir(base_path)
print((os.getcwd()))
shutil.rmtree('Управление_файлами')








