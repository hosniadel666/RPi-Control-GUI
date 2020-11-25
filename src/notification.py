 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

 class Notification(object):  
    def __init__():
        self.sender_address = 'xxxxxxxxxxxxxxxxxxxxxx'
        self.sender_pass = 'xxxxxxxxxxxxx'
        self.receiver_address = 'xxxxxxxxxxxxxxxxx' 

        self.message = MIMEMultipart()
        self.message['From'] = sender_address
        self.message['To'] = receiver_address
        self.message['Subject'] = "Attention !"

    def send_mail(mail_content):
        # The mail addresses and password
        #The body and the attachments for the mail
        self.message.attach(MIMEText(mail_content, 'plain'))
        #Create SMTP session for sending the mail
        self.session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        self.session.starttls() #enable security
        self.session.login(sender_address, sender_pass) #login with mail_id and password
        self.text = message.as_string()
        self.session.sendmail(sender_address, receiver_address, text)
        self.session.quit()
    
   