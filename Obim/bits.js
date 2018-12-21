myVar = "0101"
myVarFlipped = ~parseInt(myVar,2)
console.log(myVarFlipped)


function dec2bin(dec){
    return (dec >>> 0).toString(2);
}

console.log(dec2bin(256))
console.log(dec2bin(-256))


