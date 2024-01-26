shift = int(input())
alphabet = "abcdefghijklmnopqrstuvwxyz"

with open("3.5\public.txt", encoding="UTF-8") as text_file:
    code = ""
    for symb in text_file.read():
        coded_symb = alphabet[(alphabet.find(symb.lower()) + shift) %
                              len(alphabet)] if symb.lower() in alphabet else symb
        code += coded_symb.upper() if symb.isupper() else coded_symb

with open("3.5\private.txt", 'w', encoding="UTF-8") as caesar_file:
    print(code, file=caesar_file)
