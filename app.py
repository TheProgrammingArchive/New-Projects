import re
import time
import os

def change():
    inq = 0
    dtl_Change = input('Enter the url to change details: ')
    while(dtl_Change == ""):
        dtl_Change = input('Url cannot be empty! Please try again: ')
    userchange = input('Enter new url to replace with old: ')
    while(userchange == ""):
        userchange = input('Url cannot be empty! Please try again >> ')
    passchange = input('Enter new password to change: ')
    while(userchange == ""):
        passchange = input('Password cannot be empty >> ')

    #indev



    with open('Ab10.txt', 'r') as file:
        data = file.readlines()
    matl = [line for line in data if dtl_Change in line]
    while True:
        try:
            inq = data.index(matl[0])
            data[inq] = '\n'
            with open('Ab10.txt', 'w'):
                file.writelines(data)
            break
        except:
            IndexError
            print('Password not registered')
            break
        break

def finalconf():
    finalconfirmation = input('Do you really want to delete the entire file content (Q to quit/E to continue): ')
    while True:
        if(finalconfirmation == 'Q'):
            break
        elif(finalconfirmation == 'E'):
            file = open('Ab10.txt', 'w')
            file.write('\n')
            break
        else:
            break

def delete_Line():
    inv = 0
    linetodelete = input('Enter website url to delete details: ')
    while(linetodelete == ""):
        linetodelete = input('Url cannot be empty! Please enter a url: ')
    with open('Ab10.txt', 'r') as file:
        data = file.readlines()
    matl = [line for line in data if linetodelete in line]
    while True:
        try:
            inv = data.index(matl[0])
            data[inv] = '\n'
            with open('Ab10.txt', 'w') as file:
                file.writelines(data)
            break
        except:
            IndexError
            print('Password is not registered')
            break
        break



def register():
    global login3
    global login2
    login1 = input('Enter the webiste url(Please enter the url correctly as you will be using the same url to look up the password again!) >> ')
    login3 = input('Enter the username for the website(Enter - if not applicable) >> ')
    login2 = input('Enter the password for the website >> ')
    password_Storage = open('Ab10.txt', 'a+')
    password_Storage.write(login1+"->"+login3+":"+login2+"\n")
    password_Storage.close()

def View():
    index = 0
    lgn1 = input('Enter the website url for password lookup: ')
    while(lgn1 == ""):
        lgn1 = input('Link cannot be empty! Please enter a valid link >> ')
    lgn1 = re.sub('#!@&', '', lgn1)
    with open('Ab10.txt') as data:
        data_value = data.readlines()
    file_name = open("Ab10.txt")
    while True:
        f_rd = open('Ab10.txt', 'r')
        file_lines = f_rd.readlines()
        f_rd.close()

        matches = [line for line in file_lines if lgn1 in line]

        while True:
            try:
                index = file_lines.index(matches[0])
                print(file_lines[index])
                break
            except:
                IndexError
                print('Password is not registered')
                break
        break
    data.close()


def app_Start():
    while True:
        print('\n\n\n\nRegr -> Register a password for a website\n')
        print('VIEW -> View details for a website\n')
        print('CHG -> Change details for a website\n')
        print('DEL -> Delete a registered website\n')
        print('DEL_FINAL -> DELETE ALL DETAILS (Please use this with caution)\n')
        print('QUIT -> Sign out and exit application\n')
        chg_Lg = input('Enter a function: ')
        if(chg_Lg.upper() == 'REGR'):
            register()
            app_Start()
        elif(chg_Lg.upper() == 'VIEW'):
            View()
            app_Start()
        elif(chg_Lg.upper() == 'CHG'):
            #indev
            change()
        elif(chg_Lg.upper() == 'DEL'):
            delete_Line()
        elif(chg_Lg.upper() == "DEL_FINAL"):
            finalconf()
        elif(chg_Lg.upper() == 'QUIT'):
            time.sleep(4)
            exit()




