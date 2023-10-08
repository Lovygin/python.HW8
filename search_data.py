


def searching_data():
    request, flag = input("Write the data for searcing\n--> "), False
    for i in range(1, 3):
        with open(f'Python/Seminars/8Seminar/db/data_{i}.txt', 
                  'r', encoding = 'utf-8') as file:
            #file = list(file)
            for line in file:
                if request.lower() in line.lower():
                    flag = True
                    print(f'Here is the file:\n data_{i}.txt')
                    print(f'Here is the data:\n {line}')
    if flag:
        print('Data found! Congratulations!')
    else:
        print("Not found this information. I'm sorry.")
            
