var obj = document.getElementById('id_div');
console.log(obj);
console.log('-------------')

var a = 5;
console.log('a', a);

function f(){
  console.log('f() a', a);
  if(a){
    console.log(a);
    var a = 10;
  }
}

f(a);
