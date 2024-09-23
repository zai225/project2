
#Instance vs Class Variable
# class Employee:
#   Company = "Britania"
#   def __init__(self, name):
#     self.name = name
#     self.id_no = 447
#   def show_details(self):
#     print(f"The name of the employee is {self.name} id no. is {self.id_no} and he work's for {self.Company}")

# e = Employee("Shantanu") 
# e.show_details()
# e2 = Employee("Payal")
# e2.id_no = 304
# e2.Company = "Nestle"
# e2.show_details()
#In this the instance variable is used to change tha class variable..


#QUE
# class Car:
#     def __init__(self, make, year, model):
#         self.make = make
#         self.year = year
#         self.model = model

#     def display_info(self):
#         print(f"Car: {self.make}, {self.year}, {self.model}")

# c = Car("BMW", 1997, "Xi1")
# c.display_info()

#Que
# class Dog:
#     species = "Beagle"
#     def __init__(self,name):
#         self.name = name

#     def display(self):
#         print(f"{self.name} belongs the species {self.species}")

# d = Dog("Pluto")
# d.species = "Golden retriver"
# d.display()

#Que
class Book:
    total_book = 0
    def __init__(self, title, author,):
        self.title = title
        self.author = author
        Book.total_book += 1
    
    def book_details(self):
        print(f"The name of the book is {self.title} and the Author is {self.author} count : {Book.total_book} ")
      
b = Book("The Guy who lived", 'Harper lee')
b.book_details()      
b2 = Book("The Guy Who die", 'Chinal')
b2.book_details()
b3 = Book("The Guy Who" , "Raal")
b2.book_details()













