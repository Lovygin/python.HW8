from return_data_file import data_file


def add_row():
    name = input("Write your name: ")
    surname = input("Write your surname: ")
    birthdate = input("Write your date of birth: ")
    town = input("Write your place of residence: ")
    data, nf = data_file()
    now_number_row = len(data) + 1
    with open(f'db/data_{nf}.txt', 'a', encoding='utf-8') as file:
        file.write(f'{now_number_row};{name}; '
                   f'{surname};{birthdate};{town}\n')
    print("Data added successfuly!")
  