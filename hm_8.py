import csv
import os
import re


def get_data():
    # создаем списки для хранения данных
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    # создаем список для хранения данных отчета
    main_data = [
        ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]

    # перебираем файлы с данными
    for file_name in ['info_1.txt', 'info_2.txt', 'info_3.txt']:
        # открываем файл и считываем данные
        with open(file_name) as file:
            file_data = file.read()

        # ищем значения параметров с помощью регулярных выражений
        os_prod = re.search(r'Изготовитель системы:\s*(.*)', file_data)
        os_name = re.search(r'Название ОС:\s*(.*)', file_data)
        os_code = re.search(r'Код продукта:\s*(.*)', file_data)
        os_type = re.search(r'Тип системы:\s*(.*)', file_data)

        # добавляем значения параметров в соответствующие списки
        os_prod_list.append(os_prod.group(1))
        os_name_list.append(os_name.group(1))
        os_code_list.append(os_code.group(1))
        os_type_list.append(os_type.group(1))

        # добавляем значения параметров в список данных отчета
        main_data.append([os_prod.group(1), os_name.group(1), os_code.group(1),
                          os_type.group(1)])

    return os_prod_list, os_name_list, os_code_list, os_type_list, main_data


def write_to_csv(file_name):
    # получаем данные
    os_prod_list, os_name_list, os_code_list, os_type_list, main_data = get_data()

    # открываем CSV-файл для записи
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)

        # записываем данные в файл
        for row in main_data:
            writer.writerow(row)

    print(f'Данные записаны в файл {file_name}')


# вызываем функцию для записи данных в CSV-файл
write_to_csv('report.csv')

class Road:

    def __init__(self, length, width, weigh, num_m):
        self._length = length
        self._width = width
        self.weigh = weigh
        self.num_m = num_m

    def weight_culculator(self):
        res = self._length * self._width * self.weigh * self.num_m
        if res >= 100 and res < 1000:
            print("{}м * {}м * {}кг * {}м = {}ц".format(self._length, self._width, self.weigh, self.num_m, res / 100))
        elif res >= 1000:
            print("{}м * {}м * {}кг * {}м = {}т".format(self._length, self._width, self.weigh, self.num_m, res / 1000))
        else:
            print("{}м * {}м * {}кг * {}м = {}кг".format(self._length, self._width, self.weigh, self.num_m, res))


if __name__ == '__main__':
    a = Road(20, 5000, 25, 0.05)
    a.weight_culculator()

import yaml

# Подготовка данных для записи в файл
data = {
     "items": ["computer", "printer", "keyboard", "mouse"],
    "items_quantity": 4,
    "items_price": {
        "computer": "200€-1000€",
        "keyboard": "5€-50€",
        "mouse": "4€-7€",
        "printer": "100€-300€"
    }
}

# Запись данных в файл в формате YAML
with open('file1.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True)

# Считывание данных из файла
with open('file1.yaml', 'r', encoding='utf-8') as f:
    loaded_data = yaml.safe_load(f)

# Проверка, что данные совпадают
assert data == loaded_data, "Данные в файле не совпадают с исходными!"