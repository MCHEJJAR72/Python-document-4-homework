Object-Oriented-Programming (OOP)
Tasks Today:
Creating a Class (Initializing/Declaring)
Using a Class (Instantiating)
     a) Creating One Instance
     b) Creating Multiple Instances
     c) In-Class Exercise #1 - Create a Class 'Car' and instantiate three different makes of cars
The __init__() Method
     a) The 'self' Attribute
Class Attributes
     a) Initializing Attributes
     b) Setting an Attribute Outside of the __init__() Method
     c) Setting Defaults for Attributes
     d) Accessing Class Attributes
     e) Changing Class Attributes
     f) In-Class Exercise #2 - Add a color and wheels attribute to your 'Car' class
Class Methods
     a) Creating
     b) Calling
     c) Modifying an Attribute's Value Through a Method
     d) Incrementing an Attribute's Value Through a Method
     e) In-Class Exercise #3 - Add a method that prints the cars color and wheel number, then call them
Inheritance
     a) Syntax for Inheriting from a Parent Class
     b) The __init__() Method for a Child Class (super())
     c) Defining Attributes and Methods for the Child Class
     d) Method Overriding
     e) In-Class Exercise #4 - Create a class 'Ford' that inherits from 'Car' class and initialize it as a Blue Ford Explorer with 4 wheels using the super() method
Classes as Attributes
Exercises
     a) Exercise #1 - Turn the shopping cart program from yesterday into an object-oriented program
Creating a Class (Initializing/Declaring)
When creating a class, function, or even a variable you are initializing that object. Initializing and Declaring occur at the same time in Python, whereas in lower level languages you have to declare an object before initializing it. This is the first step in the process of using a class.

# The idea or blueprint for a car
class Car():
    wheels = 4
    color = 'blue'
    windshield_wipers = 'wee woo wee woo'
    
    def headlights():
        print("Turn them on for safety!")

volskwagen = Car()
volkswagen.headlights()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Input In [38], in <cell line: 11>()
      8         print("Turn them on for safety!")
     10 volskwagen = Car()
---> 11 volkswagen.headlights()

NameError: name 'volkswagen' is not defined
Using a Class (Instantiating)
The process of creating a class is called Instantiating. Each time you create a variable of that type of class, it is referred to as an Instance of that class. This is the second step in the process of using a class.

Creating One Instance
ford = Car()
# access something inside of this class
print(ford.windshield_wipers)
wee woo wee woo
Creating Multiple Instances
chevrolet = Car()
honda = Car()
porsche = Car()

print(type(porsche.color))
<class 'str'>
In-Class Exercise #1 - Create a Class 'Car' and Instantiate three different makes of cars
# Is this correct? I had to use the 'pass' statement to get it to work with __init__.
# doors, color, wheels

class Car():
    pass

toyota = Car()
toyota.doors = 4
toyota.color = "red"
toyota.wheels = 4

ford = Car()
ford.doors = 2
ford.color = "blue"
ford.wheels = 4

honda = Car()
honda.doors = 4
honda.color = "black"
honda.wheels = 4

print(toyota.color)
print(ford.doors)
print(honda.wheels)
red
2
4
The __init__() Method
This method is used in almost every created class, and called only once upon the creation of the class instance. This method will initialize all variables needed for the object.

class Car():
    engine = '4.7L'# Global within class - any method inside the class can call upon this variable
    
    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels
    
mazda = Car('black', 4)
subaru = Car('blue', 6)

print(mazda.color)
print(subaru.color)
print(mazda.wheels)
print(subaru.wheels)
black
blue
4
6
The 'self' Attribute
This attribute is required to keep track of specific instance's attributes. Without the self attribute, the program would not know how to reference or keep track of an instance's attributes.

# see above

class House():
    
    def __init__(self, wall, dishes):
        self.wall = wall
        self.dishes = dishes
        
    def washDishes(self):
        if self.dishes.lower() == 'dirty':
            return 'Clean'
        
    def rockClimbingWall(self, wall):
        if self.wall.lower() == 'yes':
            return 'rock on, climber!'
        else:
            return "Why wouldn't you want a rock climbing wall?"
        
brandon_house = House('dirty', 'no')

brandon_house.washDishes()
brandon_house.rockClimbingWall('Yes')    
"Why wouldn't you want a rock climbing wall?"
Class Attributes
While variables are inside of a class, they are referred to as attributes and not variables. When someone says 'attribute' you know they're speaking about a class. Attributes can be initialized through the init method, or outside of it.

Initializing Attributes
# see above

class Toy():
    kind = 'car' # This is called a constant
    
    def __init__(self, rooftop, horn, wheels): # not a function, but a nmethod
        self.rooftop = rooftop
        self.horn = horn
        self.wheels = wheels
        
