"""Learning Journal tests."""
from pyramid import testing
from pyramid.config import Configurator
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from learning_journal.models import JournalEntry, get_tm_session
import pytest
from learning_journal.models.meta import Base
import datetime
import os
from faker import Faker
import transaction


SITE_ROOT = "http://localhost"
FAKE_FACTORY = Faker()
JOURNAL_ENTRIES = [JournalEntry(
    author=FAKE_FACTORY.name(),
    body=FAKE_FACTORY.text(300),
    publish_date=datetime.datetime.now(),
    title=FAKE_FACTORY.text(20)
) for i in range(20)]


@pytest.fixture
def add_models(dummy_request):
    """Add a bunch of model instances to the database."""
    dummy_request.dbsession.add_all(JOURNAL_ENTRIES)


@pytest.fixture(scope="session")
def configuration(request):
    """Set up a Configurator instance."""
    config = testing.setUp(settings={
        'sqlalchemy.url': 'postgres:///test_journal'
    })
    config.include('learning_journal.models')
    config.include('learning_journal.routes')

    def teardown():
        testing.tearDown()

    request.addfinalizer(teardown)
    return config


@pytest.fixture
def db_session(configuration, request):
    """Create a session for interacting with the test database."""
    SessionFactory = configuration.registry["dbsession_factory"]
    session = SessionFactory()
    engine = session.bind
    Base.metadata.create_all(engine)

    def teardown():
        session.transaction.rollback()
        Base.metadata.drop_all(engine)

    request.addfinalizer(teardown)
    return session


@pytest.fixture
def dummy_request(db_session):
    """Instantiate a fake HTTP Request with a database session."""
    return testing.DummyRequest(dbsession=db_session)


@pytest.fixture
def list_response():
    """Return a response from the list view."""
    from learning_journal.views.default import list_view
    request = testing.DummyRequest()
    response = list_view(request)
    return response


@pytest.fixture
def detail_response():
    """Return a response from the detail view."""
    from learning_journal.views.default import detail_view
    request = testing.DummyRequest()
    request.matchdict['id'] = 0
    response = detail_view(request)
    return response


@pytest.fixture
def create_response():
    """Return a response from the create view."""
    from learning_journal.views.default import create_view
    request = testing.DummyRequest()
    response = create_view(request)
    return response


@pytest.fixture
def update_response():
    """Return a response from the update view."""
    from learning_journal.views.default import update_view
    request = testing.DummyRequest()
    request.matchdict['id'] = 0
    response = update_view(request)
    return response


@pytest.fixture
def set_credentials():
    """Create credentials for test."""
    from passlib.apps import custom_app_context as context
    import os
    os.environ['AUTH_USERNAME'] = 'usermcgee'
    os.environ['AUTH_PASSWORD'] = context.hash('bakeacake')


@pytest.fixture(scope="session")
def testapp(request):
    """Create a test application for functional tests."""
    from webtest import TestApp

    def main(global_config, **settings):
        """Return a Pyramid WSGI application."""
        settings['sqlalchemy.url'] = 'postgres:///test_journal'
        config = Configurator(settings=settings)
        config.include('pyramid_jinja2')
        config.include('learning_journal.models')
        config.include('learning_journal.routes')
        config.include('learning_journal.security')
        config.scan()
        return config.make_wsgi_app()

    app = main({})
    testapp = TestApp(app)

    SessionFactory = app.registry["dbsession_factory"]
    engine = SessionFactory().bind
    Base.metadata.create_all(bind=engine)

    def tearDown():
        Base.metadata.drop_all(bind=engine)

    request.addfinalizer(tearDown)

    return testapp


@pytest.fixture
def fill_the_db(testapp):
    """Fill the DB."""
    SessionFactory = testapp.app.registry["dbsession_factory"]
    with transaction.manager:
        dbsession = get_tm_session(SessionFactory, transaction.manager)
        dbsession.add_all(JOURNAL_ENTRIES)

    return dbsession


@pytest.fixture
def empty_the_db(testapp):
    """Clear database and create a new empty one."""
    SessionFactory = testapp.app.registry['dbsession_factory']
    engine = SessionFactory().bind
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


# ++++++++ Unit Tests +++++++++ #


def test_detail_view_with_id_raises_except(dummy_request):
    """."""
    from learning_journal.views.default import detail_view
    dummy_request.matchdict['id'] = '1000'
    with pytest.raises(HTTPNotFound):
        detail_view(dummy_request)


def test_update_view_with_id_raises_except(dummy_request):
    """."""
    from learning_journal.views.default import update_view
    dummy_request.matchdict['id'] = '1000'
    with pytest.raises(HTTPNotFound):
        update_view(dummy_request)


