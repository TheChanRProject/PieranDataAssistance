message = input("Put in your message here: ")
message_list = list(message)

# Create a dictionary
message_set = set(message_list)
print(message_set)

# Set up dictionary

for letter in message_set:
    message_dict = {letter : message_list.count(letter)}
    print(message_dict['y'])
