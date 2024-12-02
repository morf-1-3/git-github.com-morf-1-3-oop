# #exercise 1

# def my_generator(my_list):
#     for i in range(len(my_list)):
#         yield my_list[-1-i]

# my_list = [3,5,7,1,3,7,2,7,9,3,1]
# for i in my_generator(my_list):
#     print(i)



#Exercise 2

def my_generator(my_list:list):
    for i in my_list:
        if(i % 2) == 0:
            yield (i **2)

my_list = [3,5,7,16,3,7,2,7,9,3,1,4,2,8]

for i in my_generator(my_list):
    print(i)