# This is the main tool, please go to the README.md file for more information and instructions! If you run into any issues, please message me on Slack or open an issue on GitHub!

import json
import time
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

# Enter email address and app password
SENDER_EMAIL =  input("Please enter your email address: ").strip()
SENDER_PASSWORD = input("Please enter your app password: ").strip()

# Enter subject
SUBJECT = input("Please enter the subject of the email: ")
while not SUBJECT:
    SUBJECT = input("The email's subject cannot be empty. Please try again: ")

# Enter email content
EMAIL_CONTENT = input("Please enter the content of the email: ")
while not EMAIL_CONTENT:
    EMAIL_CONTENT = input("The email's content cannot be empty. Please try again: ")

# Enter sender name
SENDER_NAME = input("Please enter your name (to end the email with): ").strip()
while not SENDER_NAME:
    SENDER_NAME = input("The signature's name cannot be empty. Please try again: ")

# Enter max number of emails to send and validate
while True:
    try:
        MAX_EMAILS = int(input("Please enter the maximum number of emails to send (1-499): ").strip())
        if 1 <= MAX_EMAILS <= 499:
            break
        else:
            print("Please enter a number between 1 and 499.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Enter path to JSON file and validate
while True:
    FILE_PATH = input("Please enter the path to the JSON file containing contact data: ").strip()
    if os.path.exists(FILE_PATH) and os.path.isfile(FILE_PATH):
        try:
            with open(FILE_PATH, "r") as f:
                contact_data = json.load(f)
            break
        except Exception as e:
            print(f"Error reading JSON file: {e}")
            continue
    else:
        print("File does not exist or is not a valid JSON file. Please try again.")


# Email template with placeholder for name
email_template = """
Hi {first_name},<br><br>
{email_content}<br><br>
Best regards,<br>
{sender_name}
"""

sent_count = 0

# Start SMTP session
with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
    server.login(SENDER_EMAIL, SENDER_PASSWORD)

    for contact in contact_data:
        if sent_count >= MAX_EMAILS:
            break

        email = contact.get("Email")
        name = contact.get("Name")

        if not email or "@" not in email or not name:
            continue

        # Extract first name (assumes first token in full name)
        first_name = name.split()[0].strip(",") if name else "there"

        # Compose message
        personalized_message = email_template.format(
            first_name=first_name,
            email_content=EMAIL_CONTENT,
            sender_name=SENDER_NAME
        )

        msg = MIMEMultipart("alternative")
        msg["From"] = SENDER_EMAIL
        msg["To"] = email
        msg["Subject"] = SUBJECT

        msg.attach(MIMEText(personalized_message, "html"))

        try:
            server.sendmail(SENDER_EMAIL, email, msg.as_string())
            print(f"Count: {sent_count + 1} | Email sent to {email}")
            sent_count += 1
            time.sleep(5) # Sleep here to not overload the server
        except Exception as e:
            print(f"Failed to send to {email}: {e}")

print(f"\nDone! Successfully sent {sent_count} emails.")
