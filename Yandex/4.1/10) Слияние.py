def merge(tup1, tup2):
    temp1, temp2 = list(tup1), list(tup2)
    
    sortik = []
    while temp1 and temp2:
        if temp1[0] > temp2[0]:
            sortik.append(temp2.pop(0))
        else:
            sortik.append(temp1.pop(0))
    sortik += temp1 + temp2
    return tuple(sortik)
    

print(merge((7, 12), (1, 9, 50)))