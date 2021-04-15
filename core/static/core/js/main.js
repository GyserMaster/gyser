/**
* Template Name: DevFolio - v2.3.0
* Template URL: https://bootstrapmade.com/devfolio-bootstrap-portfolio-html-template/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/
(function($) {
  "use strict";

  var nav = $('nav');
  var navHeight = nav.outerHeight();

  $('.navbar-toggler').on('click', function() {
    if (!$('#mainNav').hasClass('navbar-reduce')) {
      $('#mainNav').addClass('navbar-reduce');
    }
  })

  // Preloader
  $(window).on('load', function() {
    if ($('#preloader').length) {
      $('#preloader').delay(100).fadeOut('slow', function() {
        $(this).remove();
      });
    }
  });

  // Back to top button
  $(window).scroll(function() {
    if ($(this).scrollTop() > 100) {
      $('.back-to-top').fadeIn('slow');
    } else {
      $('.back-to-top').fadeOut('slow');
    }
  });
  $('.back-to-top').click(function() {
    $('html, body').animate({
      scrollTop: 0
    }, 1500, 'easeInOutExpo');
    return false;
  });

  /*--/ Star ScrollTop /--*/
  $('.scrolltop-mf').on("click", function() {
    $('html, body').animate({
      scrollTop: 0
    }, 1000);
  });

  /*--/ Star Counter /--*/
  $('.counter').counterUp({
    delay: 15,
    time: 2000
  });

  /*--/ Star Scrolling nav /--*/
  var mainNav_height = $('#mainNav').outerHeight() - 22;
  $('a.js-scroll[href*="#"]:not([href="#"])').on("click", function() {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        var scrollto = target.offset().top - mainNav_height;
        $('html, body').animate({
          scrollTop: scrollto
        }, 1000, "easeInOutExpo");
        return false;
      }
    }
  });

  // Scroll to sections on load with hash links
  if (window.location.hash) {
    var initial_nav = window.location.hash;
    if ($(initial_nav).length) {
      var scrollto_initial = $(initial_nav).offset().top - mainNav_height;
      $('html, body').animate({
        scrollTop: scrollto_initial
      }, 1000, "easeInOutExpo");
    }
  }

  // Closes responsive menu when a scroll trigger link is clicked
  $('.js-scroll').on("click", function() {
    $('.navbar-collapse').collapse('hide');
  });

  // Activate scrollspy to add active class to navbar items on scroll
  $('body').scrollspy({
    target: '#mainNav',
    offset: navHeight
  });
  /*--/ End Scrolling nav /--*/

  /*--/ Navbar Menu Reduce /--*/
  $(window).trigger('scroll');
  $(window).on('scroll', function() {
    var pixels = 50;
    var top = 1200;
    if ($(window).scrollTop() > pixels) {
      $('.navbar-expand-md').addClass('navbar-reduce');
      $('.navbar-expand-md').removeClass('navbar-trans');
    } else {
      if (!$('#navbarDefault').hasClass('show')) {
        $('.navbar-expand-md').removeClass('navbar-reduce');
      }
      $('.navbar-expand-md').addClass('navbar-trans');
    }
    if ($(window).scrollTop() > top) {
      $('.scrolltop-mf').fadeIn(1000, "easeInOutExpo");
    } else {
      $('.scrolltop-mf').fadeOut(1000, "easeInOutExpo");
    }
  });

  /*--/ Star Typed /--*/
  if ($('.text-slider').length == 1) {
    var typed_strings = $('.text-slider-items').text();
    var typed = new Typed('.text-slider', {
      strings: typed_strings.split(','),
      typeSpeed: 80,
      loop: true,
      backDelay: 1100,
      backSpeed: 30
    });
  }

  /*--/ Testimonials owl /--*/
  $('#testimonial-mf').owlCarousel({
    margin: 20,
    autoplay: true,
    autoplayTimeout: 4000,
    autoplayHoverPause: true,
    responsive: {
      0: {
        items: 1,
      }
    }
  });

  // Portfolio details carousel
  $(".portfolio-details-carousel").owlCarousel({
    autoplay: true,
    dots: true,
    loop: true,
    items: 1
  });

  // Initiate venobox (lightbox feature used in portofilo)
  $(document).ready(function() {
    $('.venobox').venobox({
      'share': false
    });
  });

  // Services
  var botontecnico = $("#botonTecnico");
  var botonWeb = $("#botonWeb");
  var botonProyects = $("#botonProyects");
  var caja1 = $("#caja1");
  var caja2 = $("#caja2");
  var caja3 = $("#caja3");
  var caja11 = $("#caja11");
  var caja22 = $("#caja22");
  var caja33 = $("#caja33");
  caja1.hide();
  caja2.hide();
  caja3.hide();
  caja11.hide();
  caja22.hide();
  caja33.hide();

  if ($(window).width() < 767) {
    botontecnico.find(".service-box").css("background", "rgba(0, 123, 255, 0.1)");
    botontecnico.find(".service-box").css("box-shadow", "0 13px 8px -10px rgba(0, 123, 255, 1)");
    caja11.slideDown("fast"); 
    botontecnico.click(function (e) {
      e.preventDefault();
      $(this).find(".service-box").css("background", "rgba(0, 123, 255, 0.1)");
      $(this).find(".service-box").css("box-shadow", "0 13px 8px -10px rgba(0, 123, 255, 1)");
      botonWeb.find(".service-box").css("background", "rgba(0, 0, 0, 0)");
      botonWeb.find(".service-box").css("box-shadow", "0 13px 8px -10px rgba(0, 0, 0, 0.1)");
      botonProyects.find(".service-box").css("background", "rgba(0, 0, 0, 0)");
      botonProyects.find(".service-box").css("box-shadow", "0 13px 8px -10px rgba(0, 0, 0, 0.1)");
      caja11.slideDown("fast");  //fadeToggle()   slideToggle()   slideUp()   slideDown
      caja22.hide();
      caja33.hide();
    });
    botonWeb.click(function (e) {
      e.preventDefault();
      $(this).find(".service-box").css("background", "rgba(0, 123, 255, 0.1)");
      $(this).find(".service-box").css("box-shadow", "0 13px 8px -10px rgba(0, 123, 255, 1)");
      botontecnico.find(".service-box").css("background", "rgba(0, 0, 0, 0)");
      botontecnico.find(".service-box").css("box-shadow", "0 13px 8px -10px rgba(0, 0, 0, 0.1)");
      botonProyects.find(".service-box").css("background", "rgba(0, 0, 0, 0)");
      botonProyects.find(".service-box").css("box-shadow", "0 13px 8px -10px rgba(0, 0, 0, 0.1)");
      caja22.slideDown("fast");  //fadeToggle()   slideToggle()   slideUp()   slideDown
      caja11.hide();
      caja33.hide();
    });
    botonProyects.click(function (e) {
      e.preventDefault();
      $(this).find(".service-box").css("background", "rgba(0, 123, 255, 0.1)");
      $(this).find(".service-box").css("box-shadow", "0 13px 8px -10px rgba(0, 123, 255, 1)");
      botontecnico.find(".service-box").css("background", "rgba(0, 0, 0, 0)");
      botontecnico.find(".service-box").css("box-shadow", "0 13px 8px -10px rgba(0, 0, 0, 0.1)");
      botonWeb.find(".service-box").css("background", "rgba(0, 0, 0, 0)");
      botonWeb.find(".service-box").css("box-shadow", "0 13px 8px -10px rgba(0, 0, 0, 0.1)");
      caja33.slideDown("fast");  //fadeToggle()   slideToggle()   slideUp()   slideDown
      caja22.hide();
      caja11.hide();
    });

  } else {
    botontecnico.find(".service-box").css("background", "rgba(0, 123, 255, 0.1)");
    botontecnico.find(".service-box").css("box-shadow", "0 13px 8px -10px rgba(0, 123, 255, 1)");
    caja1.slideDown("fast"); 
    botontecnico.click(function (e) {
      e.preventDefault();
      $(this).find(".service-box").css("background", "rgba(0, 123, 255, 0.1)");
      $(this).find(".service-box").css("box-shadow", "0 13px 8px -10px rgba(0, 123, 255, 1)");
      botonWeb.find(".service-box").css("background", "rgba(0, 0, 0, 0)");
      botonWeb.find(".service-box").css("box-shadow", "0 13px 8px -10px rgba(0, 0, 0, 0.1)");
      botonProyects.find(".service-box").css("background", "rgba(0, 0, 0, 0)");
      botonProyects.find(".service-box").css("box-shadow", "0 13px 8px -10px rgba(0, 0, 0, 0.1)");
      caja1.slideDown("slow");  //fadeToggle()   slideToggle()   slideUp()   slideDown
      caja2.hide();
      caja3.hide();
    });
    botonWeb.click(function (e) {
      e.preventDefault();
      $(this).find(".service-box").css("background", "rgba(0, 123, 255, 0.1)");
      $(this).find(".service-box").css("box-shadow", "0 13px 8px -10px rgba(0, 123, 255, 1)");
      botontecnico.find(".service-box").css("background", "rgba(0, 0, 0, 0)");
      botontecnico.find(".service-box").css("box-shadow", "0 13px 8px -10px rgba(0, 0, 0, 0.1)");
      botonProyects.find(".service-box").css("background", "rgba(0, 0, 0, 0)");
      botonProyects.find(".service-box").css("box-shadow", "0 13px 8px -10px rgba(0, 0, 0, 0.1)");
      caja2.slideDown("slow");  //fadeToggle()   slideToggle()   slideUp()   slideDown
      caja1.hide();
      caja3.hide();
    });
    botonProyects.click(function (e) {
      e.preventDefault();
      $(this).find(".service-box").css("background", "rgba(0, 123, 255, 0.1)");
      $(this).find(".service-box").css("box-shadow", "0 13px 8px -10px rgba(0, 123, 255, 1)");
      botontecnico.find(".service-box").css("background", "rgba(0, 0, 0, 0)");
      botontecnico.find(".service-box").css("box-shadow", "0 13px 8px -10px rgba(0, 0, 0, 0.1)");
      botonWeb.find(".service-box").css("background", "rgba(0, 0, 0, 0)");
      botonWeb.find(".service-box").css("box-shadow", "0 13px 8px -10px rgba(0, 0, 0, 0.1)");
      caja3.slideDown("slow");  //fadeToggle()   slideToggle()   slideUp()   slideDown
      caja2.hide();
      caja1.hide();
    });
  }

})(jQuery);