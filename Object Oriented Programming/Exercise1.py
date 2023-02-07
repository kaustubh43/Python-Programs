class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def pur(self):
        """This function returns self"""
        print(f'Your cat {self.name} is purring')
        return self


# Instantiate 3 cats of object Cat
cat1 = Cat('Bill', 9)
cat2 = Cat('kitty', 3)
cat3 = Cat('Timu', 11)


def oldest(*args):
    return max(args)


def find_name(*args):
    for item in args:
        print(item.name, item.age)
        if old_age == item.age:
            return item.name


old_age = oldest(cat1.age, cat2.age, cat3.age)
cat_name = find_name(cat1, cat2, cat3)
print(f"Oldest age of cat is {old_age} years old and the name of the cat is {cat_name}")

print(cat1.pur().pur().pur())  # this statement is deduced to object.pur
