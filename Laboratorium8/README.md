# Lab 8 - Czat z użyciem Web Socket + Web Workers

Socket.io to biblioteka JavaScript dla aplikacji webowych.
Pozwala na komunikację w czasie rzeczywistym między serwerem i klientami.

# npm install express@4

# Express framework webowy JS działający w środowisku Node.js, zawiera metody tworzenia aplikacji webowych oraz proces ich instalacji i uruchomienia

# Przekazanie wiadomości użytkoownika do serwera

```javascript
<script>
      var socket = io();

      var messages = document.getElementById('messages');
      var form = document.getElementById('form');
      var input = document.getElementById('input');

      form.addEventListener('submit', function(e) {
        e.preventDefault();
        if (input.value) {
          socket.emit('chat message', input.value);
          input.value = '';
        }
      });

      socket.on('chat message', function(msg) {
        var item = document.createElement('li');
        item.textContent = msg;
        messages.appendChild(item);
        window.scrollTo(0, document.body.scrollHeight);
      });
    </script>
```

# io.emit() przekazuje wiadomość do reszty użytkowników

```javascript
io.on('connection', (socket) => {
  socket.on('chat message', msg => {
    io.emit('chat message', msg);
  });
});
```

# Dzaiłanie chatu

![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium8/ss/pierwszy.PNG)

![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium8/ss/drugi.PNG)

![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium8/ss/trzeci.PNG)

![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium8/ss/czwarty.PNG)

# Web Workers

WebWorkers pozwalają na wykonywanie skryptów JavaScript w tle, równoległe do głównego wątku.
Dzięki temu nie obciążają głównego interfejsu użytkownika i przyśpiesza działanie strony.

Przy pracy z workerami nie da się ich użyć po prostu włączając plik html.

Należy utwożyc serwer za pomocą polecenia `python -m http.server`

Użytkownik wprowadza liczbę po czym nastepuje sprawdzenie czy są obsługiwane Workery

Tworzony jest Worker, który wykona plik fibonacci.js i silnia.js. Za pomocą metody postMessage() zostaje przesłana liczba do Workera.

Po przesłaniu wyniku przez funkcję z fibonacci.js i silnia.js, następuje obsługa zdarzenia message za pomocą onmessage(). 


```javascript
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
```

# Działanie:

![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium8/ss/webworkers.PNG)




