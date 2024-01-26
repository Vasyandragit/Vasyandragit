def answer(func):
    
    def decorated(*args, **kwargs):
        return f"Результат функции: {func(*args, **kwargs)}"
    
    return decorated