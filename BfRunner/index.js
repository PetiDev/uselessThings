let bf = "++++++++[->+++++++++<]>.<++++[->++++++<]>+.<+++[->++++<]  >+.-------.>++++++++[->++++++++<]>-.".replace(/\s*/g,'').split('');

let bits = [0];
const emptyBit = 0;
let currentBit = 0;
let Loop = undefined;
let fullOutput = '';
const processLength = bf.length;


for (let step = 0; step < processLength; step++) {
    switch (bf[step]) {
        case '+':

            bits[currentBit] = bits[currentBit] + 1
            break;

        case '-':
            if ((bits[currentBit] - 1) < 0) return console.log("Minus number's don't exist in this world");
            bits[currentBit] = bits[currentBit] - 1
            break;

        case '>':
            currentBit = currentBit + 1;
            if (!bits[currentBit]) bits.push(emptyBit);
            break;

        case '<':
            if ((currentBit - 1) < 0) {
                return console.log("There is no bits")
            } else {
                currentBit = currentBit - 1
            }
            break;

        case '[':
            Loop = step;
            break;

        case ']':
            if (!(bits[currentBit] == 0)) step = Loop;
            break;

        case '.':
            console.log(String.fromCharCode(bits[currentBit]))
            fullOutput += String.fromCharCode(bits[currentBit]);
            break;

        default: console.log("Illegal move!");
    }
}

console.log(bits)
console.log(fullOutput)