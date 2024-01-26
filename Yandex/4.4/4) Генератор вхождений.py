def rindex(text):
    gen = []
    letters = sorted(set(text))
    letters.remove(' ')
    for let in letters:
        yield(let, text.rfind(let))
        
    
        
print(rindex('Мама мыла раму'))