import ssl,smtplib
port=465
Email=input("enter your mail")
Password=input("enter your password")
Recipient=input("enter the mail addresss")
Subject=input("enter the subject to send tha mail")
text=input("type of your text")
Message="Subject:{}\n\n{}".format(Subject,text)
context = ssl.create_default_context()
with smtplib.SMTP_SSL("gmpgovinda.gmail.com",port,context=context) as servers:
        server.login(email,password)
        server.sendmail(Email, Recipient,Message)
