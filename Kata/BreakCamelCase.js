// https://www.codewars.com/kata/5208f99aee097e6552000148/train/javascript

// complete the function
function solution(string) {
    let text = ''
    for (let i = 0; i < string.length; i++){
        text += string[i].search(/[A-Z]/g) == 0 ? ` ${string[i]}` : string[i]
    }
    return text;
}

console.log(solution('camelCasing'), 'camel Casing')
console.log(solution('camelCasingTest'), 'camel Casing Test')
