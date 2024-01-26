from sys import stdin
import json

lines = [line.rstrip() for line in stdin.readlines()]

with open(lines[0]) as file:
    data = json.load(file)

for line in lines:
    pair = line.split(' == ')
    data[pair[0]] = pair[1]

with open(lines[0], 'w') as upd_file:
    json.dump(data, upd_file, ensure_ascii=False, indent=4)
