user_choices = ["1 - Add your worker", "2 - delete all workers", "3 - show all workers \n"]


while True:
    user_choice = int(input("\n".join(user_choices)))
    if user_choice == 1:

        with open('file_with_worker.txt',"a") as file:
            name_worker = input("enter name of person you want to add:  ")
            file.write(name_worker+"\n")


    if user_choice == 2:
        with open('file_with_worker.txt',"w") as file:
            file.write("")

    if user_choice == 3:
        try:
            with open('file_with_worker.txt',"r") as file:
                name_workers = file.read()
                list_workers = name_workers.split("\n")
                for i in list_workers:
                    print(i)
        except FileNotFoundError as Error:
            print(Error)

