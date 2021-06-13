"use strict"
// типы данных

/*
десятичный – целое число (например, 0, 5, -10, -100, 56);
приближенные к вещественным – приблизительные вещественные числа (например, 6.7, 8.54, -10.34);
экспоненциальный (научный) – с использованием буквы ‘e’ (например, 10 = 1e1, 20 = 2e1, 25000 = 25e3, 8700 = 8.7e3);
восьмиричная: 0o777;
шестнадцатиричная: 0xff24f.
*/

let msg_1 = "message"
let msg_2 = 'message'
let msg_3 = `message`

console.log(msg_1);
console.log(msg_2);
console.log(msg_3);


let aa = 3;
let msg3 = `Значение a = ${aa+1+2}`;
console.log(msg3);

let msg1 = 'строка "привет" ';
console.log(msg1);
msg1 = "строка \"привет\"";
console.log(msg1);
msg1 = "строка \\";
console.log(msg1);


let tp = typeof msg_1;

console.log(tp);

tp = typeof(msg_1);

console.log(tp);

let c = 1/0;
console.log(c);

let d = Infinity;
console.log(d);

let e = -Infinity;
console.log(e);

let f = NaN;
console.log(f);



let isWin = true, isCheckedField = false;
console.log(isWin);

console.log(isCheckedField);

let isGreater = 4 > 1;
console.log(isGreater);

let idProcess = null;
console.log(idProcess);

let arg;
console.log(arg);


let a = undefined;
console.log(a);
