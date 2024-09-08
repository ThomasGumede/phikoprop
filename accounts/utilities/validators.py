import uuid, re, logging
from datetime import datetime
from django.core.validators import URLValidator
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

def validate_sa_id_number(id_number):
    error_messages = error_messages = {"success": True, "message": "ID number is valid"}

    if not re.match(r'^\d{13}$', id_number):
        error_messages = {"success": False, "message": "ID number should contain 13 numbers"}

    year = int(id_number[0:2])
    month = int(id_number[2:4])
    day = int(id_number[4:6])

    try:
        dob = datetime(year + 1900, month, day)

    except ValueError:
        error_messages = {"success": False, "message": "Your ID number is invalid"}

    if not (int(id_number[10]) in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
        error_messages = {"success": False, "message": "Your ID number is invalid"}

    check_sum = 0
    for i in range(13):
        digit = int(id_number[i])
        if i % 2 == 0:
            check_sum += digit
        else:
            check_sum += sum(divmod(digit * 2, 10))
    valid_check = check_sum % 10 == 0
    if not valid_check:
        error_messages = {"success": False, "message": "Your ID number is invalid"}

    return error_messages

def verify_rsa_phone():
    PHONE_REGEX = RegexValidator(r'^(\+27|0)[1-9][0-9]{8}$', 'RSA phone number is required')
    return PHONE_REGEX
