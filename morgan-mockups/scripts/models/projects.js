'use strict';
(function(module) {
  // global variables
  Project.all = [];

  // project constructor
  function Project(options) {
    this.image = options.image; // need to set up image folder structure first
    this.title = options.title;
    this.clientName = options.clientName;
    this.role = options.role;
    this.category = options.category; // need to decide if this should be an array
    this.summary = options.summary;
    this.link = options.link;
  }

  // method to create new project article from template
  Project.prototype.populateTemplate = function() {
    let template = Handlebars.compile($('#article-template').html());
    return template(this);
  }

  // method that gets data from JSON file and maps to Project.all array
  Project.getData = function(callback) {
    $.getJSON('../../data/projectContent.json')
    .then(data => Project.all = data.map(datum => new Project(datum)))
    .then(function() {
      callback();
    })
  }

  module.Project = Project;
})(window);
