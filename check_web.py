import os
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

MYMAIL=''
Receivers=['']
def send(s):
    sender=MYMAIL
    receivers=Receivers

    message = MIMEText(s[:1000],'plain','utf-8')
    message['From'] = Header('me','utf-8')
    message['To'] = Header('you','utf-8')

    subject = '[Notice]The intro2cs web has changed.'
    message['Subject'] = Header(subject,'utf-8')

    mail = smtplib.SMTP()
    mail.connect('smtpserver',25)
    mail.login('mailaddress','password')
    mail.sendmail(sender,receivers,message.as_string())



while True:
    os.system('wget http://iiis.tsinghua.edu.cn/~xfcui/intro2cs/ -O /root/check_web/new.html')
    os.system('diff /root/check_web/old.html /root/check_web/new.html > /root/check_web/result.txt')
    os.system('mv /root/check_web/new.html /root/check_web/old.html')
    result=''
    with open('/root/check_web/result.txt','r') as f:
        result=f.read()

    result=result.strip()
    if len(result) > 5:
        send(result)
    time.sleep(60*60)
    