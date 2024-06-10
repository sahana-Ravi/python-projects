import smtplib


email_sender = 'shvesa99@gmail.com'

email_password = 'Ilovecoading@123*'


# creates SMTP session

s = smtplib.SMTP('smtp.gmail.com', 465, timeout=10)
s.ehlo()


# start TLS for security

s.starttls()

# Authentication

s.login("email_sender", "email_password")

# message to be sent

message = "hello!!"

# sending the mail
print("8")
s.sendmail("shvesa99@gmail.com", "shvesa99@gmail.com", message)

# terminating the session

s.quit()

print("sent..")
