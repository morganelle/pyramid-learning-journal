'use strict';

(function(module) {
  // clear function to remove previously appended projects
  const clear = function() {
    $('#project-content').find('article.project').remove();
  };
  const projectView = {};

  projectView.display = function() {
    clear();
    Project.all.forEach(project => $('#project-content').append(project.populateTemplate()));
  }
  // expose projectView object to global space
  module.projectView = projectView;
})(window);
