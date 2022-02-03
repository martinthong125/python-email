import re


def check(email):

    # pass the regular expression
    # and the string into the fullmatch() method
    if re.fullmatch(email_regex, email):
        print("Valid Email")

    else:
        print("Invalid Email")


def get_email():
    """
    This function will ensure that the user key in a valid email address.

    Returns:
        str: recipient email address
    """

    email = input("Enter the recipent email address: ")
    while re.fullmatch(email_regex, email) == None:
        print("You have entered an invalid email address.")
        email = input("Enter a valid recipent email address: ")
    return email


email_regex = r"\b[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}\b"
# check("martin125@gmail.com.sg")
get_email()
