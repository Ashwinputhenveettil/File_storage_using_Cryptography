import smtplib

def sendmail(skey, skey1, skey2, email1):
    TO = email1
    SUBJECT = 'Digital Signature'
    TEXT = "key1:" + skey + " ----------" + "key2:" + skey1 + " ----------" + "key3:" + skey2

    print(TEXT)
    
    # Replace with your Gmail credentials (use App Password if 2FA is enabled)
    gmail_sender = "email_id"
    gmail_passwd = "password(use app password)"

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_sender, gmail_passwd)

        BODY = '\r\n'.join([
            f'To: {TO}',
            f'From: {gmail_sender}',
            f'Subject: {SUBJECT}',
            '',
            TEXT
        ])

        server.sendmail(gmail_sender, [TO], BODY)
        print(' Email sent successfully!')
    except Exception as e:
        print(' Error sending mail:', e)
    finally:
        server.quit()
