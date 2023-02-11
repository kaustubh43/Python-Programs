class SuperList(list):  # Extending functionality of list
    def __init__(self):
        super().__init__()

    def __len__(self):
        return 1000


super_list = SuperList()
print(len(super_list))
super_list.append(10)
print(super_list)
print(id(super_list))
print(super_list[0])
print('Is SuperList subclass of list class which comes built in in python: ', issubclass(SuperList, list))
