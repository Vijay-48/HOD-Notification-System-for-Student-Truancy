# utils/notification.py

import smtplib
from email.mime.text import MIMEText
from config.model_config import NOTIFICATION_CONFIG

def send_email_notification(student_details, additional_info=""):
    """
    Send an email notification with student details to the HOD.
    """
    email_config = NOTIFICATION_CONFIG['email']
    subject = "Truancy Alert: Student Identified"
    body = (f"Student Details:\n"
            f"Name: {student_details.get('name')}\n"
            f"ID: {student_details.get('id')}\n"
            f"Email: {student_details.get('email')}\n\n"
            f"{additional_info}")
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = email_config['from_email']
    msg['To'] = email_config['to_email']

    try:
        server = smtplib.SMTP(email_config['smtp_server'], email_config['smtp_port'])
        server.starttls()
        server.login(email_config['username'], email_config['password'])
        server.sendmail(email_config['from_email'], [email_config['to_email']], msg.as_string())
        server.quit()
        print("Notification sent to HOD.")
    except Exception as e:
        print("Failed to send email:", str(e))
