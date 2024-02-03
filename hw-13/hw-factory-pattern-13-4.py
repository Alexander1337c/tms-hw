from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return self.__class__.__name__


class Cat(Animal):
    def speak(self):
        return self.__class__.__name__


class AnimalFactory:
    @classmethod
    def create_animal(cls, pet):
        if pet == 'dog':
            return Dog()
        elif pet == 'cat':
            return Cat()
        else:
            raise ValueError('Unknown animal')


Boris = AnimalFactory.create_animal('dog')
print(Boris.speak())

Vasek = AnimalFactory.create_animal('cat')
print(Vasek.speak())
