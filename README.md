# pyramid-learning-journal

Owner: Morgan Nomura
Collaborators: James Feore

## Deployment:
Deployed on Heroku at https://rocky-inlet-61764.herokuapp.com/

## Test instructions:
In order to test, please create the following environmental variables:
- DATABASE_URL
- AUTH_SECRET
- AUTH_USERNAME
- AUTH_PASSWORD

In addition, there are two commented-out tests (test_login_view_bad_login_username and test_login_view_good_login) that will require entering in un-hashed passwords.


## Tests:
### Test plan
Please see TEST_PLAN.md

### Test coverage
Latest tox report:

---------- coverage: platform darwin, python 2.7.13-final-0 ----------
Name                                      Stmts   Miss  Cover   Missing
-----------------------------------------------------------------------
learning_journal/models/__init__.py          22      0   100%
learning_journal/models/entries.py            9      0   100%
learning_journal/models/meta.py               5      0   100%
learning_journal/views/data/__init__.py       0      0   100%
learning_journal/views/data/entries.py        1      0   100%
learning_journal/views/default.py            39      5    87%   80-84
learning_journal/views/notfound.py            4      0   100%
-----------------------------------------------------------------------
TOTAL                                        80      5    94%

======================================================

---------- coverage: platform darwin, python 3.6.1-final-0 -----------
Name                                      Stmts   Miss  Cover   Missing
-----------------------------------------------------------------------
learning_journal/models/__init__.py          22      0   100%
learning_journal/models/entries.py            9      0   100%
learning_journal/models/meta.py               5      0   100%
learning_journal/views/data/__init__.py       0      0   100%
learning_journal/views/data/entries.py        1      0   100%
learning_journal/views/default.py            39      5    87%   80-84
learning_journal/views/notfound.py            4      0   100%
-----------------------------------------------------------------------
TOTAL                                        80      5    94%

27 passed in 2.12 seconds
__________________________________________________________ 
__________________________________________________________
  py27: commands succeeded
  py36: commands succeeded


### Color palette
https://coolors.co/2e5266-6e8898-9fb1bc-d3d0cb-e2c044