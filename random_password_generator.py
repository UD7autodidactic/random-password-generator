import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%&*")

def generate_password():
    password_length = int(input("how long whould you like your password to be ?"))
    
    random.shuffle(characters)
    
    password = []
    
    for i in range (password_length):
        password.append(random.choice(characters))
        
    random.shuffle(password)
    
    password = ''.join(password)
    
    print(password)
    
option = input("whoud you like to generate password? (yes/no)")     
if option == "yes":
    generate_password()
elif option == "no":
    print("goodbye")
    quit()
else:
    print("invalid input please enter yes/no")
    quit()
        
    