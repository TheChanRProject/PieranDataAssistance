from collections import OrderedDict

message = input("Put in your message here: ")
message_list = list(message)

# Create an ordered set
message_set = OrderedDict.fromkeys(message_list)

# Message Dictionary
mDict = {}
for i in message_set:
    mDict[i] = message_list.count(i)

newStrList = []
for key,val in mDict.items():
    newStrList.append(key*(val+1))

newMessage = ''.join(newStrList)

print(newMessage)
