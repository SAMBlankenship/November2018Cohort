// function lvl5exercise2() {
//     // Remove the last element from the array and return it
//     var arr = [1, 'adam']

//     var val = arr.pop();
//     // console.log(val);
//     return arr
// }

// console.log(lvl5exercise2())

// function lvl5exercise4 () {
//     // Return the index of "adam" in the array
//     var arr = [1, 'adam']

//     return arr.indexOf('adam')
//   }

// console.log(lvl5exercise4 ())


// function lvl6exercise1 (num) {
    // Return 'hello' if num is 1, 'world' if num is 2, otherwise return 'bye'

    // if(num == 1){
    //     return 'hello'
    // }
    // else if(num == 2){
    //     return 'world'
    // }
    // else{
    //     return 'bye'
    // }

//     var x;
//     switch(num){
//         case 1:
//             x = 'hello';
//             break; 
//         case 2:
//             x = 'world';
//             break;
//         default:
//             x = 'bye';
//             break; 

//     }

//     return x;



// }

// console.log(lvl6exercise1(1))
// console.log(lvl6exercise1(2))
// console.log(lvl6exercise1(3))

// var myString = "hello world";

// console.log(myString.length);

// function lvl6exercise2 () {
    // Push 10 'hello' strings into the array using a for loop, then return it
    var arr = []

    // while( arr.length < 10){

    //     arr.push('hello');
    //     //console.log(arr);
    // }

    

    // return arr;
// }

// console.log(lvl6exercise2());


// function lvl6exercise3 () {
//     // Empty this array using a while loop and return it
//     var arr = ['hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello']

//     for(var i = 0; i< arr.length; i++){
//         arr.pop();
//     }

//     return arr;
// }

// console.log(lvl6exercise3())

// Write a function that takes a number as an input.
// Have it create an empty array and then push a string into the array as many
// times as the input number
//
// Name the function "finalFunction"

function exercise(num, string){

    var arr =[]

    for(var i = 0; i< num; i++){
        arr.push(string);
    }
    return arr;
}

var result = exercise(5, "hello");
console.log(result);

