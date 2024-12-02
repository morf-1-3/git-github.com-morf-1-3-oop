class Email:
    def __init__(self, email:str, password:str):
        self.__email = email
        self.__password = password

    def set_email(self, new_email:str):
        if("@" in new_email): 
            self.__email = new_email

    def get_email(self):
        return self.__email

    def set_password(self, new_password:str):
        flag = False
        if(len(new_password) > 7):
            for symbol in new_password:
                if symbol.istitle():
                    flag = True
        if flag:
            self.__password = new_password

    def get_password(self):
        return "*"*len(self.__password)
    


emeil1 = Email("foly@gmail.com", "gagAS")
emeil1.set_email("falooaglgmail.com")
emeil1.set_password("gasgAasg15S2")
print(emeil1.get_email())
print(emeil1.get_password())