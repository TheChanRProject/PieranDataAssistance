import re

def stringExtract():
    text = input("Input some text: ")
    character_indices = input("What characters do you want to check index: ")
    indexList = [i.start() and i.end() for i in re.finditer(character_indices, text)]
    print(indexList)
    n = int(input("At which index do you want to remove?: "))
    # Now you can choose which specific character you want to remove
    extract_text_from_index = text[:n-1] + text[n:]
    print(f"This is the new text: {extract_text_from_index}")
    # Want to extract anything else?
    other_text = input("Input what else you want to extract: ")
    extract_other_text = extract_text_from_index.replace(other_text, '')
    return extract_other_text
