//https://www.codewars.com/kata/523f5d21c841566fde000009/train/javascript

let a =[]
let b = [3]
function arrayDiff(a, b) {
  let dif = []
  for (var i = 0; i < a.length; i++) {
  	if (b.indexOf(a[i]) == -1) dif.push(a[i]);
  }
 return dif
}        


//BEST
function array_diff(a, b) {
  return a.filter(e => !b.includes(e));
}