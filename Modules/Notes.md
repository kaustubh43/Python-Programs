# Modules in Python
>Programs need to be distributed over different files
> 
> Functions can be imported from files called modules
>
#### main.py 
```
import utility  #used to import a module

print(utility.divide(2, 3))
print(utility.multiply(2, 3))
```
#### utility.py
```
def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

```
### Packages
> Many modules wrapped in a directory form a package, packages can be imported too
> 
``` 
import utility  # used to import a module
import shopping.shopping_cart  # Used to import a package. 
# Syntax: import directoryname.modulename

print(utility.divide(2, 3))
print(utility.multiply(2, 3))
print(shopping.shopping_cart.buy('Apple'))
```
> if a directory has an __init__.py file then python interpreter knows that it's a python package
> 
> Great devs organise their code will into packages and modules and keep their files organised
> 
``` 
# different way of importing
from shopping.more_shopping.shopping_cart import buy
print(buy('Apple'))  # can directly use buy() function without referring the module/package name

```

``` 
# Importing multiple functions from a module
from utility import multiply, divide
print('short', divide(2, 3))
print('short', multiply(2, 3))
```

``` 
# different way of importing
from shopping.more_shopping import shopping_cart #Use this method so that you dont override built in functions
print(shopping_cart.buy('Apple'))  # can directly use buy() function without referring the module/package name

```
> Be explicit and mention what you want to import exactly to avoid over-riding built-in functions
```
# This is the preferred way of importing functions from a module/package
from utility import multiply, divide
```

#### Modules and packages help in good engineering practices and build big projects in an organised fashion yet still have all the files talk to each other.
