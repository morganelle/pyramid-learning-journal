'use strict';

(function(module) {
  let adminView = {};
  // Creates category inputs on blog-fields form
  adminView.populateCategories = function() {
    let template = Handlebars.compile($('#category-input-template').html());
    let inputs = template(context);
    $('label#category-checkboxes').append(inputs);
  }

  // Hides for preview section by default
  $('#preview').hide();

  // Registers event on blog-fields form
  $('#blog-fields').on('change', function() {
    $('#preview').show();
    $('article.blog-post').remove();
    adminView.blogPreview();
  });

  // Get information from form
  adminView.blogPreview = function() {
    // instantiate new blog object
    let blog = new BlogContent({
      title: $('#post-title').val(),
      publishedDate: (new Date($('#post-date').val())).toDateString(),
      author: $('#post-author').val(),
      postContent: $('#post-content').val(),
      category: ['category']
    });
    // Append blog content to preview section
    $('#preview').append(blog.populateTemplate());
    $('#blog-json').val(JSON.stringify(blog) + ',');
  }
  module.adminView = adminView;
})(window);
