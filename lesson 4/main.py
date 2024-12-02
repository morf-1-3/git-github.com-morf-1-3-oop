#Exercise 2
# class colculator :
#     @staticmethod
#     def plus(num1:int, num2:int)->int:
#         return num1+num2
    
#     @staticmethod
#     def diffrence(num1:int, num2:int)->int:
#         return num1-num2
    
#     @staticmethod
#     def multi(num1:int, num2:int)->int:
#         return num1*num2
    
#     @staticmethod
#     def division(num1:int, num2:int)->float:
#         return num1/num2
    
#     @staticmethod
#     def pow(num1:int, num2:float)->float:
#         return num1**num2


# user_input = {
#     "+" : colculator.plus,
#     "-" : colculator.diffrence,
#     "*" : colculator.multi,
#     "/" : colculator.division,
#     "**" : colculator.pow
# }
# while(True):
#     colculator.plus



#     try:
#         num1 = int(input("enter num"))
#         num2 = int(input("enter num"))
#         operation = input("enter operation")
#         print(user_input[operation](num1,num2))
#     except ValueError as e:
#         print(e)
#     except ZeroDivisionError as e:
#         print(e)
#     except KeyError as e:
#         print(f"chose only + - * / ** \n your choose {e} not correct")





#exircise 3
# class Employee:
#     def __init__(self, name:str, lastname:str, departmen:str, year_srart_work:int):
#         if(len(name) < 3 or len(lastname) < 3):
#             raise(ValueError("Too short name or lastname"))
#         assert departmen in departmens, "not do exists depatment"
#         if(year_srart_work <= 2013):
#             raise(ValueError("year not possible, company creates in 2013"))
#         self.__name = name
#         self.__lastname = lastname
#         self.__deparmen = departmen 
#         self.__year_start_working = year_srart_work

#     def get_year_startToWork(self):
#         return self.__year_start_working

# departmens = [
#     "first", "second", "thirtd"
# ]

# empoyees = []

# while(True):
#     name = input("Enter Name: ")
#     if(name == "end"):
#         break

#     lastname = input("Enter LastName: ")
#     departmen = input("Enter departmen: ")
#     year = int(input("Enter year when emploee sratr to work"))
#     try:
#         empoyees.append(Employee(name,lastname,departmen,year))
#     except Exception as e:
#         print(e)

# year = int(input("Enter your for info"))
# count = 0
# for emploee in empoyees:
#     if emploee.get_year_startToWork() >= year:
#         count += 1
# print(count)



#Exercise 4

# class MyExecption(Exception):
#     pass

# def show_number(number:int)->None:
#     if(number <= 0 ):
#         raise MyExecption("mm")

# show_number(-1)
# print("s")
    

#Exercise 5 

# user_inputs =[
#     "1 - Перелік видів спорту",
#     "2 - Команда тренерів",
#     "3 - Розклад тренувать",
#     "4 - Вартість тренувань",
#     "5 - Пошук по тренеру",
#     "0 - Exit"
# ]

# sports = {
#     "footbal" : [["Berkon","Miil","Orel"],["7.00 - first","8.00 - second", "13.00 - third"],"400 per hour"],
#     "backetbal" : [["Omnick","Morf","Huskar"],["7.00 - first","8.00 - second", "13.00 - third"],"480 per hour"],
#     "golf" : [["Mippo","Srotm","Ivanov"],["7.00 - first","8.00 - second", "13.00 - third"],"500 per hour"]
# }

# class NotFoundSport(Exception):
#     pass


# def showTrainers(sport:str, sports)->str:
#     if not(sport in sports.keys()):
#         raise NotFoundSport(" ")
#     return sports[sport][0]

# def findByLastName(lastname:str, sports)->str:
#     for sport in sports:
        
#         if(lastname in sports[sport][0]):
#             return f"{lastname} traint {sport} schedule {sports[sport][1]} price {sports[sport][-1]}"
        
#     return "not found"

# def showSports(sports)->str:
#     return " ".join(sports.keys()) 


# def showShedule(sport:str, sports)->str:
#     if not(sport in sports.keys()):
#         raise NotFoundSport(" ")
#     return sports[sport][1]

# def showPrice(sport:str, sports)->str:
#     if not(sport in sports.keys()):
#         raise NotFoundSport(" ")
#     return sports[sport][-1]     



# while(True):
#     print("\n".join(user_inputs))
#     user_input = int(input())

#     match user_input:
#         case 1:
#             print(showSports(sports))

#         case 2:
#             sport = input("Enter sport: ")
#             try:
#                 print(showTrainers(sport, sports))
#             except NotFoundSport:
#                 print(NotFoundSport(f"not found {sport}"))

#         case 3:
#             sport = input("Enter sport: ")
            
#             try:
#                 print(showShedule(sport, sports))
#             except NotFoundSport:
#                 print(NotFoundSport(f"not found {sport}"))

#         case 4:
#             sport = input("Enter sport: ")
            
#             try:
#                 print(showPrice(sport, sports))
#             except NotFoundSport:
#                 print(NotFoundSport(f"not found {sport}"))

#         case 5:
#             lastname = input("Enter last name of trainer: ")
#             print(findByLastName(lastname, sports))

#         case 0:
#             break

#         case _:
#             print("not correct")

    
    

    
    
    
