var btn = document.getElementById('btn');

btn.addEventListener('click', function() {
  var ourRequest = new XMLHttpRequest();
  
  ourRequest.open('GET', 'https://learnwebcode.github.io/json-example/animals-1.json')
  ourRequest.onload = function() {
    var our_data = JSON.parse(ourRequest.responseText);
    console.log(our_data[0]);
  };
  ourRequest.send();
  
});
