'use strict';

(function(module) {
  const repos = {};

  repos.all = [];

  repos.requestRepos = function(callback) {
    $.get('github/user/repos')
    .then(data => repos.all = data, err => console.error(err))
    .then(callback);
  };

  // function for filtering repos.all
  repos.with = attr => repos.all.filter(repo => repo[attr]);

  module.repos = repos;
})(window);
