import smtplib
import csv
import time
from email.message import EmailMessage
from email.headerregistry import Address
from email.utils import make_msgid
from email.mime.text import MIMEText

s = smtplib.SMTP('smtp.gmail.com', 587)
count = 0
s.starttls()

email = "aldehf420@gmail.com"

s.login(email, 'hcmwwpjjpsudqkgo')


with open('test.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

for x in data:
    count += 1
    msg = EmailMessage()

    msg['Subject'] = 'test mail'
    msg['to'] = x[0]
    msg['from'] = email
    asparagus_cid = make_msgid()
    msg.add_alternative("""\
    <html>
    <head></head>
    <body>
        <img src="https://raw.githubusercontent.com/gohdong/image_test/master/2021_promotion.jpg" alt="aasd" width="564 px" height="2718 px" usemap="#imgmap202132175313" >
        <map id="imgmap202132175313" name="imgmap202132175313">
            <area shape="rect" alt="" title="" coords="159,439,276,464" href="https://www.hanyang3d.kr/page/consultation/?utm_source=url_source_mail&utm_medium=url_medium_mail&utm_campaign=url_campaign_mail&utm_content=url_content_mail" target="" />
            <area shape="rect" alt="" title="" coords="285,440,404,463" href="https://www.hanyang3d.kr/?utm_source=url_source_mail&utm_medium=url_medium_mail&utm_campaign=url_campaign_mail&utm_content=url_content_mail" target="" />
            <area shape="rect" alt="" title="" coords="27,2290,216,2320" href="http://hanyang3d.kr/board/list?bd_id=project_portfolio&cate=&per_page=1/?utm_source=url_source_mail&utm_medium=url_medium_mail&utm_campaign=url_campaign_mail&utm_content=url_content_mail" target="" />
        </map>
        <img src="https://www.google-analytics.com/collect?v=1&tid=UA-145822029-2&cid=*|UNIQID|*&t=event&ec=code_ec_mail&ea=code_ea_mail&cs=code_cs_mail&cm=code_cm_mail&cn=code_cn_mail&cm1=2"/>
    </body>
    </html>
    """.format(asparagus_cid=asparagus_cid[1:-1]), subtype='html')
    print("=================================================================")
    print("sending to ==> " + msg['to'])
    s.sendmail(msg['from'],msg['to'], msg.as_string())
    print(str((count*100/len(data)))+"% "+"completed "+str(count)+"/"+str(len(data)))
    print("sleep 10 seconds")
    time.sleep(10)




s.quit()

