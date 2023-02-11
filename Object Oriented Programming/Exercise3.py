# By reading the python documentation, add 3 more magic/dunder methods of your choice to this Toy class.
class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False,
        }

    def __str__(self):
        return f"{self.color}"

    def __len__(self):
        return 5

    def __del__(self):
        return "deleted"

    def __call__(self):
        return 'yes?'

    def __getitem__(self, i):
        return self.my_dict[i]

    def __add__(self, *other):  # Added by Kaustubh Ajgaonkar
        return sum(other)

    def __le__(self, other):  # Added by Kaustubh Ajgaonkar
        return self.age <= other

    def __reduce__(self,):  # Added by Kaustubh Ajgaonkar
        return 'Reducto'


action_figure = Toy('red', 5)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure['name'])

print(action_figure.__add__(4, 5, 6, 8, 9))
print(f'is older? {action_figure.__le__(5)}')
print(action_figure.__reduce__())
