import urllib2,time,json
import smtplib
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header

mailto_list=['970787907@qq.com']
mail_host="smtp.126.com"
mail_user="yuyuyugood@126.com"
mail_pass="yuning123"
mail_postfix="126.com"
headers = {'Content-Type': 'application/json'}
sender = 'yuyuyugood@126.com'
receivers = ['970787907@qq.com']
def send_mail(to_list,sub,content):
    me="Alert"+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content,_subtype='plain')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    server = smtplib.SMTP()
    server.connect(mail_host)
    server.login(mail_user,mail_pass)
    server.sendmail(me, to_list, msg.as_string())
    server.close()

def ask1():
    response = urllib2.urlopen('https://item.jd.com/8753810.html')
    responsecode = response.getcode()
    content = response.read().decode("gb18030")
    soup = BeautifulSoup(content, "lxml")
    items = soup.select("#choose-btn-ko")
    if items[0]:
        if items[0]["href"]!="#none":
            send_mail(mailto_list,"Meizu!","16plus go!")
    else:
        send_mail(mailto_list,"Error!","This program run error!")
    time.sleep(1)
var=1
while var == 1:
    ask1()