'''
Задача №49. Решение в группах
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
'''
from csv import DictWriter, DictReader
from os.path import exists
from tempfile import NamedTemporaryFile
import shutil
tempfile = NamedTemporaryFile('w+t', newline='', delete=False)

file_name = 'phone.csv'

def get_info(first_name="Ivan", last_name="Ivanov"):
    flag = False
    while not flag:
        try:
            phone_number = int(input('Введите номер телефона: '))
            if len(str(phone_number)) != 11:
                print("Наверная длина номера")
            else:
                flag = True     
        except ValueError:
            print("Невалидный номер")
        
    return [first_name, last_name, phone_number]

def create_file(filename):
    with open(filename, 'w', encoding='utf-8') as data:
        f_w = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r)

def write_file(filename, lst):
    res = read_file(filename)
    obj = {"Имя": lst[0], "Фамилия": lst[1], "Телефон": lst[2]}
    res.append(obj)
    with open(filename, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()
        f_w.writerows(res)

'''
Дополнить справочник возможностью копирования данных из одного файла в другой. 
Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.
'''
def copy_line(file_name, line_num):
    with open(file_name,'r', encoding='utf-8', newline='') as firstfile, open(input("Имя файла назначения: "),'a', encoding='utf-8', newline='') as secondfile: 
        count = 0
        for line in firstfile: 
            if count == int(line_num):
                secondfile.write(line)
                return
            count += 1


def delete_item_from_file(file_name, item):
    pass



def main():
    while True:
        command = input("Введите команду: ")
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == 'r':
            if not exists(file_name):
                print("Файл отсутствует, создайте его")
                continue
            print(*read_file(file_name))
        elif command == 'c':
            if not exists(file_name):
                create_file(file_name)
            copy_line(file_name, input("Введите существующий номер строки: "))
main()