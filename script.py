import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def email_send(workflow_name, repository_name):

    sender_email= os.getenv('SENDER_EMAIL')
    sender_password=os.getenv('SENDER_PASSWORD')
    reciever_email= os.getenv('RECIEVER_EMAIL')

    subject= f"{ workflow_name } failed failed of { repository_name } "
    body= f" Hi, your Workflow has been failed named { workflow_name } of { repository_name }"

    message=MIMEMultipart()
    message['From']= sender_email
    message['To']= reciever_email
    message['Subject']=subject
    message.attach(MIMEText(body, "plain"))


    try:
        server= smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text=message.as_string()
        server.sendmail(sender_email, reciever_email, text)
        server.quit()

        print("EMAIL SENT SUCCESSFULLY")
    
    except Exception as e:
        print(f"Error: {e}")



email_send(os.getenv('WORKFLOW_NAME'), os.getenv('REPOSITORY_NAME'))