def test_entries():
    """Test validity of dictionary."""
    assert isinstance(JOURNAL_ENTRIES[0], JournalEntry)


def test_model_gets_added(db_session):
    """Test to see if we can instantiate and load a DB."""
    assert len(db_session.query(JournalEntry).all()) == 0
    model = JournalEntry(
        title=u"Fake Category",
        publish_date=datetime.datetime.now(),
        author=u"Whoever",
        body=u"Some text in the body"
    )
    db_session.add(model)
    assert len(db_session.query(JournalEntry).all()) == 1


def test_list_view_returns_dict(dummy_request):
    """List view returns a dictionary of values."""
    from learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert isinstance(response, dict)


def test_list_view_returns_empty_when_database_empty(dummy_request):
    """List view returns nothing when there is no data."""
    from learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert len(response['entry']) == 0


def test_list_view_returns_count_matching_database(dummy_request, add_models):
    """List view response matches database count."""
    from learning_journal.views.default import list_view
    response = list_view(dummy_request)
    query = dummy_request.dbsession.query(JournalEntry)
    assert len(response['entry']) == query.count()


def test_create_view_post_empty_is_empty_dict(dummy_request):
    """POST requests should return empty dictionary."""
    from learning_journal.views.default import create_view
    dummy_request.method = 'POST'
    response = create_view(dummy_request)
    assert response == {}


def test_create_view_post_incomplete_data_returns_data(dummy_request):
        """Incomplete POST data returned to user."""
        from learning_journal.views.default import create_view
        dummy_request.method = "POST"
        post_data = {'body': 'fake title', 'title': ''}
        dummy_request.POST = post_data
        response = create_view(dummy_request)
        assert response == post_data


def test_create_view_post_with_data_302(dummy_request):
        """POST request with correct data should redirect with status code 302."""
        from learning_journal.views.default import create_view
        dummy_request.method = "POST"
        post_data = {
            'title': u'cake title',
            'body': FAKE_FACTORY.text(300)
        }
        dummy_request.POST = post_data
        response = create_view(dummy_request)
        assert response.status_code == 302


def test_update_view_post_with_data(db_session, dummy_request):
        """Get request on update view shows correct content."""
        from learning_journal.views.default import update_view
        model = JournalEntry(
            title=u'Fake Category',
            publish_date=datetime.datetime.now(),
            author=u'A big bozo',
            body=u'Some text in the body'
        )
        db_session.add(model)
        get_entry = db_session.query(JournalEntry)
        get_entry = get_entry[0].id
        get_entry = str(get_entry)
        dummy_request.method = 'GET'
        dummy_request.matchdict['id'] = get_entry
        response = update_view(dummy_request)
        assert model.title in response['title']
        assert model.body in response['text']


def test_update_view_post_with_data_302(db_session, dummy_request):
        """Get request on update view shows correct content."""
        from learning_journal.views.default import update_view
        post_data = {
            'title': u'cake title',
            'body': u'updated text'
        }
        model = JournalEntry(
            title=u'Fake Category',
            publish_date=datetime.datetime.now(),
            author=u'A big bozo',
            body=u'Some text in the body'
        )
        db_session.add(model)
        get_entry = db_session.query(JournalEntry)
        get_entry = get_entry[0].id
        get_entry = str(get_entry)
        dummy_request.method = 'POST'
        dummy_request.matchdict['id'] = get_entry
        dummy_request.POST = post_data
        response = update_view(dummy_request)
        assert response.status_code == 302


def test_update_view_post_updates_db(db_session, dummy_request):
        """Get request on update view shows correct content."""
        from learning_journal.views.default import update_view
        post_data = {
            'title': u'cake title',
            'body': u'updated text'
        }
        model = JournalEntry(
            title=u'Fake Category',
            publish_date=datetime.datetime.now(),
            author=u'A big bozo',
            body=u'Some text in the body'
        )
        db_session.add(model)
        get_entry = db_session.query(JournalEntry)
        get_entry = get_entry[0].id
        get_entry = str(get_entry)
        dummy_request.method = 'POST'
        dummy_request.matchdict['id'] = get_entry
        dummy_request.POST = post_data
        response = update_view(dummy_request)
        updated_entry = db_session.query(JournalEntry)
        assert updated_entry[0].body == post_data['body']
        assert isinstance(response, HTTPFound)


def test_login_view_bad_login_both(dummy_request):
    """Attempt log in with bad username and pw."""
    from learning_journal.views.default import login_view
    dummy_request.method = 'POST'
    post_data = {
        'username': 'notmyname',
        'password': 'notmypw'
    }
    dummy_request.POST = post_data
    assert login_view(dummy_request) == {'error': 'Bad username or password'}


