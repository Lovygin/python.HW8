


def print_file():
    for i in range(1, 3):
        with open(f'Python/Seminars/8Seminar/db/data_{i}.txt', 
                  'r', encoding = 'utf-8') as file:
            data = file.readlines()
        print(f'Outputing data from {i} file :\n'
              f'{"".join(data)}')
        print()