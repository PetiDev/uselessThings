let num = 300;
let szam = "",sad;
function toBinariy(asd) {
        if(num<1){
             console.log("A számod: \n" + szam.split("").reverse().join(""));
            return;
            }
    sad = asd % 2;
    szam += `${sad}`;
    num = Math.floor(num / 2);
    toBinariy(num)
}
toBinariy(num)