def test_login_view_bad_login_pw(dummy_request, set_credentials):
    """Attempt log in with good username and bad pw."""
    from learning_journal.views.default import login_view
    dummy_request.method = 'POST'
    post_data = {
        'username': os.environ.get('AUTH_USERNAME'),
        'password': 'notmypw'
    }
    dummy_request.POST = post_data
    assert login_view(dummy_request) == {'error': 'Bad username or password'}


def test_login_view_bad_login_username(dummy_request, set_credentials):
    """Attempt log in with bad username and good pw."""
    from learning_journal.views.default import login_view
    dummy_request.method = 'POST'
    post_data = {
        'username': 'notmyname',
        'password': 'bakeacake'
    }
    dummy_request.POST = post_data
    assert login_view(dummy_request) == {'error': 'Bad username or password'}


def test_login_view_bad_login_empty(dummy_request):
    """Attempt log in with empty username and pw."""
    from learning_journal.views.default import login_view
    dummy_request.method = 'POST'
    post_data = {
        'username': '',
        'password': ''
    }
    dummy_request.POST = post_data
    assert login_view(dummy_request) == {'error': 'Bad username or password'}


def test_login_view_good_login(dummy_request, set_credentials):
    """Attempt log in with good credentials"""
    from learning_journal.views.default import login_view
    dummy_request.method = 'POST'
    post_data = {
        'username': os.environ.get('AUTH_USERNAME'),
        'password': 'bakeacake'
    }
    dummy_request.POST = post_data
    assert isinstance(login_view(dummy_request), HTTPFound)


def test_login_view_get(dummy_request):
    """Login view returns empty dict on GET request."""
    from learning_journal.views.default import login_view
    dummy_request.method = 'GET'
    assert login_view(dummy_request) == {}


def test_logout_view_post_302(dummy_request):
        """POST request with correct data should redirect with status code 302."""
        from learning_journal.views.default import logout
        response = logout(dummy_request)
        assert response.status_code == 302


def test_logout_view_post_return(dummy_request):
        """POST request with correct data should redirect with status code 302."""
        from learning_journal.views.default import logout
        assert isinstance(logout(dummy_request), HTTPFound)


# ++++++++ Functional Tests +++++++++ #


def test_no_items_on_list_empty_db(testapp, empty_the_db):
    """When redirection is followed, result is home page."""
    response = testapp.get('/')
    post_count = response.html.find_all('section')
    assert len(post_count) == 0


def test_db_fill(testapp, fill_the_db):
    """Test to instantiate and load a DB."""
    response = testapp.get('/')
    post_count = response.html.find_all('section')
    assert len(fill_the_db.query(JournalEntry).all()) == len(post_count)


def test_list_route_returns_list_content(testapp, fill_the_db):
    """Test list route creates page that has list entries."""
    fill_the_db
    response = testapp.get('/')
    html = response.html
    post_count = html.find_all('section')
    assert len(post_count) == len(JOURNAL_ENTRIES)


def test_detail_route_returns_detail_content(testapp):
    """Test list route creates page that has list entries."""
    response = testapp.get('/journal/1')
    assert '<article class="blog-post">' in response.text


def test_update_route_returns_detail_content(testapp):
    """Test list route creates page that has list entries."""
    testapp.post('/login', {
        'username': os.environ.get('AUTH_USERNAME'),
        'password': 'bakeacake'}
    )
    response = testapp.get('/journal/10/edit-entry')
    assert '<h1>Edit post</h1>' in response.text


def test_detail_with_valid_route(testapp):
    """Detail page with invalid route gets correct template."""
    response = testapp.get('/journal/1', status=200)
    assert '<article class="blog-post">' in response.text


def test_list_with_valid_route(testapp):
    """Detail page with invalid route gets correct template."""
    response = testapp.get('/', status=200)
    assert '<section class="list-post">' in response.text


def test_create_view_with_valid_route(testapp):
    """Detail page with invalid route gets correct template."""
    testapp.post('/login', {
        'username': os.environ.get('AUTH_USERNAME'),
        'password': 'bakeacake'}
    )
    response = testapp.get('/journal/new-entry', status=200)
    assert '<h1>Create a new post</h1>' in response.text


def test_update_with_valid_route(testapp):
    """Detail page with invalid route gets correct template."""
    response = testapp.get('/journal/1/edit-entry', status=200)
    assert '<h1>Edit post</h1>' in response.text


def test_detail_with_invald_id(testapp):
    """Detail page with invalid route gets correct template."""
    response = testapp.get('/journal/cake', status=404)
    assert 'Page Not Found' in response.text


