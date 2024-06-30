import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime


now = datetime.datetime.now()

content= ''

def extractNews(url):
    print('Extracting Hackers News Stories')
    cnt = ''
    cnt+=('<b>HN Top Stories:</b>\n'+'<br>'+'-'*50+'<br>')
    respnse = requests.get(url)
    content=respnse.content
    soup = BeautifulSoup(content,'html.parser')
    for i, tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        cnt+= ((str(i+1)+tag.text + '\n' + '<br>') if tag.text!='More' else '')
        return(cnt)

cnt = extractNews('https://news.ycombinator.com/')
content+= cnt
content+= ('<br>-------<br>')
content+= ('<br><br>End of Message')


print('Composing Email...')


SERVER = 'smtp.gmail.com'
PORT = 587
FROM = input('Type Your Email --> ')
TO = input('Type Recipient --> ')
PASS = input('input Your Password --> ')

msg = MIMEMultipart()

msg['Sebject'] = 'Top New Stories HN [Automated Email]' + ' ' + str(now.day)+ '-'+ str(now.year)

msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))

print('Initiating Server.....')


server = smtplib.SMTP(SERVER, PORT)

server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent!')
server.quit()
