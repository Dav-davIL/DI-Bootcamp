

function click() {

    let myList = [];
    let noun = document.getElementById("noun").value;
    let adjective = document.getElementById("adjective").value;
    let person = document.getElementById("person").value;
    let verb = document.getElementById("verb").value;
    let place = document.getElementById("place").value;

    myList.push(noun);
    myList.push(adjective);
    myList.push(person);
    myList.push(verb);
    myList.push(place);
    for (let i=0; i<myList.length;i++) {
        if (myList[i] == '') {
            return console.warn("Please enter all the fields");
        }
    }  
    text = myList[2] + ' ' + myList[1] + ' ' + myList[0] + ' ' + myList[3] + ' ' + myList[4];

    let p = document.querySelector("p");
    let id = document.getElementById("story");
    id.appendChild(document.createTextNode(text));
    p.appendChild(id);

    
}

let button = document.querySelector("button");
button.addEventListener("click", click);