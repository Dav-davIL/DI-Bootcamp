let intermediate = '';
let array = [];
let result = 0;

function number(num)
{
	num = num.toString();
	if (isNaN(intermediate))
	{
		intermediate = num;
		document.getElementById('result').innerHTML = num;
	}
	else
	{
		intermediate += num;
		document.getElementById('result').innerHTML = intermediate;
	}
}

function operator(operator)
{
	array.push(intermediate);	
	intermediate = "";
	if (operator == '+')
	{
		array.push(operator);
	}
	else if (operator == '-')
	{
		array.push(operator);
	}
	else if (operator == '*')
	{
		array.push(operator);
	}
	else
	{
		array.push(operator);
	}
}


function equal()
{
	array.push(intermediate);
	if (array.length == 0)
	{
		document.getElementById('result').innerHTML = result;
	}
	else
	{
		for (var a = 0; a < array.length; a++)
		{
		  if (a == 0) {
		    result = parseInt(array[a]);
		  } else {
		    if (!isNaN(array[a])) {
		      switch (array[a - 1]) {
		        case "-":
		          result -= parseInt(array[a]);
		          break;
		        case "+":
		          result += parseInt(array[a]);
		          break;
		        case "*":
		          result *= parseInt(array[a]);
		          break;
		        case "/":
		          result /= parseInt(array[a]);
		          break;
		      }
		    }
		  }
		}
		document.getElementById('result').innerHTML = result;
		
	}
}

function reset()
{
	array = [];
	document.getElementById('result').innerHTML = '';
}

function clear()
{
	array.pop();
	if (isNaN(array.length-1))
	{
		document.getElementById('result').innerHTML = array[array.length-1];
	}
	else
	{
		document.getElementById('result').innerHTML = array[array.length-2];
	}
	
}