name = input()
nums = []
with open(name) as f:
    for line in f.readlines():
        for num in line.rstrip('\n').split():
            nums.append(int(num))

print(len(nums), len([num for num in nums if num > 0]), 
min(nums), max(nums), sum(nums), f'{sum(nums) / len(nums):.2f}', sep='\n')