function startFib() {
    var f;
    var n = document.getElementById("n").value;
    if(typeof(Worker) !== "undefined") {
      f = new Worker("fibonacci.js");
      f.postMessage(n);
      f.onmessage = function(event) {
      document.getElementById("result").innerHTML = event.data;
    };
  } 
 }
 // Silnia
 function startSilnia() {
   var silnia;
   var s = document.getElementById("s").value;
   if (typeof(Worker) !== "undefined") {
       silnia = new Worker("silnia.js");
       silnia.postMessage(s);
       silnia.onmessage = function(event) {
       document.getElementById("resultsilnia").innerHTML = event.data;
       };
   } 
 }