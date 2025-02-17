import os
import smtplib

# Correct Gmail SMTP settings
HOST = 'smtp.gmail.com'
PORT = 587

FROM_MAIL = '21911a3548@vjit.ac.in'
TO_MAIL = 'rockyvijju8@gmail.com'

# Ensure App Password is correctly set (without spaces)
PASSWORD = 'hsxxhpoyzafiamnu'  # Use the App Password from Google

MESSAGE = """Subject: Test Email via Gmail

Hi, this is a test email sent using Python and Gmail SMTP.
"""

try:
    with smtplib.SMTP(HOST, PORT) as smtp:
        smtp.ehlo()  # Identify ourselves
        smtp.starttls()  # Secure connection
        smtp.ehlo()  # Re-identify after securing connection
        smtp.login(FROM_MAIL, PASSWORD)  # Use App Password

        smtp.sendmail(FROM_MAIL, TO_MAIL, MESSAGE)
        print("[*] Email sent successfully!")

except smtplib.SMTPAuthenticationError:
    print("[!] Authentication failed. Double-check your email and App Password.")
except smtplib.SMTPConnectError:
    print("[!] Unable to connect to Gmail SMTP server.")
except Exception as e:
    print(f"[!] Error: {e}")
