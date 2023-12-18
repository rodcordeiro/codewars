//https://www.codewars.com/kata/546f922b54af40e1e90001da/train/javascript/5ef1146f710b30002350d468

const alphabet = ['a','b','c', 'd','e','f','g','h', 'i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
function alphabetPosition(text) {
    if (text.length <= 0) return '';
    return text.replace(/\W|_|\d/g,'').toLowerCase().split('').map(letter=>{
        return alphabet.indexOf(letter) + 1
    }).join(' ')    
}



console.log(alphabetPosition("The sunset sets at twelve o' clock."), "\n20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11");
console.log(alphabetPosition("The narwhal bacons at midnight."), "\n20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20");
console.log(alphabetPosition("}o.@# x2"))
console.log(alphabetPosition("6*,|-_l9"))

