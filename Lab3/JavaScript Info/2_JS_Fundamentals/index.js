"use strict";
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