tonka_truck = Toy(1, 1, 4) # 1 Rooftop, 1 horn, 4 wheels
hotwheels_car = Toy(2, 3, 8) #2 rooftops, 3 horns, 8 wheels  
Accessing Class Attributes
# See Above

tonka_truck.rooftop
hotwheels_car.wheels
8
Setting Defaults for Attributes
class Car():
    engine = '4.7L' # constant
    
    def __init__(self, wheels):
        self.wheels = wheels
        self.color = 'Blue'
        
honda = Car(4)
honda.color
# print(honda.engine)
'Blue'
Changing Class Attributes
Keep in mind there are global class attributes and then there are attributes only available to each class instance which won't effect other classes.

jeep = Car(8)

print(f'Before change: {jeep.color}')

jeep.color = 'White'

print(f'\nAfter Change: {jeep.color}')
print(honda.wheels)
Before change: Blue

After Change: White
4
 
In-Class Exercise #2 - Add a doors and seats attribute to your 'Car' class then print out two different instances with different doors and seats
class Car():
    
    def __init__(self, doors, seats = 4):
        self.doors = doors
        self.seats = seats
        
toyota = Car(2,2)
porsche = Car(4)

print(f"Toyota seats: {toyota.seats} and Toyota doors {toyota.doors}")
print(f"Porsche seats: {porsche.seats} and Porsche doors {porsche.doors}")
Toyota seats: 2 and Toyota doors 2
Porsche seats: 4 and Porsche doors 4
Class Methods
While inside of a class, functions are referred to as 'methods'. If you hear someone mention methods, they're speaking about classes. Methods are essentially functions, but only callable on the instances of a class.

Creating
class ShoppingBag():
    """
        The ShoppingBag class will have handles, capacity,
        and items to place inside.

        Attributes for the class:
        - handles: expected to be an integer
        - capacity: expected to be a string OR an integer
        - items: expected to be a list
    """
    
    def __init__(self, handles, capacity, items):
        self.handles = handles
        self.capacity = capacity
        self.items = items
        
    # Write a method that shows the items in our ShoppingBag / 
    # this is our items list.
    def showShoppingBag(self):
        print("You have items in your bag!")
        for item in self.items:
            print(item)

    # Show the capacity of ShoppingBag - how much room is left
    def showCapacity(self):
        print(f'Your capacity is: {self.capacity}')

    # Add item(s) to the items list for the ShoppingBag
    def addToShoppingBag(self):
        products = input('What would you like to add? ')
        self.items.append(products)

    # Change the capacity of the shopping bag
    def changeBagCapacity(self, capacity):
        self.capacity = capacity

    # Increase the capacity of the ShoppingBag by a default amount that we set to 10
    def increaseCapacity(self, changed_capacity = 10):
        if self.capacity == isinstance(self.capacity, str):
            print("We can't add that here")
        else:
            self.capacity += changed_capacity
Calling
# See Above
# So far, we created the idea of the shopping bag; now we will actually substantiate and make one and use it!
wholeFoods_bag = ShoppingBag(2,10,[])

# Create a function to run the ShoppingBag methods on our wholeFoods_bag Instance
def run():
    while True:
        response = input('What do you want to do? add/show/quit')
        
        if response.lower() == 'quit':
            wholeFoods_bag.showShoppingBag()
            print('Thanks for shopping')
            break
        elif response.lower() == 'add':
            wholeFoods_bag.addToShoppingBag()
        elif response.lower() == 'show':
            wholeFoods_bag.showShoppingBag()
        else:
            print('Try another command')
            
run()
What do you want to do? add/show/quitadd
What would you like to add? bagels
What do you want to do? add/show/quitshow
You have items in your bag!
bagels
What do you want to do? add/show/quitquit
You have items in your bag!
bagels
Thanks for shopping
Modifying an Attribute's Value Through a Method
# Show the capacity
wholeFoods_bag.showCapacity()
print('Capacity AFTER the change...')
wholeFoods_bag.changeBagCapacity(40)
wholeFoods_bag.showCapacity()
Your capacity is: 10
Capacity AFTER the change...
Your capacity is: 40
Incrementing an Attribute's Value Through a Method
wholeFoods_bag.showCapacity()
print('After increase:')
wholeFoods_bag.increaseCapacity()
wholeFoods_bag.showCapacity()
Your capacity is: 40
After increase:
Your capacity is: 50
In-Class Exercise #3 - Add a method that takes in three parameters of year, doors and seats and prints out a formatted print statement with make, model, year, seats, and doors
# Create class with 2 parameters inside of the __init__ which are make and model

# Inside of the Car class create a method that has 4 parameter in total (self,year,door,seats)

