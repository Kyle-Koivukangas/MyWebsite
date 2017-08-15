
var projectsJSON = {}
backgroundLoad()

function backgroundLoad() {
    console.log("making AJAX request..")
    $.ajax({
        type: "GET",
        url: "http://localhost:6543/projects/projectsjson",
        dataType: "JSON",
        async: true,
        data: {},
        success: function (json) {
            projectsJSON = JSON.parse(json);
            console.log(projectsJSON);
            console.log("backgroundLoad finished");
        }
    });
}

function projectBtn(project) {
    var animationName = "animated fadeOutLeft";
    var animationEnd = "webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend";

    console.log(this);
    $('.project-item').addClass("animated fadeOutLeftBig").one(animationEnd, function() {
        loadPage(project);
    });
    
}

function loadPage(project) {
    console.log(projectsJSON.message[project])
    $('.projects').html(projectsJSON.message[project]);
}
