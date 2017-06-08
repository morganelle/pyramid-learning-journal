# Test plan for pyramid-learning-journal project

## Unit tests: view functions
- ~~list_view populates list template with journal entries~~
- detail_view populates detail template with journal entry that matches request id
- ~~update_view populates form with journal entry that matches request id (when 'update' route hit with GET method)~~
- ~~update_view accepts valid POST request~~
- ~~create_view returns data if POST request missing data~~
- ~~detail_view raises HTTPNotFound error if JournalEntry doesn't exist~~
- ~~update_view raises HTTPNotFound error if JournalEntry doesn't exist~~
- ~~create_view returns an empty dictionary for POST request~~
- ~~create_view returns dictionary for incomplete POST request~~
- ~~update_view has 302 status code after successful POST~~
- ~~update_view raises HTTPNotFound error if id doesn't exist~~
- ~~create_view has 302 status code after POST~~
- ~~generated journal entries are instance of JournalEntry model class~~
- ~~model can be added successfully to database~~
- ~~model can be updated in database~~
- ~~login view with bad pw and username returns error~~
- ~~login view with bad pw and good username returns error~~
- ~~login view with good pw and bad username returns error~~
- ~~login view with correct credentials returns HTTPFound object~~
- ~~logout function returns 302 status code~~
- ~~logout function returns instance of HTTP found~~ 


## Functional tests: system
- ~~list view returns empty when database empty~~
- ~~list view shows same number of items as database~~
- ~~update_view redirects to detail view of journal entry~~
- ~~create_view redirects to list route~~
- ~~general invalid route returns 404~~
- ~~invalid update route returns 404~~
- ~~invalid create route returns 404~~
- ~~invalid list route returns 404~~
- ~~invalid detail route returns 404~~
- ~~valid update route returns 200~~
- ~~valid update route results in correct content rendered on page~~
- ~~valid create route returns 200~~
- ~~valid detail route returns 200~~
- ~~new entry displays on its detail page~~
- ~~valid list route returns 200~~
- ~~valid list route results in correct content rendered on page~~