# Version two merging from two lists

message = input("Put in your message here: ")
message_list = list(message)


# Dictionary from list comprehension

mDict = {i: message_list.count(i) for i in message_list}

keys = list(mDict.keys())
values= list(mDict.values())

# New Message
newMessage = ''.join([(value+1)*key for key,value in zip(keys,values)])
print(newMessage)
