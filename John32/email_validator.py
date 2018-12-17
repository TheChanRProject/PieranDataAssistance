def email_validator():
    input_email = input("Type in a valid email address: ")
    if not isinstance(input_email, str):
        raise TypeError
    if '@' in input_email:
        at_index = input_email.find('@')
        email_prefix = input_email[: at_index]
        email_domain = input_email[at_index + 1:]
        if '.' in input_email and email_domain[0] == input_email[at_index + 1]:
            return "This email is valid."
        else:
            return "Please write a valid email address and try again."
