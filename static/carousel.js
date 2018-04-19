// var myCarousel = $('#myCarousel')
// carouselLinkedNav = $('.carousel-linked-nav')
// carouselLinkedProjects = $('.carousel-linked-projects')
// allSlides = $('#allSlides').find('div.item')
// invoke the carousel
$('#myCarousel').carousel({
  interval: 3000
});

/* SLIDE ON CLICK */ 

carouselLinkedNav.find('li > a').click(function() {
    var $this = $(this)
    // grab href, remove pound sign, convert to number
      , item = $this.attr('href').substring(1) | 0;

    // slide to number -1 (account for zero indexing)
    $('#myCarousel').carousel(item - 1);

    // remove current active class
    carouselLinkedNav.find('.active').removeClass('active');

    // add active class to just clicked on item
    $this.closest('li').addClass('active');

    // don't follow the link
    return false;
});

carouselLinkedProjects.find(' li > a').click(function() {
    carouselLinkedProjects.find('li').removeClass('active')
    $(this).closest('li').addClass('active')
    
    var currentProject = $(this).data('project')
    
     myCarousel.find('.item').remove()
     $slides = allSlides.filter( function () { 
          return $(this).data('project') == currentProject 
     })
     
     $slides.eq(0).addClass('active')
     
     console.log(this, currentProject , $slides )
     
     myCarousel.find('.carousel-inner').append($slides)
     
     myCarousel.carousel("pause").removeData().carousel(0)
    
    return false
});
/* AUTOPLAY NAV HIGHLIGHT */

// bind 'slid' function
myCarousel.bind('slid', function() {

    // remove active class
    carouselLinkedNav.find('.active').removeClass('active');

    // get index of currently active item
    var idx = myCarousel.find('item.active').index();

    // select currently active item and add active class
    $('.carousel-linked-nav li:eq(' + idx + ')').addClass('active');

});