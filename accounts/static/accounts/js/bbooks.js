$(document).ready(function () {
        var pathArray = window.location.pathname.split('/');
        var active = pathArray[3];

        // set class = active where id = category_active
        $('#category_' + active).addClass('active');


});

function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}