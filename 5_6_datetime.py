import datetime
#1
now = datetime.datetime.now()

days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
day_name = days[now.weekday()]
print(day_name)

try:
    datetime.date(now.year, 2, 29)
    result = "Год високосный"
except ValueError:
    result = "Год невисокосный"

print(result)


#2
input_date = input('Введите дату в формате "год-месяц-день": ')
parsed_date = datetime.datetime.strptime(f'{input_date}', "%Y-%m-%d")
str_parsed_date = parsed_date.strftime("%Y-%m-%d")
difference = parsed_date - now
print(f'До даты {str_parsed_date} осталось {difference.days} дней.')

days = difference.days
hours = difference.seconds // 3600
minutes = (difference.seconds % 3600) // 60

print(f"Разница: {days} дней, {hours} часов, {minutes} минут")
