file_name1, file_name2 = input(), input()

formated_lines = []
with open(file_name1, encoding='UTF-8') as bad_format:
    for line in bad_format.readlines():
        line = line.replace('\t', '').replace('\n', '').split()
        if line:
            line = [word.strip() for word in line]
            formated_lines.append(' '.join(line))
            
with open(file_name2, 'w', encoding='UTF-8') as nice_format:
    print(*formated_lines, sep='\n', file=nice_format)