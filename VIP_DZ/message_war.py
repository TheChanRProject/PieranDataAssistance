from collections import OrderedDict

message = input("Put in your message here: ")
message_list = list(message)

# Create an ordered set

message_set = OrderedDict.fromkeys(message_list)
print(list(message_set.keys()))
# Message Dictionary

mDict = {}
for i in message_set:
    mDict[i] = message_list.count(i)
    print(mDict)

# Adding extra letter
newMessage = []
