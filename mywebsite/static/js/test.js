
function projectBtn(project) {
    var animationName = "animated fadeOutLeft";
    var animationEnd = "webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend";

    console.log(this);
    $('.project-item').addClass("animated fadeOutLeftBig").one(animationEnd, function() {
        loadPage(project);
    });
    
}

function loadPage(project) {
    console.log("http://localhost:6543/projects/".concat(project));
    $.ajax({
        type: "GET",
        url: "http://localhost:6543/projects/".concat(project),
        dataType: "json",
        async: true,
        data: {},
        success: function (json) {
            json = JSON.parse(json)
            $('.projects').html(json.message);
            console.log(json);
            console.log(json.message);  
        }
    });
}
