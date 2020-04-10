from email.mime.text import MIMEText
from email.header import Header
import smtplib


# QQ邮箱服务器登录的元素list
mail_host = 'smtp.qq.com'
mail_user = '973166414@qq.com'
mail_pass = 'rptkvjpzuonmbbib'

# 邮件收件人和发件人
sender = '973166414@qq.com'  # 3501875028@qq.com
recever = '973166414@qq.com'

# 邮件格式内容
content = """
    <p>python发送邮件的测试的内容,链接如下:</p>
    <p><a href="https://www.baidu.com">请点击此处</a></p>
    
    """
msg = MIMEText(content, 'html', 'utf-8')  # html ， plain(文本格式)
msg['from'] = Header('Alexle', 'utf-8')
msg['to'] = Header('乐春霞', 'utf-8')
subject = '这是一份python发送的测试邮件'
msg['subject'] = Header(subject, 'utf-8')




try:
    smtp = smtplib.SMTP()
    smtp.connect(mail_host, 25)
    smtp.login(mail_user, mail_pass)
    smtp.sendmail(sender, recever, msg.as_string())
    smtp.quit()
except smtplib.SMTPException:
    print("邮件无法发送")





# msg = MIMEText(content, 'plain', 'utf-8')
# # msg["from"] = '973266414@qq.com'
# # msg["to"] = '973166414@qq.com'
# # msg["subject"] = '这是一个邮件发送服务的测试'
# # msg['from'] = 'Alexle'
# # msg['to'] = 'Alexle'
