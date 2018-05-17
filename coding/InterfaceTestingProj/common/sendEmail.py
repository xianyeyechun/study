#coding = utf-8

import smtplib

from email.mime.text import MIMEText
from email.header import Header

def sendEmail():
    toList='673749948@qq.com'
    fromEmail='yhx0816@126.com'
    hostDir='smtp.126.com'
    userName='yhx0816@126.com'
    passwd='y15882452147'

    message=MIMEText(u'接口自动化脚本已经测试完成','plain','utf-8')
    message['from']=fromEmail
    message['to']=toList
    subject='Python SMTP 邮件测试'
    message['Subject']=subject

    #创建SMTP对象
    e=smtplib.SMTP()
    #创建与服务主机的连接
    e.connect(hostDir,port=25)
    e.login(userName,passwd)
    #发送相关邮件内容
    e.sendmail(fromEmail,toList,message.as_string())
    #发送完毕断开连接
    e.quit()
    print(u'邮件发送完成')
if __name__=='__main__':
   try:
       sendEmail()

   except Exception as e:
       print(e)

