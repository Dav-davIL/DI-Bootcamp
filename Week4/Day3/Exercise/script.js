let iteration = 0;
let result = 0;
function playTheGame()
{
    let userResponse = confirm("Do you want to play?");
    if (userResponse == false)
    {
        return alert("No problem, Goodbye");
    }
    else
    {
        UserNumber = parseInt(prompt("Please enter a number between 0 and 10"));
        let computerNumber;
        if (isNaN(UserNumber))
        {
            return alert("Sorry Not a number, Goodbye");
            
        }
        else if (UserNumber < 0 || UserNumber >10 )
        {
            return alert("Sorry it’s not a good number, Goodbye");
        }
        else 
        {
            computerNumber = Math.floor(Math.random() * 11);
            while (iteration < 3)
            {
                test(UserNumber, computerNumber);
                iteration++;
                if (result == 0)
                {
                    UserNumber = parseInt(prompt("Please enter a number between 0 and 10"));
                }
                else 
                {
                    iteration = 10;
                }
                
                
            }
            if (iteration >= 3 && iteration < 10)
            {
                return alert("out of chances");
            }
                    
            
            
        }
    }
}

function test(userNumber,computerNumber)
{
    if (userNumber === computerNumber)
    {
        alert("WINNER");
        result = 1;
        return result;
    }
    else if (userNumber > computerNumber)
    {
        alert("Your number is bigger then the computer’s, guess again");
        result = 0;
        return result;
    }
    else 
    {
        alert("Your number is smaller then the computer’s, guess again");
        result = 0;
        return result;
    }
}