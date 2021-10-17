let sentence = window.prompt("Give a sentence containing the world 'Nemo': ");
let myArray = sentence.split(' ');
let index = myArray.indexOf("Nemo");

if (index != -1) {
    console.log("I found Nemo at", index);
}
else {
    console.log("I can’t find Nemo");
}



