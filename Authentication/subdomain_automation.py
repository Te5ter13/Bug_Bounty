import requests

url1="https://hackthebox.eu"
fd = open("subdomains.txt","r")
content=fd.read()
fd.close()
wordlist=list(content.split('\n'))
#print(wordlist)

for i in wordlist:
    url2 = "https://{}.hackthebox.eu".format(i)

    #Virtual host enumeration
    """headers={
        "HOST":"{}.hackthebox.eu".format(i)
    }"""
    try:
        # for virtual host
        # r = requests.get(url1,headers=headers)

        #for subdomain
        r = requests.get(url2)
        if r.status_code != 404 and len(r.text)>0:
            print(i)
    except:
        pass    
