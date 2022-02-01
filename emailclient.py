#!/usr/bin/python3
"""
Email Client by Martin Thong, version 1.3
Features:
1. Hide user email and password. Stored under environment variables
2. Get user to key in recipent email, subject title and body of email
3. Check for validity of email address
4. Option to change subject title and body of email
5. Preview before sending email
6. Option to cancel sending email
7. Login success message or catch login credentials error.
"""

import os
import smtplib


def get_email():
    """
    This function will ensure that the user key in a valid email address.

    Returns:
        str: recipient email address
    """

    email = input("Enter the recipent email address: ")
    while email.count("@") != 1 or email.count(".") < 1 or email.count(" ") > 0:
        email = input("Enter a valid recipent email address: ")
    return email


def get_subject():
    """
    This function allows the user to key in the subject header till satisfied.

    Returns:
        str: subject text
    """

    subject = input("Type your subject header: ")
    choice = input("Do you want to change your subject header? (Y/N): ")
    while choice.upper() == "Y":
        subject = input("Type your subject header: ")
        choice = input("Do you want to change your subject header? (Y/N): ")
    return subject


def get_body():
    """
    This function allows the user to key in the body text till satisfied.

    Returns:
        str: body text
    """

    body = input("Type your body text: ")
    choice = input("Do you want to change your body text? (Y/N): ")
    while choice.upper() == "Y":
        body = input("Type your body text: ")
        choice = input("Do you want to change your body text? (Y/N): ")
    return body


def print_email(email, subject, body):
    """
    This function will print a summary of how the email looks like.

    Args:
        email (str): recipient email address
        subject (str): subject text
        body (str): body text
    """

    print("*" * 40)
    print(f"From: {EMAIL_ADDRESS}")
    print(f"To: {email}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    print("*" * 40)


def confirm_send(email, subject, body, EMAIL_ADDRESS):
    """
    This function allows the user to finalise the email before sending out.

    Args:
        email (str): recipient email address
        subject (str): subject text
        body (str): body text
        EMAIL_ADDRESS (str): user email address
    """

    confirm = input("Confirm send email? (Y/N): ")
    if confirm.upper() == "Y":
        msg = f"Subject: {subject}\n\n{body}"
        # print(msg)
        smtp.sendmail(EMAIL_ADDRESS, email, msg)
        print(f"Email sent to: {email}")
    else:
        print("You have chosen not to send the email.")


# Script starts here

# get sensitive data from environment variables
# https://www.youtube.com/watch?v=IolxqkL7cD8&t=0s
EMAIL_ADDRESS = os.environ.get("EMAIL_ID")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")
# print(EMAIL_ADDRESS)
# print(EMAIL_PASSWORD)

try:
    # Testing code through localhost before actual sending
    # https://www.youtube.com/watch?v=JRCJ6RtE3xU&t=590s
    # with smtplib.SMTP('localhost', 1025) as smtp:
    # python -m smtpd -c DebuggingServer -n localhost:1025
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

        # Check login credentials
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        print("Login to your email account successfully!")

        # Get user input and display them before sending email
        email = get_email()
        subject = get_subject()
        body = get_body()
        print_email(email, subject, body)

        # Confirm sending email?
        confirm_send(email, subject, body, EMAIL_ADDRESS)

except:
    # Failure could be due to wrong login credentials or recipient email
    print("Fail to send email!")
    print("Check your login credentials or recipent email.")
    # https://www.youtube.com/watch?v=JRCJ6RtE3xU

# End of script
