from base64 import decode
import imaplib
import email
from bs4 import BeautifulSoup

mailslist = open("mails.txt", "r").readlines()  #accounts list
for mail in mailslist:                          #multiple accounts           
    imap_server = "imap.mail.ru"
    seq = mail.strip()
    acc= seq.split(":")

    email_adrress = acc[0]
    password = acc[1]

    imap = imaplib.IMAP4_SSL(imap_server)
    imap.login(email_adrress, password)

    imap.select("inbox")

    _, msgnums = imap.search(None, "UNSEEN")

    for msgnum in msgnums[0].split():
        _, data = imap.fetch(msgnum, "(RFC822)")

        _, b = data[0]
        message = email.message_from_bytes(b)

        print(f"Message Number: {msgnum}")
        print(f"From: {message.get('From')}")
        print(f"To: {message.get('To')}")
        print(f"BCC: {message.get('BCC')}")
        print(f"Date: {message.get('Date')}")
        print(f"Subject: {message.get('subject')}")

        print("Content:")
        for part in message.walk():
            if part.get_content_type() == "text/html" or part.get_content_type() == "text/plain":
                body = part.get_payload()
                
                soup = BeautifulSoup(body, "lxml")
                #page_code = soup.find('div', class_="button-container").find("style").text
                page_code = soup.find_all("h2")
                
                for item in page_code:
                    print(item.text)
                    #newsletters
imap.close() 
