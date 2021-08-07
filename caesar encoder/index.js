const abc = "abcdefghijkljmnopqrstuvwxyzabcdefghijkljmnopqrstuvwxyzabcdefghijkljmnopqrstuvwxyz".split('');

let decoded = "Tomi szereti az almat".toLocaleLowerCase().split('');
let key = "asd".toLocaleLowerCase().split('');
let keyValues = []
let txtValues = []
let encodedValues = [];
let encoded = ''.toLowerCase();
let decodedValues = [];

encode()

function encode(){
while(key.length < decoded.length){
    key += key
}

for(let x = 0;x<key.length;x++){
    keyValues[x] = (abc.indexOf(key[x]) + 1);
}
console.log(`keyValues: ${keyValues}`);

for(let x = 0;x<decoded.length;x++){
    txtValues[x] = abc.indexOf(decoded[x]);
}
console.log(`txtValues: ${txtValues}`);

for(let x = 0;x<decoded.length;x++){
    encodedValues[x] = (txtValues[x] + keyValues[x])
}
console.log(`encodedValues: ${encodedValues}`);

for(let x = 0;x<encodedValues.length;x++){
    encoded += abc[encodedValues[x]]
}
console.log(`Encded: ${encoded}`);
}

function decode(){
    encoded = encoded.split('')

    while(key.length < encoded.length){
        key += key
    }
    
    for(let x = 0;x<key.length;x++){
        keyValues[x] = (abc.indexOf(key[x]) + 1);
    }
    console.log(`keyValues: ${keyValues}`);
   
    for(let x = 0;x<encoded.length;x++){
        encodedValues[x] = (abc.indexOf(encoded[x]));
    }
    console.log(`encodedValues: ${encodedValues}`);
    for(let x = 0;x<decoded.length;x++){
        decodedValues[x] = (encodedValues[x] - keyValues[x])
    }
    for(let x = 0;x<encodedValues.length;x++){
        decoded += abc[decodedValues[x]]
    }
    console.log(`Decoded: ${decoded}`);
}