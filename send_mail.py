import smtplib
from email.mime.text import MIMEText
def send_mail(customer, address, rating, comments):
    port=2525
    smtp_server='smtp.mailtrap.io'
    login='1a3c79cf284920'
    password='9530126fd6dda4'
    message=f"<h3>New Feedback Submission</h3><ul><li>Customer:{customer}</li><li>Address:{address}</li><li>Rating:{rating}</li><li>Comments:{comments}</li></ul>"
    sender_email='examil1@example.com'
    receiver_email='email2@example.com'
    msg=MIMEText(message, 'html')
    msg['Subject']='Aritzia Feedback'
    msg['From']=sender_email
    msg['To']=receiver_email

    #Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email,receiver_email, msg.as_string())
    