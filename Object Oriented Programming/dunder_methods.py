class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }

    def __del__(self):  # Deletes the object, we can override the dunder methods
        print('Deleted')

    def __call__(self):
        print("Yes????")
        return f'Called {self.color}'

    def __getitem__(self, item):
        return self.my_dict[item]


action_figure = Toy('Red', 0)
print(action_figure.__str__())
print(str(action_figure))
print(action_figure)
print(action_figure())
print(action_figure['name'])  # Allows us to subscript an object and get a value from the dictionary
del action_figure  # deleting object
