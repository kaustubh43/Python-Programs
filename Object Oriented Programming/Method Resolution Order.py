class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass

    #     A
    #   /   \
    #  /     \
    # B       C
    #  \     /
    #   \   /
    #     D


print(D.num)  # Doesn't print num belonging to A, but prints num of C due to Method Resolution Order
print(D.mro())  # Prints MRO Order of class D
# Object.mro is a good way to find out object class relations in terms of inheritance
print(D.__mro__)  # Prints MRO Order of class D
