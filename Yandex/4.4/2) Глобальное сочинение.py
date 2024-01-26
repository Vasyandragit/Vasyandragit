words = ""
count = 0

def add_word(word):
    global words, count
    words += f"{word}, "
    count += 1

def get_work():
    return f"{words[:-2]}. ({count})"
    
  

add_word("мама")
add_word("мыла")
print(get_work())
add_word("раму")
print(get_work())