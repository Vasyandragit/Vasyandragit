from itertools import combinations


def multiple_sum(*numbers, div=2):
    if sum(numbers) % div:
        sum_list = []
        for i in range(len(numbers) - 1, 0, -1):
            for comb in combinations(numbers, i):
                if sum(comb) % div == 0:
                    sum_list.append(sum(comb))
    else:
        return sum
    return max(sum_list)

print(multiple_sum(1, 2, 3, 4, 5))