# Output: This car is from 2019 and is a Ford Expolorer and has 4 doors and 5 seats

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    def print_details(self, year, doors, seats):
        print(f"This car is from {year} and is a {self.make} {self.model} and has {doors} doors and {seats} seats.")

# Usage:
my_car = Car("Ford", "Explorer")
my_car.print_details(2019, 4, 5)
This car is from 2019 and is a Ford Explorer and has 4 doors and 5 seats.
Inheritance
You can create a child-parent relationship between two classes by using inheritance. What this allows you to do is have overriding methods, but also inherit traits from the parent class. Think of it as an actual parent and child, the child will inherit the parent's genes, as will the classes in OOP

Syntax for Inheriting from a Parent Class
# Create a parent class and call it Animal
class Animal():
    acceleration = 9.8 # Constant
    
    def __init__(self, name, species, legs = 4):
        self.name = name
        self.species = species
        self.legs = legs
        
    # Generic Parent Method - This is not overriding anything
    def makeSound(self):
        print('Make some generic sound')
    
    # End of parent class

# Creation of child class... Dog
class Dog(Animal):
    speed = 15
    
    def printInfo(self):
        print(f"The Dog has {self.speed}mph in speed and {self.acceleration}")
    
# Creation of Grand-Child Class -- Mutt
class Mutt(Dog):
    color = "Tan"
    
    # Override the ANIMAL class - using the Dog class to overwrite the __init__ from ANIMAL
    def __init__(self, name, species, eye_color, legs = 4):
        Dog.__init__(self,name,species,legs)
        self.eye_color = eye_color
        
    # Override the makeSound method (whiich is coming from... ANIMAL)
    def makeSound(self):
        noise  = 'Bark'
        return noise

lassie = Dog('Lassie', 'Dog')
basic_animal = Animal('Generical Animal Name', 'Generiic Animal Species')
buster = Mutt('Buster', 'Mut', 'Brown')

print(buster.makeSound())
print(lassie.makeSound())
print(buster.acceleration)
print(Dog.speed)
Bark
Make some generic sound
None
9.8
15
The __init__() Method for a Child Class - super()
class Puppy(Dog):
    color = 'black and brown'
    
    # Override the Animal class __init__ (via Dog class)
    def __init__(self, name, species, eye_color, legs = 4):
        super().__init__(name,species,legs)
        self.eye_color = eye_color
    
    # Override the makeSound method
    def makeSound(self):
        noise = 'Bark'
        return noise
Defining Attributes and Methods for the Child Class
# See Above
Method Overriding
# See Above
Classes as Attributes
Classes can also be used as attributes within another class. This is useful in situations where you need to keep variables locally stored, instead of globally stored.

class Battery():
    volts = 7.8
    
    def __init__(self, cells):
        self.cells = cells
        
class Car():
    def __init__(self, year, make, model, battery):
        self.year = year
        self.make = make
        self.model = model
        self.battery = battery
        
    def printInfo(self):
        return f'{self.year} {self.make} {self.model} {self.battery.cells}'
        
my_battery = Battery(20)

tesla = Car(2019, 'Tesla', 'Model X', my_battery)

print(tesla.battery.cells)
tesla.printInfo()
20
'2019 Tesla Model X 20'
Exercises
Exercise 1 - Turn the shopping cart program from yesterday into an object-oriented program
The comments in the cell below are there as a guide for thinking about the problem. However, if you feel a different way is best for you and your own thought process, please do what feels best for you by all means.

# Create a class called cart that retains items and has methods to add, remove, and show

class Cart():
    def __init__(self):
        self.cart = {}

    # Method to add items
    def addItem(self):
        item = input("Enter an item: ")
        quantity = int(input("Enter the quantity: "))
        if item in self.cart:
            self.cart[item] += quantity
            print(f"{quantity} added to {item}")
        else:
            self.cart[item] = quantity
            print(f"{item} added with quantity {quantity}")
        
    # Method to remove items
    def remItem(self):
        item = input("Enter the item you'd like to remove: ")
        if item in self.cart:
            del self.cart[item]
            print(f"{item} removed from cart.")
                  
    # Method to show cart
    def showCart(self):
        for item, quantity in self.cart.items():
            print(f"{item}: {quantity}")
        else:
            print(f"There are no items in your cart.")

my_cart = Cart()
my_cart.addItem()
my_cart.showCart()
my_cart.remItem()
There are no items in your cart.
Exercise 2 - Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case
class String():
    def __init__(self):
        self.string = {}
        
    def get_String(self):
        self.string = str(input("Give me a string: "))

    def print_String(self):
        print(f"Here is your string in capital letters: {self.string.upper()}")
            
my_string = String()
my_string.get_String()
my_string.print_String()
Give me a string: CT teachers are rad!
Here is your string in capital letters: CT TEACHERS ARE RAD!