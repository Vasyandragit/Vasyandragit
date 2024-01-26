file_in = input()
files_out = {input(): ">", input(): "<", input(): "=="}


nums = []
with open(file_in) as numbers:
    for line in numbers.readlines():
        nums.append([abs(int(num)) for num in line.split()])


for file in files_out.keys():
    with open(file, "w") as f:
        for line in nums:
            for num in line:
                if eval(f"{len([i for i in str(num) if int(i) % 2 == 0])} \
                {files_out[file]} {len([j for j in str(num) if int(j) % 2])}"):
                    print(num, end=' ', file=f)
            print('\n', end='', file=f)
