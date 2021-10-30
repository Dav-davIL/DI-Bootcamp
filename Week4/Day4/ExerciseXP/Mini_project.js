let wordPlayer1 = ''
let intermediateWord = '';
let letter = '';
let times = 0;
let array = [];
let errorArray = [];


wordPlayer1 = prompt("Please enter a word (minimum 8 letters) ");
wordPlayer1 = wordPlayer1.toLowerCase();
array = wordPlayer1.split("");

if (wordPlayer1.length >= 8)
{
	intermediateWord = ("*").repeat(wordPlayer1.length);
	console.log(intermediateWord);
}
else
{
	wordPlayer1 = prompt("Please enter a word (minimum 8 letters) ");
}

window.alert("Please, find the word!");
let intermediateWordArray = intermediateWord.split("");


do
{

	letter = prompt("Please, enter a letter");
	var success = false;
	for (let x=0; x<array.length;x++)
	{
		
		if (letter == array[x])
		{
			intermediateWordArray[x] = letter;
			success = true;

		}
	}
	if (!(success))
	{
		errorArray.push(letter);
	}
	
	index = intermediateWordArray.indexOf('*');
	if (index == -1)
	{
		alert("CONGRATS YOU WIN");
		success = true;
		times = 12;
	}
	else 
	{
		alert(intermediateWordArray.join("") +'\n' + errorArray);
	}

	times++
} while(times < 10);

if (success == false)
{
	alert("YOU LOSE");
}




