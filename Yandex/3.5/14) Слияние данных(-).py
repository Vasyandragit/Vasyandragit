import json


user_file, update_file = input(), input()

with open(user_file, encoding="UTF-8") as old:
    data = json.load(old)

with open(update_file, encoding="UTF-8") as upd:
    data |= json.load(upd)

with open(user_file, encoding="UTF-8") as new:
    json.dump(new, data, ensure_ascii=False, )