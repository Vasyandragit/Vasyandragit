def same_type(fu):
    def decorated(*args):
        if len(set(type(arg) for arg in args)) > 1:
            print("Обнаружены различные типы данных")
            return False
        return fu(*args)
    return decorated