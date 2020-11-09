import simplejson as json
import os

def register():
    file = open('./part.json', 'w+')
    username = input('NEW USERNAME: ')
    password = input('NEW PASSWORD: ')
    data = {'usr': username, 'pass': password}
    file.seek(0)
    file.writelines(json.dumps(data))
def login():
    username = input('Username: ')
    password = input('Password: ')
    file = open('./part.json', 'r+')
    data = json.loads(file.read())
    if(data['usr'] == username and data['pass'] == password):
        print('Login successful!')
    else:
        print('Login unsuccessful')



lgn = input('REGISTER/LOGIN/EXIT : ')
while True:
    if(lgn.upper() == "REGISTER"):
        if(os.path.isfile('./part.json') and os.stat('./part.json').st_size != 0):
            print('ACCOUNT EXISTS!')
            login()
            break
        else:
                register()
    elif(lgn.upper() == "LOGIN"):
        login()
        break
    elif(lgn.upper() == 'EXIT'):
        exit()
    else:
        lgn = input('no: ')

