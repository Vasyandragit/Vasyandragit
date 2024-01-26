import json

name_txt, name_json = input(), input()
nums = []
with open(name_txt) as file_txt:
    for line in file_txt.readlines():
        for num in line.rstrip('\n').split():
            nums.append(int(num))

stats = {}
stats['count'], stats['positive_count'] = len(nums), len([num for num in nums if num > 0])
stats['min'], stats['max'] = min(nums), max(nums)
stats['sum'], stats['average'] = sum(nums), f'{sum(nums) / len(nums):.2f}'

with open(name_json, 'w') as file_json:
    json.dump(stats, file_json, indent=2) 