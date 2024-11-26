#exercise 1,2
# class rewiew:
#     def __init__(self, text :str):
#         self.review = text
#     def __str__(self):
#         return (self.review)
#     def show_me(self):
#         return self.review

# class book:
#     def __init__(self, name : str, autor : str, 
#                  year : int, teme : str):
#         self.name = name
#         self.aurot = autor
#         self.year = year
#         self.teme = teme
#         self.reviews = []
#         self.reviews.append(rewiew("nice book"))
#     def __str__(self):
#         return (f"book name is {self.name}, autor is {self.aurot}, year - {self.year}, theme - {self.teme},  rewiews  - {self.show_rewiew()}")
#     def __rept__(self):
#         return (f"book  sss name is {self.name}, autor is {self.aurot}, year - {self.year}, theme - {self.teme}, rewiews  - ")
#     def add_rewiew(self, rew : rewiew):
#         self.reviews.append(rew)
#     def show_rewiew(self):
#         str = ""
#         for rewiew in self.reviews:
#             str += rewiew.review
#             str += "  "
#         return str



# book1 = book("harry poter", "GGG", "2001", "Mific")
# print(book1)
# new_rewiew = rewiew("Bla bal bal")
# book1.add_rewiew(new_rewiew)
# print(book1)


# class car:
#     def __init__(self, name : str, year : int):
#         self.name = name
#         self.year = year

    

# class Showroom:
#     def __init__(self):
#         self.cars = []
#     def add_car(self,car : car):
#         self.cars.append(car)
#     def show_cars(self):
#         for car in self.cars:
#             print(car.name)
#     def sell_car(self, number : int):
#         str = input(f"do you wanna sell {self.cars[number].name}  :?")
#         if str == "yes":
#             self.cars.pop(number-1)
        


        
    

# my_showroom = Showroom()
# my_showroom.add_car(car("BMW",2024))
# my_showroom.add_car(car("Lexus",2024))
# my_showroom.add_car(car("Toyota",2024))
# my_showroom.show_cars()
# my_showroom.sell_car(1)
# my_showroom.show_cars()
