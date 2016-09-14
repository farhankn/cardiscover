$(document).ready(function(){
  $(window).scroll(function() { // check if scroll event happened
    if ($(document).scrollTop() > 100) { // check if user scrolled more than 50 from top of the browser window
      $(".navbar").css("background", "#141212");
      $(".navbar").addClass("boxshadowout");
      // if yes, then change the color of class "navbar-fixed-top" to white (#f8f8f8)
    } else {
      $(".navbar").css("background", "transparent");
      $(".navbar").removeClass("boxshadowout");
      // if not, change it back to transparent
    }
  });
});
