import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = 'mail.corp.hxqc.com'
mail_user = 'mayw@corp.hxqc.com'
mail_passw = 'j123456789'

sender = 'mayw@corp.hxqc.com'
receiver = ['287541778@qq.com']
msg_mail = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">这是一个链接</a></p>
"""

message = MIMEText(msg_mail,'html')
'''message['From'] = Header('马援伟')
message['To'] = Header('余洁')'''
sub = 'python smtp 邮件测试'
message['Subject'] = Header(sub)

smtp = smtplib.SMTP()
smtp.connect(mail_host)
smtp.login(mail_user,mail_passw)
smtp.sendmail(sender,receiver,message.as_string())
print('发送成功')