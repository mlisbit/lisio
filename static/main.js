var height_over = "17px";
var height_leave = "0px";

var top_over = "0px";
var top_leave = "15px";

var icon_map = {
    '.fa-github-alt': 'github',
    '.fa-linkedin': 'linkedin',
    '.fa-twitter': 'twitter',
    '.fa-envelope-o': 'maciej@lis.io'
}

//console.log(icon_map[".fa-envelope-o"])
$.each(icon_map, function(key, value) {
    $(key).mouseover(function() {
        $('.seperator h5').text(value)
        $('.seperator').stop().animate({height: height_over}, 100);
        $('.seperator h5').stop().animate({marginTop: top_over}, 100);
    });
    $(key).mouseleave(function() {
        $('.seperator').stop().animate({height: height_leave}, 100);
        $('.seperator h5').stop().animate({marginTop: top_leave}, 100);
    })
})


