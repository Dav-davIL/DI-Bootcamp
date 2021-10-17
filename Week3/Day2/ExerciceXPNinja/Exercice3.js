let sentence = window.prompt("Please enter 2 numbers separate by coma: ");
let myArray = sentence.split(',');

let result = Number(myArray[0])+Number(myArray[1]);
console.log(result);