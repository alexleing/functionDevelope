from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import smtplib


mail_host = 'smtp.qq.com'      #   网易邮箱 PJVFOXNUTFAEBLBN
# mail_host = 'smtp.163.com '
mail_user = '973166414@qq.com' # mailhz.qiye.163.com   alexle@x2era.com lechunxiaing@163.com
# mail_user = 'lechunxiaing@163.com'
mail_pass = 'rptkvjpzuonmbbib' # 网易企业邮箱的授权码 hhuE28EkeRXBms6S
# mail_pass = 'PJVFOXNUTFAEBLBN'
sender = "973166414@qq.com"
# sender = "lechunxiaing@163.com"
to_reciver = ['973166414@qq.com',"3501875028@qq.com",]
# cc_reciver = "973166414@qq.com"
reciver_name = ['乐春霞', "小号"]

content = """
<p>Dear {user}:</p>
    <p style="text-indent:2em"> 这是测试邮件里面的内容,详情请点击链接或者下载附件。</p>
    <div> <a href = "https://www.baidu.com"><span font-size="20px">请点击这里</span></a></div>
    <p> 图片的演示：</p>
    <p> <img src="cid:image1" alt="本地文件的图片" width="300px"/></p>

"""

for i in range(len(to_reciver)):

    msg = MIMEMultipart("related")
    msg['from'] = Header("973166414@qq.com", 'utf-8')
    msg['to'] = Header(reciver_name[i],'utf-8')
    # msg['cc'] = Header('973166414@qq.com', 'utf-8')
    subject = '这是一个带附件的python测试邮件'
    msg['subject'] = Header(subject, 'utf-8')

    msg2 = MIMEMultipart("alternative")
    msg.attach(msg2)




    msg.attach(MIMEText(content.format(user=reciver_name[to_reciver.index(to_reciver[i])]), 'html', 'utf-8'))
    msgImage = MIMEImage(open('testimage.jpg', 'rb').read())
    msgImage.add_header("Content-ID", "<image1>")
    msg.attach(msgImage)

    att1 = MIMEText(open('user_info.txt', 'rb').read(), 'base64','utf-8')
    att1['content-type'] = 'application/octet-stream'
    att1['content-disposition'] = 'attachment; filename="user_info.txt"'
    msg2.attach(att1)

    att2 = MIMEText(open('SMTPdevelop.py', 'rb').read(), 'base64', 'utf-8')
    att2['content-type'] = 'application/octet-stream'
    att2['content-disposition'] = 'attachment; filename="SMTPdevelop.py"'
    msg2.attach(att2)



    try:
        smtp = smtplib.SMTP()
        smtp.connect(mail_host, 25)
        smtp.login(mail_user,mail_pass)
        # for i in range(5):
        smtp.sendmail(sender, to_reciver[i], msg.as_string())

        smtp.quit()
        print('邮件发送成功')
    except smtplib.SMTPException as e:
    # except Exception as e:
        print('邮件发送失败！')
        print(e)


