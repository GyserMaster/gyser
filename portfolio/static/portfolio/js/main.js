'use strict';
// $ o JQuery es exactamente el mismo objeto
var it = document.getElementById("services-it");

var projects = document.getElementById("services-projects");

window.addEventListener("load", function(){
    //DOCUMENT OBJECT MODEL
    var it = $("#services-it");
    var webdev = $("#services-webdev");
    var projects = $("#services-projects");

    webdev.hide();
    projects.hide();

    var navit = $("#services-nav-it");
    var navwebdev = $("#services-nav-webdev");
    var navprojects = $("#services-nav-projects");

    navit.click(function (e){
        $(this).addClass("active");
        $(navwebdev).removeClass("active");
        $(navprojects).removeClass("active");

        webdev.hide();
        projects.hide();
        $(it).slideToggle("low");
        
    });
    navwebdev.click(function (e){
        $(this).addClass("active");
        $(navit).removeClass("active");
        $(navprojects).removeClass("active");

        it.hide();
        projects.hide();
        $(webdev).slideToggle("low");
    });
    navprojects.click(function (e){
        $(this).addClass("active");
        $(navwebdev).removeClass("active");
        $(navit).removeClass("active");

        it.hide();
        webdev.hide();
        $(projects).slideToggle("low");
    });
    

});