def test_list_with_invald_id(testapp):
    """Detail page with invalid route gets correct template."""
    response = testapp.get('/list/1', status=404)
    assert 'Page Not Found' in response.text


def test_create_view_with_invald_id(testapp):
    """Detail page with invalid route gets correct template."""
    response = testapp.get('/journa/new-entry/hello', status=404)
    assert 'Page Not Found' in response.text


def test_update_with_invald_id(testapp):
    """Detail page with invalid route gets correct template."""
    response = testapp.get('/journal/cake/edit-entry', status=404)
    assert 'Page Not Found' in response.text


def test_unauthenticated_user_forbidden_create_route(testapp):
    """Test status code of unauthenticated user."""
    testapp.get('/logout')
    response = testapp.get('/journal/new-entry', status=403)
    assert response.status_code == 403


def test_unauthenticated_user_forbidden_update_route(testapp):
    """Test status code of unauthenticated user."""
    response = testapp.get('/journal/1/edit-entry', status=403)
    assert response.status_code == 403


def test_login_route(testapp):
    """Get a 200 status code from hitting login route."""
    response = testapp.get('/login')
    assert response.status_code == 200


def test_login_route_good_creds(testapp):
    """Ensure auth_tkt in resonse headers after hitting login route."""
    response = testapp.post('/login', {
        'username': os.environ.get('AUTH_USERNAME'),
        'password': 'bakeacake'}
    )
    assert 'auth_tkt' in response.headers['Set-Cookie']


def test_logged_in_user_gets_200_create(testapp):
    """Logged in user gets status 200 on create route."""
    response = testapp.get('/journal/new-entry', status=200)
    assert response.status_code == 200


def test_logged_in_user_gets_200_update(testapp, fill_the_db):
    """Logged in user gets status 200 on valid update page."""
    response = testapp.get('/journal/1/edit-entry', status=200)
    assert response.status_code == 200


def test_login_route_form_method(testapp):
    """Confirm the form method on login is post and input value is Login."""
    response = testapp.get('/login')
    html = response.html
    assert html.find('form').attrs['method'] == 'POST'
    assert html.find('input', type='submit').attrs['value'] == 'Login'


def test_update_route_non_existent_entry(testapp):
    """Test update route for a non-existent entry returns 404 status."""
    response = testapp.get('/journal/1000/edit-entry', status=404)
    assert response.status_code == 404


def test_new_entry_redirects_to_list(testapp, empty_the_db):
    """New post added successfully, check reroute."""
    response = testapp.get('/journal/new-entry')
    token = response.html.find('input', {'type': 'hidden'}).attrs['value']
    post_data = {
        'csrf_token': token,
        'title': FAKE_FACTORY.text(20),
        'body': FAKE_FACTORY.text(300)
    }
    response = testapp.post('/journal/new-entry', post_data)
    list_route = testapp.app.routes_mapper.get_route('list').path
    assert response.location == SITE_ROOT + list_route


def test_new_entry_redirection_lands_on_list(testapp, empty_the_db):
    """When redirection is followed, result is home page."""
    response = testapp.get('/journal/new-entry')
    token = response.html.find('input', {'type': 'hidden'}).attrs['value']
    post_data = {
        'csrf_token': token,
        'title': FAKE_FACTORY.text(20),
        'body': FAKE_FACTORY.text(300)
    }
    response = testapp.post('/journal/new-entry', post_data)
    next_response = response.follow()
    list_response = testapp.get('/')
    assert next_response.text == list_response.text


def test_new_entry_detail_exists(testapp, empty_the_db):
    """Correct new post content appears on detail route."""
    response = testapp.get('/journal/new-entry')
    token = response.html.find('input', {'type': 'hidden'}).attrs['value']
    post_data = {
        'csrf_token': token,
        'title': FAKE_FACTORY.text(20),
        'body': FAKE_FACTORY.text(300)
    }
    testapp.post('/journal/new-entry', post_data)
    details_response = testapp.get('/journal/1')
    assert post_data['title'] in details_response.text
    assert post_data['body'] in details_response.text


def test_update_view_displays_correct_content(testapp, empty_the_db):
    """Correct new post appears in edit view fields."""
    response = testapp.get('/journal/new-entry')
    token = response.html.find('input', {'type': 'hidden'}).attrs['value']
    post_data = {
        'csrf_token': token,
        'title': FAKE_FACTORY.text(20),
        'body': FAKE_FACTORY.text(300)
    }
    testapp.post('/journal/new-entry', post_data)
    details_response = testapp.get('/journal/1/edit-entry')
    assert post_data['title'] in details_response.text
    assert post_data['body'] in details_response.text
