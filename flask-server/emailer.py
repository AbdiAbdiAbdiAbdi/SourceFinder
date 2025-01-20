import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from news import News_Getter
from dotenv import load_dotenv
import os



def send_email(text, email):

    sender_email = os.getenv('sender_email')
    to_email = email
    search_query = text
    answer = News_Getter(search_query)
    #Returns a nested list where answer[i][0] is Title, answer[i][1] is Summary, and answer[i][2] is URL Link

    subject = "Your Email from SourceFinder"
    body = f"Thank You for Using SourceFinder. Here are your results for {text}: \n\n"

    for i in range(len(answer)):
        body += f"\n{answer[i][0]}\n"
        body += f"\n{answer[i][1]}\n"
        body += f"\nUse this Link to Learn More: {answer[i][2]}"
        body += "\n\n\n"


    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = to_email
    message['Subject'] = Header(subject, 'utf-8') #allows for all unicode to be represented in subject

    message.attach(MIMEText(body, 'plain', 'utf-8')) #allows for all unicode in body


    try:
        #Start SMTP server connection
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, os.getenv('loginD'))

        #Sends the email
        server.sendmail(sender_email, to_email, message.as_string())
        server.quit() #To not allow for excess runtime
        return "Email was sent successfully."
        


    except Exception as E:
        server.quit() #To not allow for excess runtime
        return f"Failed to send email: {E}"
