def email_validator():
    input_email = input("Type in a valid email address: ")
    if '@' in input_email:
        at_index = input_email.find('@')
        email_prefix = input_email[: at_index]
        email_domain = input_email[at_index + 1:]
        if '.' in input_email and email_domain[0] == input_email[at_index + 1]:
            message = "This email is valid."
    else:
        message = "Please write a valid email address and try again."
    return message
print(email_validator())
print(email_validator())
print(email_validator())
