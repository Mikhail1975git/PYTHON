#Домашнее задание

# 55. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
        "1. Отобразить весь справочник\n"
        "2. Найти абонента по фамилии\n"
        "3. Найти абонента по номеру телефона\n"
        "4. Добавить абонента в справочник\n"
        "5. Сохранить справочник в текстовом формате\n"
        "6. Закончить работу")
    choice = int(input())
    return choice

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phon.txt')


    while (choice != 6):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            name = get_search_name()
            print(find_by_name(phone_book, name))
        elif choice == 3:
            number = get_search_number()
            print(find_by_number(phone_book, number))
        elif choice == 4:
            user_data = get_new_user()
            #add_user(phone_book, user_data)
            write_txt2('phon.txt', phone_book, user_data)
        elif choice == 5:
            file_name = get_file_name()
            write_txt3(file_name, phone_book)
        choice = show_menu()

def read_txt(filename):
    #with open(filename, 'r', encoding='utf-8') as fin:
            
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data
    #print(fin.readlines())

def print_result(data: list):
    for el in data:
        s = ''
        for v, k in el.items():
            s += f'{v}: {k}\n'
        print(s)
    print(data)

def write_txt(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:

        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')    

def get_search_name():
    return input ('Введите фамилию для поиска')

def find_by_name(data: list, name):
    for j in data:
        if j.get('Фамилия')==name:
            return j.get("Телефон")
    else:
        return ("Нет такого абонента в списке")
        
def get_search_number():
    return input ('Введите номер для поиска')

def find_by_number(data: list, number: int):
    for j in data:
        if j.get('Телефон')==number:
            return j.get("Фамилия")
    else:
        return ("Нет такого абонента в списке")

def get_new_user():
    return input('Фамилия, Имя, Телефон, Описание')

def write_txt2(filename, phone_book, user_data: str):
    with open('phon.txt', 'a', encoding='utf-8') as fout:
        fout.write(f'{user_data[:-1]}\n') 

def get_file_name():
    return input('Введите имя файла')
def write_txt3(file_name, phone_book):
    with open(file_name, 'a', encoding='utf-8') as fout:
        fout.write(f'{phone_book[:-1]}\n')
    

work_with_phonebook()



