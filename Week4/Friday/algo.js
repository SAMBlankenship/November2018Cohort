
// var myString = "DigitalCrafts";

// var myArray = myString.split('');

// var reveserd = myArray.reverse();

// var rs = reveserd.join('');
// console.log(rs);


// function reverse(str){

//     let reverse = '';

//     for(let char of str){

//         reverse = char + reverse;
//     }

//     return reverse;
// }



// console.log(reverse('hello'))

// function palindrone(str){

//     let newString = str.split('');

    
//     if(newString.reverse().join('') === str){
//         return true;
//     }
//     else{
//         return false;
//     }

// }

// console.log(palindrone('eve'));

// var i = -34;

// var i_s = i.toString();

// var newS = i_s.split('').reverse().join();

// console.log(newS);


// let myNumber = -848549;
// let myNumber1 = -50000;
// function reverseString(n){

//     const reversed = n.toString().split('').reverse().join('');
//     console.log(Math.sign(n))
//     return parseInt(reversed) * Math.sign(n);
// }
// console.log(reverseString(myNumber))

const myString =  "Digital Crafts"; 
const myCharMap = {};
let max = 0;
let maxChar = '';


for(let char of myString){
    if(!myCharMap[char]){
        myCharMap[char] = 1;
    }
    else{
        myCharMap[char]++;
    }
}

console.log(myCharMap);


for(let key in myCharMap){
    if(myCharMap[key] > max){

        max  = myCharMap[key];
        maxChar = key;
    }
}

var myArray = [];
for(let key in myCharMap){
    if(myCharMap[key] === max){

        myArray.push(key);
    }
}

console.log(myArray);



