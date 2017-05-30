'use strict';

(function(module) {
  const journalController = {};
  // clear function to remove previously appended projects
  const clear = function() {
    $('#blog').find('article.blog-post').remove();
  };

  journalController.display = function() {
    console.log('journalcontroller is running');
    clear();
    // updates nav appearance
    $('#page-nav li').removeClass('active-nav-item');
    $('#page-nav li.journal').addClass('active-nav-item');
    // loads and appends posts
    BlogContent.getBlogPosts();
    // displays content
    $('#page-content section').hide();
    $('#blog').show().siblings();
  }
  journalController.displayByCategory = function(ctx) {
    var category = ctx.params.id;
    $('article.blog-post').hide();
    $('article.blog-post').has('a.' + category).css('display', 'block');
    $('p#category-display').text(`Category: ${category}`);
    $('html, body').animate({scrollTop: '0px'}, 800);
  }
  module.journalController = journalController;
})(window);
