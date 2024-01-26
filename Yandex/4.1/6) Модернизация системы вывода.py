output = []


def modern_print(message):
    if message not in output:
        output.append(message)
        print(message)
