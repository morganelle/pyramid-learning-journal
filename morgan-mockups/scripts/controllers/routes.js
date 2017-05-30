'use strict';

page('/journal', journalController.display);
page('/journal/:id', journalController.displayByCategory);
page('/projects', projectsController.display);
page('/', homeController.display);
page();
