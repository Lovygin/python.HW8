from delete_data import delete_row
from change_data import change_row
from add_data import add_row
from print_data import print_file
from search_data import searching_data
from copying_data import copying_row


def check_number(n):
    while n < 1 or n > 7:
        n = int(input("Error! There is no such command number!"
                      "Enter the number from 1 to 5\n"
                      "Select a function from the list:\n"
                      "1. Add\n"
                      "2. Remove\n"
                      "3. Change\n"
                      "4. Outputing\n"
                      "5. Searching data\n"
                      "6. Copy data\n"
                      "7. Exit\n"
                      "Write the number of the command: "))
    return n


def start_menu():
    command = None
    while command != 7:
        command = int(input("Hello!\n"
                            "Select a function from the list:\n"
                            "1. Add\n"
                            "2. Remove\n"
                            "3. Change\n"
                            "4. Outputing\n"
                            "5. Searching data\n"
                            "6. Copy data\n"
                            "7. Exit\n"
                            "Write the number of the command: "))
        command = check_number(command)
        if command == 1:
            add_row()
        elif command == 2:
            delete_row()
        elif command == 3:
            change_row()
        elif command == 4:
            print_file()
        elif command == 5:
            searching_data()
        elif command == 6:
            copying_row()
    print("Thank you for using our services. Come to us again!\n"
          "Good luck!")