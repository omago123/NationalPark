from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
import hashlib
import smtplib
from email.mime.text import MIMEText


def send_mail(from_email, to_email, msg):
    # SMTP 설정
    smtp = smtplib.STMP_SSL('stmp.gmail.com', 587)
    # 인증정보 설정
    smtp.login(from_email, 'cofcuqsulcxfvjxu')
    msg = MIMEText(msg)
    # 제목
    msg['Subject'] = '[문의사항]' + to_email
    # 수신 이메일
    msg['To'] = from_email
    smtp.sendmail(from_email, from_email, msg.as_string())
    smtp.quit()

    
def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        # 발신자주소, 수신자주소, 메시지
        send_mail('nagyeomhan91@gmail.com', email, comment)
        return render(request, 'contact_success.html')
    return render(request, 'contact.html')