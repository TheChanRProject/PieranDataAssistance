def email_validator():
    input_email = input("Type in a valid email address: ")
    if not isinstance(input_email, str):
        raise TypeError
    at_index = input_email.find('@')
    domain_index = input_email.find('.com') 
