function newString(string) {
  const strArr = string.split('')
  var counts = {};
  for (var i = 0; i < strArr.length; i++) {
    if ((string.match(new RegExp(strArr[i], "g"))).length >= 1) {
      counts[string[i]] = (string.match(new RegExp(string[i], "g"))).length;
    }
  }
  var countArr = Object.entries(counts)
  var newStrArr = []
  for(const [key,value] in countArr) {
    var product = key.repeat(value + 1)
    newStrArr.push(product)
  }
  return newStrArr 
}

newString('yeah')
