import os

def get_words(text):
    text_str = str(text).lower()
    punc = '?!-,.":'

    for p in punc:
        text_str = text_str.replace(p, '')

    text_str = text_str.replace('\n', ' ').split()
    return text_str

def get_words_dict(dic):
    print(f"Кол-во слов: {len(dic)}")
    print(f"Кол-во уникальных слов: {len(set(dic))}")
    words_dict = {}
    for word in dic:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1

    words_dict_sorted = dict(sorted(words_dict.items(), key=lambda item: item[1], reverse=True))
    print("Все использованные слова: ")
    for key, value in words_dict_sorted.items():
        print (f"{key}: {value}")



folder = 'D:\\Technium'
input_file = input("Введите название файла: ")

file_path = os.path.join(folder, f'{input_file}.txt')

if os.path.exists(file_path):
    with open(file_path, 'r', encoding = 'utf-8') as file:
        split_words = get_words(file.read())
        get_words_dict(split_words)
else:
    print("Такого файла не существует!")

