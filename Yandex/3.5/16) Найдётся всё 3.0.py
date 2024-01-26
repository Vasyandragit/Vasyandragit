from sys import stdin


search, *files = [line.strip() for line in stdin]

flag = 0
for file in files:
    with open(file, encoding="UTF-8") as f:
        if search in ' '.join(f.read().replace('&nbsp;', ' ').lower().split()):
            print(file)
            flag = 1
            
if flag == 0:
    print('404. Not Found')