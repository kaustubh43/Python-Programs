class Pets:
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

    def sing(self):
        pass


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    @staticmethod
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    @staticmethod
    def sing(self, sounds):
        return f'{sounds}'


class Billi(Cat):
    @staticmethod
    def sing(self, sounds):
        return f'{sounds}'


# 2 Create a list of all the pets (create 3 cat instances from the above)
my_cats = [Simon("Meow", 2), Sally("Miu", 5), Billi("Shoot", 3)]

# 3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)

# 4 Output all the cats walking using the my_pets instance
my_pets.walk()
