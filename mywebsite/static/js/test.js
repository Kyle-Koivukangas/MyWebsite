// following this tutorial, will finish tomorrow.. https://www.youtube.com/watch?v=rJesac0_Ftw

var animalContainer = document.getElementById("animal-info");
var btn = document.getElementById('btn');

btn.addEventListener('click', function() {

  console.log("click registered");

  var ourRequest = new XMLHttpRequest();
  ourRequest.open('GET', 'https://learnwebcode.github.io/json-example/animals-1.json');
  ourRequest.onload = function() {
    var our_data = JSON.parse(ourRequest.responseText);
    console.log(our_data);
    renderHTML(our_data);
  };
  ourRequest.send();

});

function renderHTML(data) {
  var HTML_string = "";

  for (i = 0; i < data.length; i++) {
    HTML_string += "<p>" + data[i].name + "is a" + data[i].species + ".</p>";
  };
  animalContainer.insertAdjacentHTML('beforeend', HTML_string);

};
