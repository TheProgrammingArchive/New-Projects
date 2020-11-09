import os
import random
import time
import re
from app import app_Start

def login():
    while True:
        print('\n\n\n\n\n\nLOGIN PAGE\n\n')
        usr = input('Enter your username: ')
        pasr = input('Enter your password: ')
        storage_Login = open('Tm1.txt', 'r')
        data_Login = storage_Login.readline()
        storage_Login.close()
        if(data_Login == pasr+":"+usr):
            print("LOGIN SUCCESSFUL!\n\n")
            app_Start()
            break
        print('Username/Password incorrect! Please try again.')

print("\t\t\t\t\t\t\tPASSWORD VAULT PYTHON\t\t\t\t\t\t\t\n\n\n\n\n\n\n")

reg_Conf = input("REGISTER/LOGIN: ")
while(reg_Conf == ""):
    reg_Conf = input("Argument cannot be empty! >> ")

if(reg_Conf.upper() == 'REGISTER'):
    while True:
        if (os.path.exists('Tm1.txt') == True):
            print("This device already has a registered account! Please login to continue\n")
            login()
            break
        username = input('Enter a username: ')
        while(username == ""):
            username = input('Username cannot be empty! >> ')
        password = input('Enter a password: ')
        while(password == ""):
            password = input("Password cannot be empty!")
        passconf = input("Please confirm your password: ")
        if(password == passconf):
            storage = open('Tm1.txt', 'w')
            storage.write(username+":"+password)
            storage.close()
            print("Login for device successful! Please login to your account now \n\n")
            login()
            break
        print('Passwords do not match! Please try again\n')

elif(reg_Conf.upper() == 'LOGIN'):
    login()

else:
    login()