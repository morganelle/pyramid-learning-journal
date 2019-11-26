# pyramid-learning-journal

Owner: Morgan Nomura
Collaborators: James Feore

## Deployment:
Deployed on Heroku at https://rocky-inlet-61764.herokuapp.com/

## Install locally:
- pip install -r requirements.txt

## Test instructions:
- test.py includes dummy environmental variables
- run tox from the directory that tox.ini lives in


## Tests:
### Test plan
Please see TEST_PLAN.md

### Test coverage
Latest tox report:
```
---------- coverage: platform darwin, python 2.7.13-final-0 ----------
Name                                      Stmts   Miss  Cover   Missing
-----------------------------------------------------------------------
learning_journal/models/__init__.py          22      0   100%
learning_journal/models/entries.py            9      0   100%
learning_journal/models/meta.py               5      0   100%
learning_journal/security.py                 30      0   100%
learning_journal/views/data/__init__.py       0      0   100%
learning_journal/views/data/entries.py        1      0   100%
learning_journal/views/default.py            54      0   100%
learning_journal/views/notfound.py            4      0   100%
-----------------------------------------------------------------------
TOTAL                                       125      0   100%

46 passed in 11.41 seconds


py36 runtests: PYTHONHASHSEED='1440921674'
py36 runtests: commands[0] | py.test --cov=learning_journal -q --cov-report term-missing
..............................................

---------- coverage: platform darwin, python 3.6.1-final-0 -----------
Name                                      Stmts   Miss  Cover   Missing
-----------------------------------------------------------------------
learning_journal/models/__init__.py          22      0   100%
learning_journal/models/entries.py            9      0   100%
learning_journal/models/meta.py               5      0   100%
learning_journal/security.py                 30      0   100%
learning_journal/views/data/__init__.py       0      0   100%
learning_journal/views/data/entries.py        1      0   100%
learning_journal/views/default.py            54      0   100%
learning_journal/views/notfound.py            4      0   100%
-----------------------------------------------------------------------
TOTAL                                       125      0   100%

46 passed in 10.39 seconds


  py27: commands succeeded
  py36: commands succeeded
  congratulations :)
```


### Color palette
https://coolors.co/2e5266-6e8898-9fb1bc-d3d0cb-e2c044