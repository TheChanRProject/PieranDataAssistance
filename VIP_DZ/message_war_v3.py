# Version two merging from two lists
message_list = list(input("Put in your message here: "))
# Dictionary from list comprehension
mDict = {i: message_list.count(i) for i in message_list}
# New Message
newMessage = ''.join([(value+1)*key for key,value in mDict.items()])
print(newMessage)
