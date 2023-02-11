class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def pur(self):
        """This function returns self"""
        print(f'Your cat {self.name} is purring')
        return self

    def __getitem__(self, item):    # Get item modified to get the values of other attributes
        if item == 'Name':
            return self.name
        elif item == 'Age':
            return self.age
        else:
            return None


# Instantiate 3 cats of object Cat
cat1 = Cat('Bill', 9)
cat2 = Cat('Kitty', 11)
cat3 = Cat('Timu', 11)


def oldest(*args):
    return max(args)


def find_name(*args):
    """Finds the cat names with the oldest age"""
    names = []
    for item in args:
        print(item.name, item.age)
        if old_age == item.age:
            names.append(item.name)
    return names


old_age = oldest(cat1.age, cat2.age, cat3.age)
cat_name = " ".join(find_name(cat1, cat2, cat3))  # joins the elements of the list
print(f"Oldest age of cat is {old_age} years old and the name of the cat are {cat_name}")

print(cat1.pur().pur().pur())  # this statement is deduced to object.pur

print(cat1['Age'])  # Calling __getitem__ makes our object subscript-able
