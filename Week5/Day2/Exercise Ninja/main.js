let id_totalTip = document.getElementById("totalTip");
id_totalTip.style.display = "none";

function calculateTip() {
    // Create a variable called billAmount that fetches the value of the input, which id is billAmt
    let billAmount = document.getElementById("billamt").value;

    // Create a variable called serviceQuality that fetches the value of the input, which id is serviceQual
    let serviceQuality  = document.getElementById("serviceQual").value;

    // Create a variable called numberOfPeople that fetches the value of the input, which id is numOfPeople
    let numberOfPeople = document.getElementById("peopleamt").value;

    let allP = document.querySelectorAll("p");
    let p = allP[allP.length - 1];
    if (serviceQuality == 0 || billAmount == '') {
        return alert("Please enter a service quality and a bill");
        
    }
    else if (numberOfPeople == '' || numberOfPeople < 1) {
        numberOfPeople = 1;
        document.getElementById("peopleamt").value = 1;
        let tag_each = document.getElementById("each");
        tag_each.style.display = "none";
    }
    let total = ( billAmount * serviceQuality ) / numberOfPeople;
    total = total.toFixed(2);

    // Add the CSS property “display:block” to the tag which id is totalTip
    let id_tip = document.getElementById("tip");
    id_tip.style.display = "block";

    // Display the variable total in the tag which id is tip.
    id_totalTip.style.display = "block";
    let sup = document.querySelector("sup");
    sup.appendChild(document.createTextNode(total))
}

let button = document.querySelector("button");
button.addEventListener("click", calculateTip);
