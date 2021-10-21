let sentence = "The movie is not that bad, I like it";
let wordNot = "not";
let wordBad = "bad";

if (sentence.indexOf(wordNot) < sentence.indexOf(wordBad)) {
    let a = sentence.substr(sentence.indexOf(wordNot),sentence.indexOf(wordBad)+1);
    let b = sentence.replace(a,"good");
    console.log(b);
}
else {
    console.log(sentence);
}
