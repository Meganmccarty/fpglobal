$(document).ready(function(){
    $(".nav .nav-link").on("click", function(){
        $(".nav").find(".active").removeClass("active");
        $(this).addClass("active");
    });
    $('#parallax_image_first').parallax("50%", 0.3);
    $('#parallax_image_second').parallax("50%", 0.3);
    $('#parallax_image_third').parallax("50%", 0.3);
});