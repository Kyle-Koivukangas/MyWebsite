
// var projectsJSON = {}
// backgroundLoad()

// function backgroundLoad() {
//     console.log("making AJAX request..")
//     $.ajax({
//         type: "GET",
//         url: "http://localhost:6543/projects/projectsjson",
//         dataType: "JSON",
//         async: true,
//         data: {},
//         success: function (json) {
//             projectsJSON = JSON.parse(json);
//             console.log(projectsJSON);
//             console.log("backgroundLoad finished");
//         }
//     });
// }

// function projectBtn(project) {
//     var animationOutName = "animated fadeOutLeftBig";
//     var animationEnd = "webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend";

//     $('#projects-content').addClass(animationOutName).one(animationEnd, function() {
//         $('#projects-content').removeClass(animationOutName);
//         loadPage(project);
//     });
// }

// function loadPage(project) {
//     console.log(`load page: ${project}`)
//     $('#projects-content').html(projectsJSON.message[project]);
// }

// function backBtn() {
//     var animationOutName = "animated fadeOutRightBig";
//     var animationInName = "animated fadeInLeftBig";
//     var animationEnd = "webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend";

//     $('#projects-content').addClass(animationOutName).one(animationEnd, function() {
//         console.log("Back AnimationEnd")
//         loadPage('index');
//         $('#projects-content').addClass(animationInName).one(animationEnd, function() {
//             $('#projects-content').removeClass(animationInName)
//         });
//     });
// }

class ProjectsClass{
    constructor(contentDiv){
        this.contentDiv = contentDiv;
        this.fadeOutAnimation = "animated fadeOutLeftBig";
        this.fadeInAnimation = "animated fadeInRightBig";
        this.animationEnd = "webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend";
        this.projectsJSON = null;
        this.backgroundLoad();
    }

    ajaxCallBack(json) {
        this.projectsJSON = json;
        console.log("backgroundLoad finished");                
        console.log(this.projectsJSON);
    }

    backgroundLoad() {
        console.log("making AJAX request..")
        var self = this;
        $.ajax({
            type: "GET",
            url: "http://localhost:6543/projects/projectsjson",
            dataType: "JSON",
            async: true,
            data: {},
            success: function(json) {
                self.ajaxCallBack(JSON.parse(json));
                // this.projectsJSON = JSON.parse(json);
            }
        });
    }



    btn(page) {
        var self = this;
        console.log("Button Pressed");
        // Fade out animation
        $(self.contentDiv).addClass(self.fadeOutAnimation).one(self.animationEnd, function() {
            console.log("Fade OUT Class ADDED <---");
            //fade out animation removal (after animation completes)
            $(self.contentDiv).removeClass(self.fadeOutAnimation);
            console.log("Fade OUT Class REMOVED...");

            //insert new HTML
            $(self.contentDiv).html(self.projectsJSON.message[page]);
            console.log("New page loaded ----------------------------------------------");

            //fade in animation on new HTML
            $(self.contentDiv).addClass(self.fadeInAnimation).one(self.animationEnd, function() {
                console.log("Fade IN Class ADDED --->");
                //fade in animation removal (after animation completes)
                $(self.contentDiv).removeClass(self.fadeInAnimation);
                console.log("Fade IN Class REMOVED.....");
            })
        });
    }
    

    fadeOut() {
        var self = this;
        console.log("fadeOut Add <---");        
        $(self.contentDiv).addClass(self.fadeOutAnimation).one(self.animationEnd, function() {
            console.log("fadeOut Remove <---");   
            $(self.contentDiv).removeClass(self.fadeOutAnimation)
            console.log("fadeOut DONE <---");
        });
    }

    fadeIn() {
        var self = this;
        console.log("fadeInAdd --->");        
        $(self.contentDiv).addClass(self.fadeInAnimation).one(self.animationEnd, function() {
            console.log("fadeInRemove --->");
            $(self.contentDiv).removeClass(self.fadeInAnimation)
            console.log("fadeIn DONE --->");        
        });
    }

    loadPage(page, callback = null) {
        console.log(`projects class, load page: ${page}`);
        //console.log(this.projectsJSON.message[page]);
        $(this.contentDiv).html(this.projectsJSON.message[page]);
        console.log(`load Page (${page})   DONE ----------------------------`);
        console.log(callback);
        callback();
    }
}


let p = new ProjectsClass('#projects-content');

// console.log("projects class instantiated, JSON:")
// console.log(p.projectsJSON);


// function projectBtn(page) {
//     console.log(p.projectsJSON);
//     p.fadeOut();
//     p.loadPage(page);
//     p.fadeIn();
// }

