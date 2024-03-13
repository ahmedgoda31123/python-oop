# when calling a method python passes the object 
# itself so you need to define the parameter self to hold it in it

# you can define parameters to your object even if they are not defined in there obj.random_var = 5

# ...(self, name: str) it makes sure that it will be a string

# assert price >= 0 to make sure that the price variable will be positive
# the assert statement throughs an error if the condition isn't true

# print(class.attribute) will work
# print(class.__dict__) will print all the attributes in the class

# def __repr__ ... a method used to make representing the objects more user friendly

# @classmethod before the line of def of a method will make this method a class method
# so it will be accessible from the class level class.method and the object level
# when you call a class method the class itself will be passed as a first argument
# so we have to intercept it not in self but in cls variable

# also static methods must have @staticmethod before it
# and the main difference is that a static method don't need to have self
# and it receives it's parameters as any regular function

# isinstance(var, className) checks whether a given parameter is from a specific class or not

# you should use a static method when you want to define a method without passing the self var
# while you should use the class method mostly when initializing objects from files
# both could be called from the class level and the object level

# here if you wanted to created methods for phone kind of items 
# you should make another class with those methods added here comes inheritance
# class son(father):

# you don't have to duplicate while initializing __init__ for the son class
# you can use super.__init__(...) with passing the original args for the father class
# the super() function gives us access to all of the attributes and functions from the father class

# self.__class__.__name__ => refers to current class name

# @... are called decorators

# self.__name makes name a private property you need setters and getters to access

# oop principles => 1- encapsulation, 2- abstraction, 3- inheritance, 4- polymorphism
# encapsulation is about taking control of the process of accessing your data

# abstraction show only necessary and make them accessible
# __private_method()

# polymorphism (many forms)=> def func(self, value1) def func(self, value1, value2) ...
# it accepts many forms so polymorphism is achieved