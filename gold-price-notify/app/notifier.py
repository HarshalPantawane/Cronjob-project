import smtplib
from email.mime.text import MIMEText
import os

def send_email(message):
    sender = os.getenv("EMAIL_SENDER")
    receiver = os.getenv("EMAIL_RECEIVER")
    password = os.getenv("EMAIL_PASSWORD")
    
    if not all([sender, receiver, password]):
        print("Error: Email environment variables not set")
        return False
    
    try:
        msg = MIMEText(message)
        msg["Subject"] = "Gold Price Update"
        msg["From"] =  sender
        msg["To"] = receiver
        
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender, password)
            server.send_message(msg)
        
        print("Email sent successfully")
        return True
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
        return False
    except Exception as e:
        print(f"Error sending email: {e}")
        return False
        