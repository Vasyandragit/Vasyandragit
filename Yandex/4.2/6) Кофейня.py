in_stock = {}


def order(*items):
    
    recipes = {"Эспрессо": [1, 0, 0], "Капучино": [1, 3, 0], "Макиато": [2, 1, 0],
          "Кофе по-венски": [1, 0, 2], "Латте Макиато": [1, 2, 1], "Кон Панна": [1, 0, 1]}
    
    for item in items:
        for i in range(3):
            
            if recipes[item][i] > list(in_stock.values())[i]:
                break
        else:
            for j in range(3):
                in_stock[list(in_stock.keys())[j]] -= recipes[item][j]
            return item
    return "К сожалению, не можем предложить Вам напиток"