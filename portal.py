import re

# Validate email address
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(pattern, email):
        print("Valid email address")
    else:
        print("Invalid email address")


# Validate phone number (10 digits)
def validate_phone(phone):
    pattern = r'^[6-9][0-9]{9}'

    if re.match(pattern, phone):
        print("Valid phone number")
    else:
        print("Invalid phone number")


# Extract transaction IDs from logs
def extract_transaction_ids(log):
    pattern = r'[0-9]{2}'
    ids = re.findall(pattern, log)

    if ids:
        print("Transaction IDs:", ids)
    else:
        print("No transaction IDs found")


# Main program
print("ONLINE REGISTRATION VALIDATION")

email = input("Enter email address: ")
validate_email(email)

phone = input("Enter 10-digit phone number: ")
validate_phone(phone)

log = input("Enter transaction log: ")
extract_transaction_ids(log)