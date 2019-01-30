function newString(string) {
  const strArr = string.split('')
  var count = {};
  for (var i = 0; i < strArr.length; i++) {
    if ((string.match(new RegExp(strArr[i], "g"))).length >= 1) {
      count[string[i]] = (string.match(new RegExp(string[i], "g"))).length;
    }
  }
  return count
}

newString('yeah')
