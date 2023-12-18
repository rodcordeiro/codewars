// https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/javascript

// :: NOT COMPLETED ::

function bouncingBall(h,  bounce,  window) {
    var rebounds = -1;
    if (bounce > 0 && bounce < 1) while (h > window) rebounds+=2, h *= bounce;
    return rebounds;
}

console.log(bouncingBall(3.0, 0.66, 1.5), 3)
console.log(bouncingBall(30.0, 0.66, 1.5), 15)
console.log(bouncingBall(2,0.5,1),1)
console.log(bouncingBall(30,0.75,1.5),21)
console.log(bouncingBall(30,0.4,10),3)
console.log(bouncingBall(40,0.4,10),3)
console.log(bouncingBall(10,0.6,10),-1)
console.log(bouncingBall(-5,0.66,1.5),-1)

