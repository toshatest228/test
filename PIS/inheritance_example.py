class Animal:
    def speak(self):
        print("Тварина видає звук")

class Dog(Animal): # Dog наслідує Animal
    def speak(self):
        print("Собака гавкає: Гав-гав!")

my_dog = Dog()
my_dog.speak()
