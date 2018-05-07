function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
} 

$(document).ready(function(){

	$('img').hover(

		function() {
			$(this).css({"box-shadow":"0px 0px 26px 4px white"});
		},
		function() {
			$(this).css({"box-shadow": "0px 0px 26px 2px #988c8c"});
		}


	);

});