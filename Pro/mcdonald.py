def old_mcdonald(name):
    chars = name
    newName = chars[0].upper() + chars[1:3] + chars[3].upper() + chars[4:]
    return newName

print(old_mcdonald('mcdonald'))
