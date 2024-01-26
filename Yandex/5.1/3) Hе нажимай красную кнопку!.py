class RedButton:
    def __init__(self, counter=0):
        self.counter = counter
    
    def click(self):
        print("Тревога!")
        self.counter += 1
    
    def count(self):
        return self.counter