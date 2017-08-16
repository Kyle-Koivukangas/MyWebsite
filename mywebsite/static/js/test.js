
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
        console.log(`New JSON file: `);
        console.log(json);
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
                //console.log("AJAX request Complete.");
            }
        });
    })();



    //Public Method
    projects.btn = function(page) {

        var screenWidth = $(window).width();
        if (isOnIndex === true && screenWidth < 1500) {
            fadeOutAnimation = "animated fadeOutLeftBig";
            fadeInAnimation = "animated fadeInRightBig";

        } else if (isOnIndex === true && screenWidth >= 1500) {
            fadeOutAnimation = "animated fadeOutUpBig";
            fadeInAnimation = "animated fadeInUpBig";

        } else if (isOnIndex === false && screenWidth < 1500) {
            fadeOutAnimation = "animated fadeOutRightBig";
            fadeInAnimation = "animated fadeInLeftBig";

        } else if (isOnIndex === false && screenWidth >= 1500) {
            fadeOutAnimation = "animated fadeOutDownBig";
            fadeInAnimation = "animated fadeInDownBig";   
        }


        $(contentDiv).addClass(fadeOutAnimation).one(animationEnd, function() {
            $(contentDiv).removeClass(fadeOutAnimation);

            //insert new HTML from json
            $(contentDiv).html(json.message[page]);

            $(contentDiv).addClass(fadeInAnimation).one(animationEnd, function() {
                $(contentDiv).removeClass(fadeInAnimation);
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
