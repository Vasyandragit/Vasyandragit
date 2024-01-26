files = [input() for _ in range(3)]

first_data = set()
with open(files[0], encoding='UTF-8') as first:
    for line in first.readlines():
        first_data |= set(line.split())

second_data = set()
with open(files[1], encoding='UTF-8') as second:
    for line in second.readlines():
        second_data |= set(line.split())

with open(files[2], 'w', encoding='UTF-8') as answer:
    print(*sorted(first_data ^ second_data), sep='\n', file=answer)