'use strict';

(function(module) {
  const homeController = {};

  homeController.display = function() {
    console.log('homecontroller is running');
    // updates nav appearance
    $('#page-nav li').removeClass('active-nav-item');
    $('#page-nav li.home').addClass('active-nav-item');
    // displays content
    $('#page-content section').hide();
    $('#home, #home > section').show().siblings();
  }
  module.homeController = homeController;
})(window);
