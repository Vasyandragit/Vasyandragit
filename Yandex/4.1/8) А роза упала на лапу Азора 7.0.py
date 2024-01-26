def is_palindrome(obj):
    
    if type(obj) == int:
        return str(obj) == str(obj)[::-1]
    
    return obj == obj[::-1]
        