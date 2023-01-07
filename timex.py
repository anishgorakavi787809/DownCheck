import smtplib
import os
from email.message import EmailMessage
import requests as req
import sys

gmail = smtplib.SMTP("smtp-mail.outlook.com",587)
gmail.starttls()
em = EmailMessage()
gmail.login("xxx@xmail.xxd","###########")
def sendme(sub,text:str):
    em["from"] = "xxx@xmail.xxd"
    em["to"] = "anish.gorakavi@gmail.com"
    em["subject"] = sub
    em.set_content(text)
    gmail.sendmail("xxx@xmail.xxd","anish.gorakavi@gmail.com",em.as_string())

argli = sys.argv
argli.pop(0)
print(argli)

def check_sites(los:list):
    down_sites = []
    for i in los:
        try:
            r = req.get(i)
            if r.status_code > 399:
                down_sites.append(i)
        except:
            down_sites.append(i)
    return down_sites
# Server check

#LOGGING!
los = argli
res = ""
for i in check_sites(los):
    res += i + "\n"
if len(check_sites(los)) != 0:
    comp = f"""Error, The sites are down.\n
    Here are the down sites\n\n
    {str(res)}
    """
    sendme("Alert: Site is down",comp)