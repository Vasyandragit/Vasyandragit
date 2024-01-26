file_name = input()
how_many_lines = int(input())

with open(file_name, encoding='UTF-8') as hvost:
    print(*hvost.readlines()[-how_many_lines:], sep='')