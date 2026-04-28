import requests
from  collections import Counter

def main():
    while True:
        username = input("Введите имя пользователя Github: ").strip()
        repos = get_repos(username)

        if repos is not None:
            analyze_repos(repos)
            break


def get_repos(username):
    url = f'https://api.github.com/users/{username}/repos'
    response = requests.get(url)

    if response.status_code == 200:
        repos = response.json()
        print(f"Репозитории пользователя {username}: ")
        for repo in repos:
            print (f'- {repo['name']} (⭐{repo['stargazers_count']} stars)')
        return repos
    else:
        print(f'Не удалось получить данные. Код ошибки: {response.status_code}')

        if response.status_code == 403:
            print("Превышен лимит запросов")
        if response.status_code == 404:
            print("Такого пользователя не существует")
        return None


def analyze_repos(repos):

    overall_stars = []
    overall_lang = []
    for repo in repos:
        overall_stars.append(repo['stargazers_count'])
        overall_lang.append(repo['language'])

    #Популярный репозиторий
    max_stars_idx = overall_stars.index(max(overall_stars))
    max_repo_name = repos[max_stars_idx]['name']
    max_repo_stars = repos[max_stars_idx]['stargazers_count']

    print()
    print(f'Общее количество звезд: {sum(overall_stars)}')
    print(f"Количество публичных репозиториев: {len(repos)}")
    print(f'Самый популярный репозиторий: {max_repo_name} (⭐{max_repo_stars})')

    #Частый язык
    print()
    counter = Counter(overall_lang)
    counter = counter.most_common()
    print("Наиболее используемые языки: ")
    for lang in counter:
        if lang[1] == 1:
            word = 'репозиторий'
        elif 4 >= lang[1] >= 2:
            word = 'репозитория'
        elif lang[1] >=5:
            word = 'репозиториев'
        print(f"{lang[0]}: {lang[1]} {word}")
    print()


main()

#VK API
import os
import requests
from  collections import Counter

#tok = os.getenv("vk_tok")
tok = '2c4cc33b2c4cc33b2c4cc33bea2f0c6e7322c4c2c4cc33b45bdd06d7bcf633227020e99'
def main2():
    while True:
        user_id = input("Введите id пользователя vk: ") # 151576949
        if user_id:
            get_info(user_id)
            break
        else:
            print("Введите валидный id")

def get_info(user_id):
    url = (f'https://api.vk.ru/method/users.get?user_ids={user_id}&fields=online, bdate, about, '
           f'city, contacts, country, followers_count, interests, relation, career, status, friends'
           f'&access_token={tok}&lang=0&v=5.199')
    response = requests.get(url)

    if response.status_code == 200:
        info = response.json()
        user = info['response'][0]

        print(f"Информация пользователя {user.get('first_name', '')} {user.get('last_name', '')}: ")

        bdate = user.get('bdate', 'Нет данных')
        if bdate:
            print(f'Дата рождения: {bdate}')

        city = user.get('city', {})
        if city:
            print(f'Город: {city.get('title', 'Нет данных')}')

        interests = user.get('interests', 'Нет данных')
        if interests:
            print(f'Интересы: {interests}')

        about = user.get('about', 'Нет данных')
        if about:
            print(f'О пользователе: {about}')

        status = user.get('status', 'Нет данных')
        if status:
            print(f'Статус: {status}')

        followers = user.get('followers_count', 0)
        print(f'Количество подписчиков: {followers}')

        career = user.get('career', {})
        if career:
            print("Карьера:")
            for job in career:
                company = job.get('company') or f'vk.com/club{job.get('group_id','')}'
                position = job.get('position', 'Нет данных')
                period = f'{job.get('from', '')} - {job.get('until', 'по настоящее время')}'
                print(f'- {company}')
                if position:
                    print(position)
                print(period)


        relation_dict = {0:'Не указано' , 1:'Не женат/не замужем;', 2:'Есть друг/есть подруга',
                         3:'Помолвлен/помолвлена' , 4:'Женат/замужем' , 5:'Всё сложно' ,
                         6:'В активном поиске;' , 7:'Влюблён/влюблена' , 8:'В гражданском браке'}
        relation = user.get('relation', 0)
        print(f'Семейное положение: {relation_dict.get(relation, 'Не указано')}')\

        online = user.get('online', 0)
        if online == 1:
            print("Статус: В сети")
        else:
            print("Статус: Не сети")

    else:
        print(f'Не удалось получить данные. Код ошибки: {response.status_code}')

        if response.status_code == 403:
            print("Превышен лимит запросов")
        if response.status_code == 404:
            print("Такого пользователя не существует")
        return None


main2()



