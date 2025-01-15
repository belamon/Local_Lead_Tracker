#this file is used to store validation function 
import re
from datetime import datetime

def is_valid_email(email):
    """Validate the format of an email address."""
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def is_valid_phone_number(phone_number):
    #this is regex pattern to allow numbers, spaces, +, _, and parentheses
    pattern = r'^\+?[0-9\s\-()]{7,15}$'

    #validate phone number
    if re.match(pattern, phone_number):
        return True
    else:
        print("Invalid phone number. Please enter a 10-digit number, e.g., 123-456-7890.")
        return False
    
def validate_date(date_created):
    """This is a function to validate if an input date is in the correct format

    Returns True if valid, False otherwise
    """
    try:
        #try to parse the input date using the format 'yyyy/mm/dd'
        datetime.strptime(date_created, "%Y/%m/%d")
        return True
    except ValueError:
        print("Invalid date. Please enter a date in the format 'yyyy/mm/dd'.")
        return False
    
