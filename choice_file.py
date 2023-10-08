from print_data import print_file


def choice_number_file():
    print_file()
    number = int(input("Select the file you want to work with\n"
                       "Write the number 1 or 2: "))
    while number < 1 or number > 2:
        number = int(input("Error!!!\n"
                           "Select the number 1 or 2: "))
    return number