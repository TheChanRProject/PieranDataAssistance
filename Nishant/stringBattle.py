def stringBattle_sliced(factor):
    if not isinstance(factor, int or float):
        raise TypeError
    myString = input("Type in your opponent's text: ")
    if not isinstance(myString, str):
        raise TypeError
    newLength = len(myString[1:]) + factor
    newStr = myString[0] + (newLength * myString[1:])
    return newStr



def stringBattle_NLetters(factor):
    if not isinstance(factor, int or float):
        raise TypeError
    myString = input("Type in your opponent's text: ")
    if not isinstance(myString, str):
        raise TypeError
    letterArray = list(myString)
    letterHashTable = {i:myString.count(i) for i in letterArray}
    newArray = []
    for key,val in letterHashTable.items():
        newArray.append(key*(val+factor))
    newStr = ''.join(newArray)
    filename = '/Users/rchatter/Desktop/DS/Python/PieranDataAssistance/Nishant/battle.txt'
    file = open(filename, 'w')
    file.write(newStr)
    file.close()
    print(newStr)
    return newStr

stringBattle_NLetters(5);
