def skyline(input_string: str):
    letters = list(input_string)
    new_string = []
    for i in range(len(letters)):
        if i % 2 == 0:
            new_string.append(letters[i].upper())
        else:
            new_string.append(letters[i].lower())
    return ''.join(new_string)
print(skyline("apple"))
    
