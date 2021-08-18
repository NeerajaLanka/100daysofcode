class Animal:
    def __init__(self):
        self.num_eyes = 2
    def breath(self):
        print("inhale,exhale")
class Fish(Animal):
    def __init__(self):
        super().__init__()
    def breath(self):
        super().breath() 
        print("doing this underwater ")  
    def swim(self):
        print("more in water")

gold_fish =Fish()
gold_fish.swim()
gold_fish.breath()
print(gold_fish.num_eyes)