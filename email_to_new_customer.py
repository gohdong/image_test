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

email = "print3d@hanyang.ac.kr"

s.login(email, 'arkgszgsychrkizj')


with open('new_try_1st.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

for x in data:
    count += 1
    msg = EmailMessage()

    msg['Subject'] = '[한양3D팩토리] 3D프린팅 목업 제작 지원'
    msg['to'] = x[0]
    msg['from'] = email
    asparagus_cid = make_msgid()
    msg.add_alternative("""\
    <html>
    <head></head>
    <body>
        <div>
            <p
                style="font-variant-numeric:normal;font-variant-east-asian:normal;font-stretch:normal;font-size:13px;line-height:normal;font-family:&quot;Helvetica Neue&quot;;margin:0px">
                안녕하세요. 디자인/개발팀 담당자님!</p>
            <p
                style="font-variant-numeric:normal;font-variant-east-asian:normal;font-stretch:normal;font-size:13px;line-height:normal;font-family:&quot;Helvetica Neue&quot;;margin:0px">
                3D프린팅 제조 전문 서비스,&nbsp;<b>“한양3D팩토리”</b>입니다.</p>
            <p
                style="font-variant-numeric:normal;font-variant-east-asian:normal;font-stretch:normal;font-size:13px;line-height:normal;font-family:&quot;Helvetica Neue&quot;;margin:0px">
                <br>현재 개발 중이거나, 개발 예정인 상품이 있으신가요?</p>
            <p
                style="font-variant-numeric:normal;font-variant-east-asian:normal;font-stretch:normal;font-size:13px;line-height:normal;font-family:&quot;Helvetica Neue&quot;;margin:0px">
                <br></p>
            <p
                style="font-variant-numeric:normal;font-variant-east-asian:normal;font-stretch:normal;font-size:13px;line-height:normal;font-family:&quot;Helvetica Neue&quot;;margin:0px">
                귀사의 목업 제작 비용 절감을 위해</p>
            <p
                style="font-variant-numeric:normal;font-variant-east-asian:normal;font-stretch:normal;font-size:13px;line-height:normal;font-family:&quot;Helvetica Neue&quot;;margin:0px">
                신규 고객님께<font color="#0b5394">&nbsp;</font><b>
                    <font color="#0000ff">30% 할인 혜택</font>
                </b>을 드리고 있습니다!</p>
            <p
                style="font-variant-numeric:normal;font-variant-east-asian:normal;font-stretch:normal;font-size:13px;line-height:normal;font-family:&quot;Helvetica Neue&quot;;margin:0px">
                <br></p>
            <img src="https://ci6.googleusercontent.com/proxy/-dzfoNC0cb3XCDGSe--vA0TX6JUE-re4oKcq2XBy-VxeepOyimW9okQYNOYCpqrmVeYSCWBgrrt4tvlqy60aPF4aPVnikqrYCHbMHXr6pN7kdiP7A-q6sx3svCxEjYlz8-ll0RUP3w=s0-d-e1-ft#https://raw.githubusercontent.com/gohdong/image_test/master/promotion_final_crop.jpg"
                alt="aasd" width="564 px" height="2053 px" usemap="#m_-5487310236322190759_imgmap202132175313"
                class="CToWUd a6T" tabindex="0">
            <div class="a6S" dir="ltr" style="opacity: 0.01; left: 516px; top: 2141px;">
                <div id=":1bw" class="T-I J-J5-Ji aQv T-I-ax7 L3 a5q" title="다운로드" role="button" tabindex="0"
                    aria-label="첨부파일() 다운로드" data-tooltip-class="a1V">
                    <div class="akn">
                        <div class="aSK J-J5-Ji aYr"></div>
                    </div>
                </div>
            </div>
            <map id="m_-5487310236322190759imgmap202132175313" name="m_-5487310236322190759_imgmap202132175313">
                <area shape="rect" alt="" title="" coords="161,148,275,172"
                    href="https://www.hanyang3d.kr/page/consultation/?utm_source=url_source_mail&amp;utm_medium=url_medium_mail&amp;utm_campaign=url_campaign_mail&amp;utm_content=url_content_mail"
                    target="_blank"
                    data-saferedirecturl="https://www.google.com/url?q=https://www.hanyang3d.kr/page/consultation/?utm_source%3Durl_source_mail%26utm_medium%3Durl_medium_mail%26utm_campaign%3Durl_campaign_mail%26utm_content%3Durl_content_mail&amp;source=gmail&amp;ust=1614934330583000&amp;usg=AFQjCNEF27IGOlKcyu4k840dJFVae1D7Mg">
                <area shape="rect" alt="" title="" coords="285,149,404,172"
                    href="https://www.hanyang3d.kr/?utm_source=url_source_mail&amp;utm_medium=url_medium_mail&amp;utm_campaign=url_campaign_mail&amp;utm_content=url_content_mail"
                    target="_blank"
                    data-saferedirecturl="https://www.google.com/url?q=https://www.hanyang3d.kr/?utm_source%3Durl_source_mail%26utm_medium%3Durl_medium_mail%26utm_campaign%3Durl_campaign_mail%26utm_content%3Durl_content_mail&amp;source=gmail&amp;ust=1614934330583000&amp;usg=AFQjCNELCmMXbUSAnnXfSOeLS_bLMVlilg">
                <area shape="rect" alt="" title="" coords="28,1998,215,2028"
                    href="http://hanyang3d.kr/board/list?bd_id=project_portfolio&amp;cate=&amp;per_page=1/?utm_source=url_source_mail&amp;utm_medium=url_medium_mail&amp;utm_campaign=url_campaign_mail&amp;utm_content=url_content_mail"
                    target="_blank"
                    data-saferedirecturl="https://www.google.com/url?q=http://hanyang3d.kr/board/list?bd_id%3Dproject_portfolio%26cate%3D%26per_page%3D1/?utm_source%3Durl_source_mail%26utm_medium%3Durl_medium_mail%26utm_campaign%3Durl_campaign_mail%26utm_content%3Durl_content_mail&amp;source=gmail&amp;ust=1614934330583000&amp;usg=AFQjCNGojCkx5M_rLo_AqPR4nFTH9KUV3A">
            </map>
            <img src="https://www.google-analytics.com/collect?v=1&tid=UA-145822029-2&cid=*|UNIQID|*&t=event&ec=code_ec_mail&ea=code_ea_mail&cs=code_cs_mail&cm=code_cm_mail&cn=code_cn_mail&cm1=2"/>
            <p
                style="font-variant-numeric:normal;font-variant-east-asian:normal;font-stretch:normal;font-size:13px;line-height:normal;font-family:&quot;Helvetica Neue&quot;;margin:0px">
                <br></p>
            <div style="font-family:gulim,sans-serif">
                <p
                    style="margin:0px;font-variant-numeric:normal;font-variant-east-asian:normal;font-stretch:normal;font-size:13px;line-height:normal;font-family:&quot;Helvetica Neue&quot;;min-height:15px">
                    더욱 자세한 서비스는 홈페이지에서 확인하실 수 있습니다.</p>
            </div>
            <div style="font-family:gulim,sans-serif">
                <p
                    style="margin:0px;font-variant-numeric:normal;font-variant-east-asian:normal;font-stretch:normal;font-size:13px;line-height:normal;font-family:&quot;Helvetica Neue&quot;">
                    <a href="https://www.hanyang3d.kr/?utm_source=url_source_mail&amp;utm_medium=url_medium_mail&amp;utm_campaign=url_campaign_mail&amp;utm_content=url_content_mail" target="_blank">한양3D팩토리
                        홈페이지 바로가기</a></p>
                <p
                    style="margin:0px;font-variant-numeric:normal;font-variant-east-asian:normal;font-stretch:normal;font-size:13px;line-height:normal;font-family:&quot;Helvetica Neue&quot;">
                    <br>궁금하신 점이 있다면 편하게 연락주세요!</p>
                <p
                    style="margin:0px;font-variant-numeric:normal;font-variant-east-asian:normal;font-stretch:normal;font-size:13px;line-height:normal;font-family:&quot;Helvetica Neue&quot;">
                    감사합니다.<br></p>
                <p
                    style="margin:0px;font-variant-numeric:normal;font-variant-east-asian:normal;font-stretch:normal;font-size:13px;line-height:normal;font-family:&quot;Helvetica Neue&quot;">
                    <br></p>
            </div>
        </div>
        <div>
            <div dir="ltr">
                <div dir="ltr">
                    <div dir="ltr">
                        <div dir="ltr"><br></div>
                        <div dir="ltr">
                            <table border="0" cellspacing="0" cellpadding="0"
                                style="margin:0px;padding:0px;font-size:13.33px;font-family:&quot;Malgun Gothic&quot;,&quot;\00b9d1\00c740  \00ace0\00b515&quot;;width:820px;color:rgb(17,17,17);border-top:2px solid rgb(0,0,0)">
                                <tbody>
                                    <tr>
                                        <td style="padding:20px 3px 0px;font-size:10pt;line-height:21.3333px">
                                            <table border="0" cellspacing="0" cellpadding="0"
                                                style="margin:0px;padding:0px;width:815.2px">
                                                <tbody>
                                                    <tr>
                                                        <td
                                                            style="padding:0px 0px 8px;font-size:14px;font-family:&quot;\00b9d1\00c740  \00ace0\00b515&quot;,&quot;Malgun Gothic&quot;,돋움,dotum,sans-serif;line-height:22.4px">
                                                            <p
                                                                style="margin:0px;padding:0px;line-height:22.4px;font-weight:bold">
                                                                <span
                                                                    style="margin:0px;padding:0px;line-height:16px;font-size:7pt"></span>(주)하이쓰리디&nbsp;<span
                                                                    style="margin:0px;padding:0px;line-height:22.4px;color:rgb(40,108,149)">(HY3D)</span>
                                                            </p>
                                                            <p style="margin:0px;padding:0px;line-height:22.4px"><span
                                                                    style="margin:0px;padding:0px;line-height:21.3333px;font-size:10pt">이세윤</span><span
                                                                    style="margin:0px;padding:0px 0px 0px 8px;line-height:19.2px;color:rgb(153,153,153);font-size:12px;vertical-align:middle">3D팩토리팀
                                                                    팀장</span></p>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td
                                                            style="padding:0px;font-size:12px;font-family:&quot;\00b9d1\00c740  \00ace0\00b515&quot;,&quot;Malgun Gothic&quot;,돋움,dotum,sans-serif;line-height:17px">
                                                            <p style="margin:0px;padding:0px;line-height:19.2px"><span
                                                                    style="margin:0px;padding:0px;line-height:19.2px;font-weight:bold">tel</span>
                                                                <font color="#888888"
                                                                    style="margin:0px;padding:0px;line-height:19.2px">
                                                                    &nbsp;070-8015-3244&nbsp;</font>|<font color="#d7d7d7"
                                                                    style="margin:0px;padding:0px;line-height:19.2px">
                                                                </font>
                                                                <font color="#888888"
                                                                    style="margin:0px;padding:0px;line-height:19.2px">&nbsp;
                                                                </font><b>phone</b>
                                                                <font color="#888888"
                                                                    style="margin:0px;padding:0px;line-height:19.2px">
                                                                    &nbsp;010-<wbr>5504-0938</font>
                                                            </p>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td style="padding:0px;line-height:17px">
                                                            <p
                                                                style="margin:0px;padding:0px;line-height:19.2px;font-size:12px;font-family:&quot;\00b9d1\00c740  \00ace0\00b515&quot;,&quot;Malgun Gothic&quot;,돋움,dotum,sans-serif;color:rgb(136,136,136)">
                                                                <span
                                                                    style="margin:0px;padding:0px;line-height:19.2px;color:rgb(17,17,17);font-weight:bold">address</span>&nbsp;
                                                                경기 안산시 상록구 한양대학로 55 창업보육센터 204호</p>
                                                            <p style="margin:0px;padding:0px;line-height:21.3333px"><b
                                                                    style="font-family:&quot;\00b9d1\00c740  \00ace0\00b515&quot;,&quot;Malgun Gothic&quot;,돋움,dotum,sans-serif;font-size:12px">homepage</b>
                                                                <font color="#888888"
                                                                    style="margin:0px;padding:0px;line-height:19.2px;font-family:&quot;\00b9d1\00c740  \00ace0\00b515&quot;,&quot;Malgun Gothic&quot;,돋움,dotum,sans-serif;font-size:12px">
                                                                    &nbsp;</font><a href="https://www.hanyang3d.kr/?utm_source=url_source_mail&amp;utm_medium=url_medium_mail&amp;utm_campaign=url_campaign_mail&amp;utm_content=url_content_mail"
                                                                    rel="noreferrer noopener"
                                                                    style="background-color:transparent;font-size:10pt"
                                                                    target="_blank">www.hanyang3d.kr</a>
                                                            </p>
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """.format(asparagus_cid=asparagus_cid[1:-1]), subtype='html')
    print("=================================================================")
    print("sending to ==> " + msg['to'])
    s.sendmail(msg['from'],msg['to'], msg.as_string())
    print(str(int(count*100/len(data)))+"% "+"completed "+str(count)+"/"+str(len(data)))
    print("sleep 5 seconds")
    for y in range(0,5):
        print(str(5-y)+"...")
        time.sleep(1)




s.quit()

