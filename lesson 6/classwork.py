# class MyIterator:
#     def __init__(self, start_number : int):
#         self.__start_number = start_number

#     def __iter__(self):
#         self.__curent_number = self.__start_number
#         return self

#     def __next__(self):
#         if(self.__curent_number == -5):
#             raise StopIteration
#         rezult = self.__curent_number
#         self.__curent_number -= 1
#         return rezult
    
# for num in MyIterator(5):
#     print(num)
# for num in MyIterator(5):
#     print(num)

# class MyItter:
#     def __init__(self, num1:int, num2:int):
#         if(num1 < num2):
#             self.__start = num1
#             self.__end = num2
#         else:
#             raise ValueError("no")
        
#     def __iter__(self):
#         self.__current_number = self.__start
#         return(self)
    
#     def __next__(self):
#         if(self.__current_number > self.__end):
#             raise StopIteration
        
#         rezult = self.__current_number
#         self.__current_number += 1
#         return rezult
    
# for i in MyItter(10,10):
#     print(i)

class MyItter:
    def __init__(self, itter_obj:list):
        self.__itter_obj = itter_obj

    def __iter__(self):
        self.__current_id = 0
        return self

    def __next__(self):
        if(self.__current_id >= len (self.__itter_obj)):
            raise StopIteration
        
        rezult = self.__itter_obj[self.__current_id]
        self.__current_id += 1
        return (self.__current_id -1, rezult)
    
my_list = [3,5,1,7,5,3,75,123,64,13]
for i, value in MyItter(my_list):
    print(f"{i} --- {value}")
