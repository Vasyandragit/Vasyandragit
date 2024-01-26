def make_linear(sp):
    linear = []
    for i in sp:
        if isinstance(i, list):
            linear += make_linear(i)
        else:
            linear.append(i)
    
    return linear
    
    