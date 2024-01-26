def can_eat(coords0, coords1):
    modx, mody = abs(coords0[0] - coords1[0]), abs(coords0[1] - coords1[1])
    
    if (modx, mody) in ((1, 2), (2, 1)):
        return True
    return False

print(can_eat((5, 5), (6, 6)))