var ourRequest = new XMLHttpRequest();
ourRequest.open('GET', 'https://learnwebcode.github.io/json-example/pets-data.json');

ourRequest.onload = function() {
  if (ourRequest.status >= 200 && ourRequest.status < 400) {
    // This is where we'll do something with the retrieved data
    var petsData = JSON.parse(ourRequest.responseText);

    createHTML(petsData);

  } else {
    console.log("We connected to the server, but it returned an error.");
  }
};

ourRequest.onerror = function() {
  console.log("Connection error");
};

ourRequest.send();  

Handlebars.registerHelper("calculateAge", function(birthYear) {
  var age = new Date().getFullYear() - birthYear;
  if (age < 1) {
    return "Less than a year old."
  } else{ 
    return age + " years old."
  };
});


function createHTML (data) {
  console.log(data);
  var rawTemplate = document.getElementById("petsTemplate").innerHTML;
  var compiledTemplate = Handlebars.compile(rawTemplate);
  var ourGeneratedHTML = compiledTemplate(data);

  var petsContainer = document.getElementById("pets-container");
  petsContainer.innerHTML = ourGeneratedHTML;
}