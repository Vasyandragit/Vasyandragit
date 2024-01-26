from sys import stdin
import json

answers = [line.rstrip() for line in stdin]

with open("3.5\scoring.json", encoding="UTF-8") as score_file:
    scoring = json.load(score_file)

point_sum = 0
for score in scoring:
    good_ans = score["points"] // len(score["tests"]) 
    for test in score["tests"]:
        if answers.pop(0) == test["pattern"]:
            point_sum += good_ans
print(point_sum)