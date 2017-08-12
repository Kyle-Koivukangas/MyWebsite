// following this tutorial, will finish tomorrow.. https://www.youtube.com/watch?v=rJesac0_Ftw

var animalContainer = document.getElementById("animal-info");
var btn = document.getElementById('btn');

btn.addEventListener('click', function() {

  console.log("click registered");

  var ourRequest = new XMLHttpRequest();
  ourRequest.open('GET', 'https://learnwebcode.github.io/json-example/animals-1.json');
  ourRequest.onload = function() {
    if (ourRequest.status >= 200 && ourRequest.status <400) {
      var our_data = JSON.parse(ourRequest.responseText);
      console.log(our_data);
      renderHTML(our_data);
    } else {
      console.log("Connected to server, but server returned an error: " + ourRequest.status);
    };
  };
  
  ourRequest.onerror = function() {
    console.log("connection error");
  }
  ourRequest.send();

});

function renderHTML(data) {
  var HTML_string = "";

  for (i = 0; i < data.length; i++) {
    HTML_string += "<p>" + data[i].name + " is a " + data[i].species + ', ' + data[i].name + "'s favourite foods are: ";
    
    for (ii = 0; ii < data[i].foods.likes.length; ii++) {
      if (ii == 0) {
        HTML_string += data[i].foods.likes[ii]; 
      } else {
        HTML_string += ", " + data[i].foods.likes[ii];
      }
           
    }
    HTML_string += '. ' + data[i].name + " doesn't like ";
    for (ii = 0; ii < data[i].foods.dislikes.length; ii++) {
      if (ii == 0) {
        HTML_string += data[i].foods.dislikes[ii]; 
      } else {
        HTML_string += " or " + data[i].foods.dislikes[ii];
      }
           
    } 

    HTML_string += ".</p>";
  };
  animalContainer.insertAdjacentHTML('beforeend', HTML_string);

};
