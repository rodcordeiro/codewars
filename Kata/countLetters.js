// https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/javascript

function count (string) {  
  let str = string.split('')
  let response = {}
  for (var i = 0; i < str.length; i++) {
  	if(response[str[i]]) {response[str[i]]=  response[str[i]] +1}
  	else{
  		response[str[i]] = 1
  	}

  }
  return response
}
