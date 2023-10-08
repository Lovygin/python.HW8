from return_data_file import data_file
from choice_file import choice_number_file


def copying_row():
    data, nf = data_file()
    count_rows = len(data)
    if count_rows == 0:
        print("File is empty!")
    else:
        number_row = int(input(f"Write the number of row "
                               f"from 1 to {count_rows}: "))
        while number_row < 1 or number_row > count_rows:
            number_row = int(input(f"Error!!!"
                                   f"Write the number of row "
                                   f"from 1 to {count_rows}: "))
        dublicate = data[number_row - 1]
    
        nf = choice_number_file()

        with open(f'db/data_{nf}.txt', 'r+', encoding='utf-8') as file:
            data = file.readlines()
            if data[-1][-1] not in '\n':
                dublicate = f'\n{str(count_rows) + dublicate[1:]}'
            else:
                dublicate = f'{str(count_rows + 1) + dublicate[1:]}'
            file.write(dublicate)
            print(file)