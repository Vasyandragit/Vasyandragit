class Programmer:
    def __init__(self, name, place, exp=0, capital=0):
        self.name = name
        self.place = place
        self.exp = exp
        self.capital = capital
        
        wages = {"Junior": 10, "Middle": 15, "Senior": 20}
        self.wage = wages[self.place]
    
    def work(self, time):
        self.exp += time
        self.capital += self.wage * time
    
    def rise(self):
        if self.wage < 15:
            self.place, self.wage = "Middle", 15
        elif self.wage < 20:
            self.place, self.wage = "Senior", 20
        else:
            self.wage += 1
        
    def info(self):
        return f"{self.name} {self.exp}ч. {self.capital}тгр."
            
        
    