from return_data_file import data_file


def change_row():
    data, nf = data_file()
    count_rows = len(data)
    number_row = int(input(f"Enter the number of row "
                           f"from 1 to {count_rows - 1}: "))
    while number_row < 1 or number_row > count_rows:
        number_row = int(input(f" Error! "
                               f"Enter the number of row "
                               f"from 1 to {count_rows}: "))
    name = input("Write your name: ")
    surname = input("Write your surname: ")
    birthdate = input("Write your date of birth: ")
    town = input("Write your place of residence: ")
    data[number_row - 1] = f'{number_row};{name};{surname};{birthdate};{town}\n'
    with open(f'Python/Seminars/8Seminar/db/data_{nf}.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)
    print("Data changed successfuly!")