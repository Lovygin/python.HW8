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
    
        if nf == 1:
            with open(f'Python/Seminars/8Seminar/db/data_{nf + 1}.txt', 'r+', encoding='utf-8') as file:
                #lines = file.readlines() #чтение всех строк из файла - дорого
                file.seek(0,2) # Перемещаем курсор к последнему символу в файле
                has_newline = file.tell() > 0 # Проверка, есть ли символы в последней строке (длина больше 0?)
                if has_newline:
                    dublicate = f'\n{str(count_rows + 1) + dublicate[1:]}\n'
                else:
                    dublicate = f'{str(count_rows + 1) + dublicate[1:]}\n'
                file.write(dublicate)
        else:
            with open(f'Python/Seminars/8Seminar/db/data_{nf - 1}.txt', 'r+', encoding='utf-8') as file:
                file.seek(0,2) # Перемещаем курсор к последнему символу в файле
                has_newline = file.tell() > 0 # Проверка, есть ли символы в последней строке (длина больше 0?)
                if has_newline:
                    dublicate = f'\n{str(count_rows + 1) + dublicate[1:]}\n'
                else:
                    dublicate = f'{str(count_rows + 1) + dublicate[1:]}\n'
                file.write(dublicate)

