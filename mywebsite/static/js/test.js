
(function( projects, $, undefined ) {
    // Access the public variables/methods in this namespace as if it was a class named 'projects'.
    // EG: projects.btn()  to access the btn method.

    //Private Properties
    var contentDiv = "#projects-content";
    var fadeOutAnimation = "animated fadeOutLeftBig";
    var fadeInAnimation = "animated fadeInRightBig";
    var animationEnd = "webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend";
    var json = {};
    var isOnIndex = true;

    function saveJSON(jsonFile) {
        json = jsonFile;
    };

    //private method
    (function backgroundLoad() {
        console.log("making AJAX request..")
        $.ajax({
            type: "GET",
            url: "http://localhost:6543/projects/projectsjson",
            dataType: "JSON",
            async: true,
            data: {},
            success: function(json) {
                saveJSON(JSON.parse(json));
                //projects.json = JSON.parse(json);
                console.log("AJAX request Complete: ");
                console.log(projects.json);
            }
        });
    })();



    //Public Method
    projects.btn = function(page) {
        if (isOnIndex === true) {
            fadeOutAnimation = "animated fadeOutLeftBig";
            fadeInAnimation = "animated fadeInRightBig";
        } else if (isOnIndex === false) {
            fadeOutAnimation = "animated fadeOutRightBig";
            fadeInAnimation = "animated fadeInLeftBig";
        } else {
            fadeOutAnimation = "animated fadeOut";
            fadeInAnimation = "animated fadeIn";   
        }


        console.log("button pressed");
        $(contentDiv).addClass(fadeOutAnimation).one(animationEnd, function() {
            console.log("Fade OUT Class ADDED <---");
            //fade out animation removal (after animation completes)
            $(contentDiv).removeClass(fadeOutAnimation);
            console.log("Fade OUT Class REMOVED...");

            //insert new HTML
            $(contentDiv).html(json.message[page]);
            console.log("New page loaded ----------------------------------------------");

            //fade in animation on new HTML
            $(contentDiv).addClass(fadeInAnimation).one(animationEnd, function() {
                console.log("Fade IN Class ADDED --->");
                //fade in animation removal (after animation completes)
                $(contentDiv).removeClass(fadeInAnimation);
                console.log("Fade IN Class REMOVED.....");
            })
        });

        if (page === 'index') {
            isOnIndex = true;
            console.log("page switched to INDEX");
        } else {
            isOnIndex = false;
            console.log(`page switched to ${page}`)
        }
    };


}( window.projects = window.projects || {}, jQuery ));
