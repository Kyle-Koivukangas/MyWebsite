
console.log("js loaded");

$(document).ready(function() { 
// this will get the full URL at the address bar and slice off the last element or two, depending on how many there are
var path = window.location.href.split("/").splice(3,4);

//checks incase path is clean (no sub directories, fresh homepage) or it has multple parts
if (path == '') {
    path = 'index';
}
if (path.length > 1) {
    path = path.join("/");
}
console.log(path);

//target the navbar link that's the same as the path and add 'active' class to it to highlight it.
var target = $('nav a[href="/'+path+'"]');
$(target.addClass('active'));

});