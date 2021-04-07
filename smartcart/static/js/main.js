$(document).ready(function(){
  $('.owl-carousel').owlCarousel({
    loop: true,
    margin:0,
    items:1,
    autoPlay:true,
    singleItem:true,
    nav:true,
    navText: [
        "<i class='fa fa-caret-left'></i>",
        "<i class='fa fa-caret-right'></i>"
    ],
    dots:true
  });
});