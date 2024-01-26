nums = [650975472, 591084323, 629700, 1504180, 577023,
8460612246, 42161437, 29409368, 58531725, 5725268, 2198001838,
796451, 69358, 7195510, 975628465, 9756641,
44200289, 126541, 979391, 93479581, 291170, 28987042, 86139603]

print('even:')
for num in nums:
    if eval(f"{len([i for i in str(num) if int(i) % 2 == 0])} \
                > {len([j for j in str(num) if int(j) % 2])}"):
        print(num, end=' ')
        nums.remove(num)
print()
print('odd:')
for num in nums:
    if eval(f"{len([i for i in str(num) if int(i) % 2 == 0])} \
                < {len([j for j in str(num) if int(j) % 2])}"):
        print(num, end=' ')
        nums.remove(num)
print()   
print('equal:')
for num in nums:
    if eval(f"{len([i for i in str(num) if int(i) % 2 == 0])} \
                == {len([j for j in str(num) if int(j) % 2])}"):
        print(num, end=' ')
        nums.remove(num)