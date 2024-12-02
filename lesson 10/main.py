# #Exercise 1
# import re

# def splitwords(text:str)->dict:
#     words = dict()
#     find = r"(\w+)"
#     result = re.findall(find,text)
#     for i in result:
#         if i not in words:
#             words[i] = 1
#         else:
#             words[i] += 1
#     return words

    


# text = "gagsg hdfhf  hjehgew jhekrwh hrhr, ashgdhs ehewh. jhrejj asdhdsh weghasdhj asfg asdf asdfg asdf asgaghhrfs asdf asfg"
# find = r"(\w+)"
# result = splitwords(text)

# print(result)



# #Exercise 2
# import os
# import re
# import json
# PATH = os.path.abspath(__file__ + "/.." + "/savedata.json")

# def savetojson(text):
#     try :
#         with open(PATH,"r") as file:
#             text_read = json.load(file)
#     except (FileNotFoundError, json.decoder.JSONDecodeError):
#         with open(PATH,"w") as file:
#             json.dump("", file, indent=4, ensure_ascii=False)
#             text_read = []

#     with open(PATH,"w") as file:
#         text_read.append(text)
            
#         json.dump(text_read,file, indent=4, ensure_ascii=False)

# def savedatafromtext(text):
#     templete1 = r"[0-9]{2}\.[0-9]{2}\.[0-2][0-9](([0-1)][0-9])|([2][0-5]))"
#     templete2 = r"\+380[0-9]{9}"
#     templete3 = r"\w+@\w+\.\w+"
#     date = re.search(templete1,text)
#     phone = re.search(templete2,text)
#     email = re.search(templete3,text)
#     savedata = {
#         "date" : date.group(),
#         "phone" : phone.group(),
#         "email" : email.group()
#         }
#     savetojson(savedata)
    

# text = "Today's date is 15.08.2013, and yesterday was 14.08.23. Contact us at +380123456789 for more details.Send inquiries to support@example.com "
# savedatafromtext(text)


#Exercise 3
# import re
# def backlastsymbol(text):
#     templete = r"\w{1,3}\b"
#     # templete = r"(\w\w\w(|$|,|\.))|( \w\w(|$|,|\.))|(\w(|$|,|\.))"
#     rezult = re.findall(templete,text)
#     print(rezult)

# text = input("enter your text : ")
# backlastsymbol(text)


# #Exercise 4

# import re

# def splitwords(text:str)->dict:
#     words = dict()
#     find = r"(\w+)"
#     result = re.findall(find,text)
#     for i in result:
#         if i not in words:
#             words[i] = 1
#         else:
#             words[i] += 1
#     return words

# def printinfo(text:str):
#     obj = splitwords(text)
#     count = 0
#     for i in obj:
#         if(obj[i] == 1):
#             print(i)

#         count += obj[i] 

#     print(len(obj))  
#     print(count)
    



# text = "gagsg hdfhf  hjehgew jhekrwh hrhr, ashgdhs ehewh. jhrejj asdhdsh weghasdhj asfg asdf asdfg asdf asgaghhrfs asdf asfg"
# find = r"(\w+)"


# printinfo(text)