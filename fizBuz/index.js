let fizBuz = [];
for(let x = 1;x<100;x++){
    if(x % 3 == 0 && x % 5 == 0){
        fizBuz[x] = 'fizBuz';
    }else if(x % 3 == 0){
        fizBuz[x] = 'fiz';
    }else if(x % 5 == 0){
        fizBuz[x] = 'buz';
    }else{
        fizBuz[x] = x;
    }
}
console.log(fizBuz);