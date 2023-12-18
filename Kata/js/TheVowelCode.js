//https://www.codewars.com/kata/53697be005f803751e0015aa/train/javascript
//My solution

let vowels = ['a','e','i','o','u']
function validateVowel(a){
	if (vowels.includes(a) || Number.isInteger(parseInt(a))) return true;
	return false;
}
function changeVowel(str){
	return Number.isInteger(parseInt(str)) ? vowels[parseInt(str) -1] : vowels.indexOf(str) +1
}

function encode(str){
	let string = str.split('');
	for (var i = 0 ; i < string.length; i++) {
		string[i] = validateVowel(string[i].toLowerCase())?changeVowel(string[i].toLowerCase()):string[i]
	}
	return string.toString().replace(/,/gi, "");
}
function decode(str){
	let string = str.split('');
	for (var i = 0 ; i < string.length; i++) {
		string[i] = Number.isInteger(parseInt(string[i])) && parseInt(string[i]) <6 ? vowels[parseInt(string[i]) -1]:string[i]
	}
	return string.toString().replace(/,/gi, "");
}


//Best solution
// turn vowels into numbers
function encode(string){
		return string.replace(/[aeiou]/g, function (x) { return '_aeiou'.indexOf(x) });
}

//turn numbers back into vowels
function decode(string){
  return string.replace(/[1-5]/g, function (x) { return '_aeiou'.charAt(x) });
}
