"use strict"; //To fully enable all features of modern JavaScript
alert("I'm Javascript!");
// юху комменты 

alert("Hello");


let message = "hello";
alert(message);

var anotherMessage = "What'up";
alert(anotherMessage);

const myBirthday = "21.10.2003";

//2.4
//1)
let admin, name;
name = "John";
admin = name;
alert(admin);
//2)
let ourPlanetName;
let curUserName;


//2.5
console.log(55684 + 6);
alert( `Hello, ${admin}!` );
console.log(typeof(message))

//2.6
let age  = prompt("How old are u?");
alert (`u r ${age} years old`);


let isStudent = confirm("Are u a student?");
alert(isStudent);


let name2 = prompt("What is ur name?");
alert(`hello, ${name2}`)

//2.7
let num = 5;
num  = String(num) // Number(), Boolean()
console.log(typeof num)

//2.8
let x = 1;
x = -x
console.log(x)

alert( '1' + 2 ); // "12"

alert(2 + 2 + '1' ); // "41" and not "221"
alert('1' + 2 + 2); // "122" and not "14"


let a = 1;
let b = 2;
let c = 3 - (a = b + 1);

alert( a ); // 3
alert( c ); // 0

let num1 = +prompt("First number?", 1);
let num2 = +prompt("Second number?", 2);

alert(num1 + num2);

//2.9

alert( 0 === false );//strict equality operator -> answer is false, because the types are different
alert( undefined == 0 ); // false (3)
alert( null === undefined ); // false

//2.10

let year = prompt('In which year was ECMAScript-2015 specification published?', '');

// if (year < 2015){
//     alert('Malo');
// }else if (year > 2015){
//     alert('Mnogo'); 
// }else{
//     alert('Әп бәрекелді!');
// }

let isCorrect = (year < 2015) ? "Malo" : 
                (year > 2015) ? "Mnogo":
                                "Әп бәрекелді!";
alert(isCorrect)


let nameOfJS = prompt("What's the “official” name of JavaScript?", "");
if(nameOfJS == "ECMAScript"){
    alert("Right");
}else{
    alert("You don't know? “ECMAScript”!");
}


//2.11
let hour = 12,  isWeekend = true;
if (hour < 10 || hour > 18 || isWeekend) alert( 'The office is closed.' );

let clockHour = 12, clockMinute = 30;
if (hour == 12 && minute == 30) alert( 'The time is 12:30' );

alert( !0 ); // true

let userName = prompt("Who's there?", '');

if(userName === 'Admin') {
  let pass = prompt('Password?', '');
  if (pass === 'TheMaster') alert( 'Welcome!' );
  else if (pass === '' || pass === null) alert( 'Canceled' );
  else alert( 'Wrong password' );

} else if (userName === '' || userName === null) {
  alert( 'Canceled' );
} else {
  alert( "I don't know you" );
}


//2.12

// || returns the first truthy value.
// ?? returns the first defined value.

let height = 0;
alert(height || 100); // 100
alert(height ?? 100); // 0

//2.13
let i = 0;
while (i < 3) { // shows 0, then 1, then 2
  console.log(i);
  i++;
}

let i1 = 0;
do {
  console.log( i );
  i++;
} while (i < 3);


for (let i = 0; i < 3; i++) { // shows 0, then 1, then 2
    console.log(i);
}

//2.14
let num3 = 2 + 2;

switch (num3) {
  case 3:
    alert( 'Too small' );
    break;
  case 4:
    alert( 'Exactly!' );
    break;
  case 5:
    alert( 'Too big' );
    break;
  default:
    alert( "I don't know such values" );
}


//2.15
function showMessage() {
    alert( 'Hello everyone!' );
}

showMessage();
  

function showMessage(from, text = "no text") { 
    alert(from + ': ' + text);
}
  
showMessage('Alima', 'Hello!'); 
showMessage('Alima');



//2.16
function sayHi() {   
    alert( "Hello" );
}
  
let func = sayHi;    //copy
  
func(); // Hello     
sayHi(); // Hello 


let sayHi2 = function(name) {  // (*) no magic any more
    alert( `Hello, ${name}` );
};

sayHi2()

//2.17 Arrow functions
//let func = (arg1, arg2, ..., argN) => expression;

let sum = (a, b) => a + b;

// or multi-line syntax with { ... }, need return here:
let sum2 = (a, b) => {
    // ...
    return a + b;
  }

console.log(sum(2,5));


// function ask(question, yes, no) {
//     if (confirm(question)) yes();
//     else no();
//   }
  
//   ask(
//     "Do you agree?",
//     function() { alert("You agreed."); },
//     function() { alert("You canceled the execution."); }
//   );

function ask(question, yes, no) {
    if (confirm(question)) yes();
    else no();
}

ask(
    "Do you agree?",
    () => alert("You agreed."),
    () => alert("You canceled the execution.")
);


