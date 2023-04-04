"""
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий список. Должно получиться
четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции создать главный список для
хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

"""
import re
import csv

files = [
    'info_1.txt',
    'info_2.txt',
    'info_3.txt',
]


def get_data():
    main_data = [
        ["Изготовитель системы", "Название ОС", "Код продукта", "Тип системы"],
    ]

    prod_pattern = re.compile(r'(?:Изготовитель системы:\s+)(?P<prod>\w+)')
    name_pattern = re.compile(r'(?:Название ОС:\s+)(?P<name>\w+\s\w+\s\w+\.?\w?\s\w+)')
    code_pattern = re.compile(r'(?:Код продукта:\s+)(?P<code>\w+\-\w+\-\w+\-\w+)')
    type_pattern = re.compile(r'(?:Тип системы:\s+)(?P<type>\S+\s?PC)')
    for file in files:
        rez = list_creator()
        with open(file, "r") as f:
            for line in f.readlines():
                prod = re.search(prod_pattern, line)
                if prod:
                    rez.append(prod.group('prod'))
                    # print(prod.group('prod'))
                name = re.search(name_pattern, line)
                if name:
                    rez.append(name.group('name'))
                    # print(name.group('name'))
                code = re.search(code_pattern, line)
                if code:
                    rez.append(code.group('code'))
                    # print(code.group('code'))
                t = re.search(type_pattern, line)
                if t:
                    rez.append(t.group('type'))
                    # print(t.group('type'))
        main_data.append(rez)
    return main_data


def list_creator():
    return list()


get_data()

"""
[['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы'], 
 ['Microsoft Windows 7 Профессиональная', '00971-OEM-1982661-00231', 'LENOVO', 'x64-based PC'],
 ['Microsoft Windows 10 Professional', '00971-OEM-1982661-00231', 'ACER', 'x64-based PC'], 
 ['Microsoft Windows 8.1 Professional', '00971-OEM-1982661-00231', 'DELL', 'x86-based PC']]
 """

"""
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(), а также сохранение подготовленных данных
в соответствующий CSV-файл; Проверить работу программы через вызов функции write_to_csv().
"""


def write_to_csv():
    data = get_data()
    with open('main_data.csv', 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        for line in data:
            writer.writerow(line)
    with open('main_data.csv') as f:
        print(f.read())


write_to_csv()
