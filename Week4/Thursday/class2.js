


// function area(width, height) {
//   return width * height;
// };


// function area(h, w){
//     h = h +  1;
//     console.log(h)
//     return height * width;
// }

// var height =3;

// var width = 4;

// area(height, width);
// console.log(height)


// function pushArray(newArray){

//     newArray.push(6);

//     console.log(newArray);
//     return newArray

// }

// var myArray = [1, 3 ,4, 5];

// pushArray(myArray);

// console.log(myArray)

// function myTest(){

//     var a = 4;
//     var b = 3;
//     console.log(a);
    
//     return a* b;
// }

// console.log(myTest());
// console.log(a)

// var x = 1;

// if (x === 1) {

//   let x = 2;
//   console.log(x);
//   // expected output: 2
// }
// console.log(x);

// const pi = 3.14;

// console.log(pi);

// pi = 2;

// function varTest() {
//     var x = 1;
//     if (x===1) {
//       var x = 2;  // same variable!
//       console.log(x);  // 2
//     }
//     console.log(x);  // 2
//   }

//   varTest()
//   function letTest() {
//     let x = 1;
//     if (x === 1) {
//       let x = 2;  // different variable
//       console.log(x);  // 2
//     }
//     console.log(x);  // 1
//   }


// var x = 'global';
// let y = 'global';


// console.log(window.x); // "global"
// console.log(this.y); // undefined



// if (true) {
//     var x = 2;  // different variable
//     console.log(x);  // 2
// }
// console.log(x);  // 1

// function m(){
//     var x = 2;

// }

// m();
// console.log(x)

// var greet = function (name){
//     return 'hello ' + name;
// }

// console.log(greeting('Shoba'))

// console.log(greet('Eric'))

// var add = function(num1, num2){

//     return num1 + num2;
// }

// var subtract = function(num1, num2){

//     return num1 - num2;
// }

// var calc = function(num1, num2, operation){

//     return operation(num1, num2)
// }

// console.log(calc(3, 4, subtract))


// var arr = [4, 7, 2, 3, 9, 0];

// var result = arr.some(function(value){
    
//     console.log(value);
//     return value < 0;
// })
// console.log(result)
// var newArray = arr.filter(function(value){

//     return value > 3
// })

// console.log(newArray)

// var newArray = arr.map(function(value){

//     return value * 2

// })

// console.log(newArray)
// console.log(arr)
// arr.forEach(function(value, index){
//     console.log(value + " " + index);
// })

// for (var i = 0; i< arr.length; i++){
//     console.log(arr[i] + " " + i);
// }


// var arr = ['very', 'important', 'person'];

// var p = arr.reduce(function(x,y){

//     return x + y[0];
// }, '')

// console.log(p)


var p = ['very', 'important', 'person'];
var q = ['national', 'aeronautics', 'space', 'administration'];

function acronymn(arr){
    var p = arr.reduce(function(accumulator, currentValue){
        return (accumulator + currentValue[0]).toUpperCase()
    },"");

    return p;
}

console.log(acronymn(p))
console.log(acronymn(q))









