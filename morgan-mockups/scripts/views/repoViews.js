'use strict';

(function(module) {
  const repoView = {};
  // clear function to remove previously appended projects
  const clear = function() {
    let $projects = $('#projects');
    $projects.find('ul').empty();
    $projects.show().siblings().hide();
  };
  // create handlebars template
  let template = Handlebars.compile($('#repo-template').html());

  repoView.display = function() {
    console.log('repoView display begins');
    clear();
    $('#projects ul').append(
      // repos.with('name').map(template)
      repos.all.map(template)
    );
  };
  // expose repoView object to global space
  module.repoView = repoView;
})(window);
