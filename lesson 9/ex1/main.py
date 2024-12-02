
import saveinfile as save
import reedfromfile as read






links = read.load_data()

print(links)

while(True):

    link = input("Enter full link : ")
    if (link == "end"):
        break

    short_link = input("Enter short link : ")
    if (short_link == "end"):
        break

    links[short_link] = link
save.save_data(links)

find_link = input ("Enter shord link to find : ")
if(find_link in list(links.keys())):
    print(links[find_link])
else:
    print("error link")