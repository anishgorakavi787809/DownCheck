import smtplib
import os
from email.message import EmailMessage
import requests as req
import sys

gmail = smtplib.SMTP("smtp-mail.outlook.com",587)
gmail.starttls()
em = EmailMessage()
gmail.login(os.environ["GMAIL_EMAIL"],os.environ["GMAIL_PASSWORD"])
def sendme(sub,text:str):
    em["from"] = "gorakavI@outlook.com"
    em["to"] = "anish.gorakavi@gmail.com"
    em["subject"] = sub
    em.set_content(text)
    gmail.sendmail("gorakavi@outlook.com","anish.gorakavi@gmail.com",em.as_string())

def check_sites(los:list):
    down_sites = []
    for i in los:
        try:
            req.get(i)
        except:
            down_sites.append(i)
    return down_sites
# Server check

#LOGGING!
los = ["http://localhost:5000"]
res = ""
for i in check_sites(los):
    res += i + "\n"
if len(check_sites(los)) != 0:
    comp = f"""Error, The sites are down.\n
    Here are the down sites\n\n
    {str(res)}
    """
    sendme("Alert: Site is down",comp)