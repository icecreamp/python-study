# Password manager
# Date: 2/18/2023
# Author: Hyunjin Kim
# Reference: https://youtu.be/DLn3jOsNRVE

# Encrypt textsz
from cryptography.fernet import Fernet

'''
# create key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

# load key
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key() 
fer = Fernet(key)

# function that shows the existing passwords
def view():
    with open('passwords.txt', 'r') as f:
        # read all the lines in the text file
        for line in f.readlines():
         data = line.rstrip()
         user, passw = data.split("|")
         print("User: ", user, "| Password: ",
              fer.decrypt(passw.encode()).decode())

# function that create the text file for passwords
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    # with: automatically close the file
    with open('passwords.txt', 'a') as f:
        # format the text
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

# view or add passwords or quit
while True: 
    mode = input(
        "Would you like to add a new password or view existing ones? (view, add), press q to quit: ").lower()

    if mode == "q":
        break 

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
         print("Invalid mode.")
         continue