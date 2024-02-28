import re

def validate_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(regex, email):
        return False

    username, domain = email.split('@')
    if '.' not in domain:
        return False

    return True

# Example usage
email_to_test = "my_email@example.com"
if validate_email(email_to_test):
    print("Valid email address")
else:
    print("Invalid email address")
