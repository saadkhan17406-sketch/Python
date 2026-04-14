#https://github.com/saadkhan17406-sketch/Python
print ("UIN : 251A053")
import re
def validate_phone(phone):

    pattern = r"^(\+91[\-\s]?)?[6-9]\d{9}$"
    return re.match(pattern, phone)
def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email)

phone = input("Enter your phone number: ")
email = input("Enter your email ID: ")

if validate_phone(phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")

if validate_email(email):
    print("Valid Email ID")
else:
    print("Invalid Email ID")