import re

class Account:
    def __init__(self,username,password,phone_number,email) -> None:
        self.username = Account._username_checker(username)
        self.password = Account._password_checker(password)
        self.phone_number = Account._phone_checker(phone_number)
        self.email =Account._email_checker(email)

def get_username(name,lastname):
    name = input("please write your name")
    lastname =input("please write your lastname")
    return ("name"+"_"+"lastname")

def get_password():
    temppassword = self._password_checker(password)
    password= input("please write a strong password")
    return password.encode(encoding = 'UTF-8', errors = 'strict')

@staticmethod
def _password_checker(password):
    pattern =[A-Za-z0-9]{1,8}
    if re.match(pattern, password):
        return password
    else:
        print('invalid password')

@staticmethod
def _username_checker(username):
    pattern =[A-Za-z]
    if re.match(pattern, username):
        return username
    else:
        print('invalid username')

@staticmethod
def _phone_checker(phone_number):
    pattern =[0-9]{1,11}
    if re.match(pattern,phone_number):
       return phone_number
    else:
        print('invalid phone number')

@staticmethod
def _email_checker(First_Part,Second_Part,Third_Part):
    pattern_1 = [a-z A-Z 0-9 _ - . ]
    pattern_2 = [a-zA-Z]{2,5}
    if re.match(pattern_1,First_Part,Second_Part):
       return First_Part,Second_Part
    elif re.match(pattern_2,First_Part,Third_Part):
        return Third_Part
    else:
        print('invalid email')

class Site:
    def __init__(self,url,register_users,active_users) -> None:
        self.url=url
        self.register_users= []
        self.active_users = []
    
    def register (object=Account()):
        if object not in register_users:
            register_users.append(object)
            print ("register successful")
        else:
            raise Exception("user already registered")
    
    def login():
        pass

    def logout():
        pass
    

        



