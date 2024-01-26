with open("3.5\secret.txt", encoding="UTF-8") as file:
    code = file.read()

print(''.join(chr(ord(symb) & 255) for symb in code))
