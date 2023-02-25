from validate_email import validate_email

def is_valid_email(email):
    # Check if the email address is valid
    is_valid = validate_email(email)

    # Return True if the email address is valid, False otherwise
    return is_valid