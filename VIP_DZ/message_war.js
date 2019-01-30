from collections var OrderedDict = require('OrderedDict');

message = input('Put in your message here: ');
message_list = list(message);

// Create an ordered set
message_set = OrderedDict.fromkeys(message_list);

// Message Dictionary
mDict = {};
for (i in message_set) {
    mDict[i] = message_list.count(i);
}
newStrList = [];
for (key,val in mDict.items()) {
    newStrList.push(key*(val+1));
}
newMessage = ''.join(newStrList);

console.log(newMessage);
