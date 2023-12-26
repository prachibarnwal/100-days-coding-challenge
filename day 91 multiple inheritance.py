class Mammal:
    def mammal_info(self):
        print("Mammals can give Direct Birth.")

class Animal:
    def animal_info(self):
        print("Winged Animals can Flap.")

class Bat(Mammal, Animal):
    def display(self):
        Mammal.mammal_info(self)
        Animal.animal_info(self)

#creating an object of Bat class
b1 = Bat()
b1.display()
