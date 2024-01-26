def secret_replace(text, **rules):
    code = ''
    for symb in text:
        if symb in rules.keys():
            code += rules.get(symb)[0]
            rules[symb] = rules[symb][1:] + (rules[symb][0],)
        else:
            code += symb
    return code

print(secret_replace("Hello, world!", l=("hi", "y"), o=("123", "z")))