
#Задача1
def find_best_deals(data):
    # Разделяем входные данные на заголовок и информацию о магазинах
    header = data[0][1:].split('\t')
    stores_data = data[1:]

    # Создаем словарь для хранения цен по каждой книге
    book_prices = {}

    # Извлекаем информацию о книгах и ценах из каждой строки данных
    for row in stores_data:
        store_data = row.split('\t')
        store_name = store_data[0]
        prices = list(map(int, store_data[1:]))

        # Используем функцию zip, чтобы объединить заголовок и цены вместе
        for book, price in zip(header, prices):
            if book not in book_prices:
                book_prices[book] = {}

            book_prices[book][store_name] = price

    # Ищем самый выгодный магазин для каждой книги
    best_deals = []
    for book, prices in book_prices.items():
        best_store = min(prices, key=prices.get)
        best_price = prices[best_store]
        best_deals.append((book, best_store, best_price))

    # Сортируем результаты по порядку книг из заголовка
    best_deals.sort(key=lambda x: header.index(x[0]))

    return best_deals


# Пример входных данных
input_data = [
    '\tBook1\tBook2\tBook3',
    'Store1\t10\t20\t15',
    'Store2\t12\t18\t20',
    'Store3\t8\t25\t17'
]

result = find_best_deals(input_data)

# Вывод результатов
print("Название самого выгодного магазина:")
print(result[0][1])
print("Наименование книги\tЦена")
for book, store, price in result:
    print(f"{book}\t{price}")

#Задача2

from itertools import product

# Функция для генерации колоды карт без выброшенной масти
def generate_deck(suit_to_exclude):
    # Определяем номиналы и масти
    ranks = [str(num) for num in range(2, 11)] + ['валет', 'дама', 'король', 'туз']
    suits = ['пик', 'треф', 'бубен', 'червей']

    # Удаляем выброшенную масть из списка мастей
    suits.remove(suit_to_exclude)

    # Используем итератор product для комбинирования номиналов и мастей
    deck = list(product(ranks, suits))

    return deck

# Ввод выброшенной масти от пользователя
suit_to_exclude = input("Введите масть, которую необходимо выбросить (пик, треф, бубен, червей): ")

# Генерация и вывод колоды карт без выброшенной масти
deck = generate_deck(suit_to_exclude)

# Сортировка колоды по увеличению номинала, затем масти
deck.sort(key=lambda card: (card[0], card[1]))

# Вывод колоды карт на экран
for card in deck:
    print(f"{card[0]} {card[1]}")

#Задача3

from itertools import groupby

# Функция для группировки столиц по интервалам численности
def group_capitals(capitals):
    # Сортируем столицы по численности населения
    capitals.sort(key=lambda x: x[1])

    # Группируем столицы по интервалам численности
    grouped_capitals = []
    for key, group in groupby(capitals, lambda x: x[1] // 100000):
        interval = key * 100
        capitals_in_interval = sorted(list(group), key=lambda x: x[0])
        grouped_capitals.append((interval, capitals_in_interval))

    return grouped_capitals

# Список столиц соответствующий формату (столица, численность)
capitals = [
    ('Москва', 12500000),
    ('Токио', 13929286),
    ('Пекин', 21700000),
    ('Лондон', 8908081),
    ('Нью-Йорк', 8405837),
    ('Берлин', 3769000),
    ('Париж', 2140526),
    ('Рим', 2870500),
]

# Группировка столиц по интервалам численности
grouped_capitals = group_capitals(capitals)

# Вывод интервалов численности и соответствующих столиц
for interval, capitals_in_interval in grouped_capitals:
    print(f" {interval}-{interval+100}:")
    for capital in capitals_in_interval:
        print(capital[0])
    print()

#Задача4

import sys

def format_comment(line_number, comment):
    return f"Line {line_number}: {comment}"

def process_comments(input_lines):
    comments = []

    for line_number, line in enumerate(input_lines, start=1):
        line = line.rstrip('\n')
        stripped_line = line.lstrip('# ').rstrip()
        if stripped_line:
            comments.append(format_comment(line_number, stripped_line))

    return comments

# Ввод
input_lines = [
    "    # rstrip(’\n’) \"отрезает\" от строки line,",
    "    # идущий справа символ перевода строки,",
    "    # ведь print сам переводит строку"
]

# Обработка комментариев
comments = process_comments(input_lines)

# Вывод комментариев
for comment in comments:
    print(comment)

#Задача5

import random

# Чтение случайной строки из файла
def read_random_line(filename):
    line = None
    count = 0

    with open(filename, 'r', encoding='utf-8') as file:
        for current_line in file:
            count += 1
            if random.randint(1, count) == 1:
                line = current_line.rstrip('\n')

    return line

# Путь к файлу
filename = "lines.txt"

# Чтение случайной строки из файла
random_line = read_random_line(filename)



# Вывод случайной строки, если она существует
if random_line is not None:
    print(random_line)

#Задача6

import csv

def find_longest_decreasing_sequence(data):
    start_index = 0
    max_length = 0

    current_index = 0
    current_length = 1

    for i in range(1, len(data)):
        if data[i] <= data[i-1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                start_index = current_index
            current_index = i
            current_length = 1

    if current_length > max_length:
        max_length = current_length
        start_index = current_index

    return start_index, start_index + max_length - 1

# Чтение данных из файла
filename = "alpha_oriona.csv"

data = []
with open(filename, 'r') as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        luminosity = int(row['luminosity'])
        data.append(luminosity)

# Поиск наибольшей невозрастающей последовательности
start_index, end_index = find_longest_decreasing_sequence(data)

# Получение даты и времени начала последовательности
start_date_time = None
with open(filename, 'r') as file:
    reader = csv.reader(file, delimiter=';')
    for i, row in enumerate(reader):
        if i == start_index:
            start_date_time = row[0] + ' ' + row[1]
            break

# Запись результатов в файл
result_filename = "result.txt"
with open(result_filename, 'w') as file:
    file.write(f"Length: {end_index - start_index + 1}\n")
    file.write(f"Start Date Time: {start_date_time}\n")

# Вывод результатов на экран
print(f"Length: {end_index - start_index + 1}")
print(f"Start Date Time: {start_date_time}")


