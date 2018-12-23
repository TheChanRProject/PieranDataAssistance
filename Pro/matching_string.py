def myfunc(string_pass):
    string_list = list(string_pass)
    counter = 1
    while counter < len(string_list):
        if counter % 2 == 0:
            string_list[counter - 1] = string_list[counter - 1].upper()
        else:
            string_list[counter - 1] = string_list[counter - 1].lower()

        counter += 1

    return print(''.join(string_list))

myfunc("testing")
