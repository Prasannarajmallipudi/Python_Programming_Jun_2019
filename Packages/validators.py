import re
def phoneNumberValidator(phone):
    pattern = '^[9876][0-9]{9}$|^[0][6-9][0-9]{9}$|^[+][9][1][6-9][0-9]{9}$'
    if re.match(pattern, str(phone)):
        return True
    return False
#phoneNumberValidator(9494699851)  


def emailValidator(email):
    pattern = '^[a-z0-9][0-9a-z_.]{3,14}[@][a-z0-9.]{3,18}[.][a-z]{2,4}$'
    if re.match(pattern, email):
        return True
    return False
emailValidator('venkatesh@gmail.com') 
phoneNumberValidator(7569456282)