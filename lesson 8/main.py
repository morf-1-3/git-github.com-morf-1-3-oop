# import random
# import os
# # print(__file__ + "  ss")
# PATH = os.path.abspath(__file__ + "/..") + "/file.txt"
# print(PATH)
# with open (PATH, "w") as file:
#     file.write("")
# for _ in range(1000):
    
#     with open (PATH,"a") as file:
#         file.write(str(random.randint(1,1000)) + ' ')
# sum = 0
    
# with open (PATH,"r") as file:
#     numbers = file.read()
# numbers = numbers.split(" ")
# numbers.pop(-1)
# print(numbers)
# for n in numbers:
#     sum += int(n)

# print(sum)




# #Exercise 3
# import json
# import pickle
# import os
# products = {
#     "Електроніка": ["Телефон", "Ноутбук", "Навушники"],
#     "Одяг": ["Футболка", "Джинси", "Куртка"],
#     "Книги": ["Роман", "Фентезі", "Наукова література"]
# }

# PATH_JSON = os.path.abspath(__file__ + "/..") + "/fileJson.json"
# PATH_PICKLE = os.path.abspath(__file__ + "/..") + "/filePikle.pkl"

# with open(PATH_JSON, "w", encoding="utf-8") as file_json:
#     json.dump(products, file_json, indent= 2, ensure_ascii=False)

# with open(PATH_JSON, "r", encoding="utf-8") as file_json:
#     read = json.load(file_json)
# print(read)

# with open(PATH_PICKLE, "wb") as file_pickle:
#     pickle.dump(products,file_pickle)

# with open(PATH_PICKLE, "rb") as file_pickle:
#     read = pickle.load(file_pickle)  
# print(read)  




#  #Exercise 2
# import json
# import os
# PATH = os.path.abspath(__file__ + "/..")
# PATH_JSON = PATH + "/filebd.json"

# def save_data(obj):
#     with open(PATH_JSON, "w") as file:
#         json.dump(obj, file,indent=0)

# def load_data():
#     with open(PATH_JSON, "r") as file:
#         result = json.load(file)
#     return result




# try:
#     links = load_data()
# except FileNotFoundError:
#     links = dict()

# while(True):

#     link = input("Enter full link : ")
#     if (link == "end"):
#         break

#     short_link = input("Enter short link : ")
#     if (short_link == "end"):
#         break

#     links[short_link] = link
# save_data(links)

# find_link = input ("Enter shord link to find : ")
# if(find_link in list(links.keys())):
#     print(links[find_link])
# else:
#     print("error link")
