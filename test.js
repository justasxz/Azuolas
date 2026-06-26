
const x = parseFloat(process.argv[2]);
const y = parseFloat(process.argv[4]);
const action = process.argv[3];
if(x == null || y == null || action == null){
    console.log("insufficient arguments, must use 3!");
    process.exit(1);
}
switch(action){
    case '+':
    sum = x+y;
    console.log(x + " + " + y + " = " + sum);
    break;
    case '-':
    sum = x-y;
    console.log(x + " - " + y + " = " + sum);
    break;
    case '/':
    if(y == 0){console.log("Can't divide by 0!");  process.exit(1);}
    sum = x/y;
    console.log(x + " / " + y + " = " + sum);
    break;
    case '%':
    if(y == 0){console.log("Can't divide by 0!");  process.exit(1);}
    sum = x%y;
    console.log(x + " % " + y + " = " + sum);
    break;
    case '*':
    sum = x*y;
    console.log(x + " * " + y + " = " + sum);
    break;
    case '^':
    if(y > 0){
    sum = Math.pow(x,y);
    }
    else if(y < 0){
        if(x < 0){console.log("Can't root negative numbers!");  process.exit(1);}
        sum = Math.pow(x,1/(y*-1));
    }
    else sum = 1;
    console.log(x + " ^ " + y + " = " + sum);

    break;
}


// amzius = 12
// console.log(amzius)