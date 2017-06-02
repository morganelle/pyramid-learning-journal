"""Learning Journal tests."""
from pyramid import testing
from pyramid.config import Configurator
# from pyramid.response import Response
from pyramid.httpexceptions import HTTPNotFound
from learning_journal.models import JournalEntry, get_tm_session
import pytest
from learning_journal.models.meta import Base
import datetime
from faker import Faker
import transaction


FAKE_FACTORY = Faker()
JOURNAL_ENTRIES = [JournalEntry(
    author=FAKE_FACTORY.name(),
    body=FAKE_FACTORY.text(300),
    publish_date=datetime.datetime.now(),
    title=FAKE_FACTORY.text(300)
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
    config.include("learning_journal.models")

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
    """Instantiate a fake HTTP Request, complete with a database session."""
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


@pytest.fixture(scope="session")
def testapp(request):
    """Create a test application for functional tests."""
    from webtest import TestApp

    def main(global_config, **settings):
        """Return a Pyramid WSGI application."""
        settings['sqlalchemy.url'] = 'postgres:///test_journal'
        config = Configurator(settings=settings)
        config.include('pyramid_jinja2')
        config.include('.models')
        config.include('.routes')
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
    """File the DB."""
    SessionFactory = testapp.app.registry["dbsession_factory"]
    with transaction.manager:
        dbsession = get_tm_session(SessionFactory, transaction.manager)
        dbsession.add_all(JOURNAL_ENTRIES)

    return dbsession


# def test_list_view_returns_content(list_response):
#     """List view response includes content."""
#     assert 'page' in list_response
#     assert 'entry' in list_response
#     assert list_response['entry'] == entry


# def test_create_view_returns_content(create_response):
#     """Create view response includes content."""
#     assert 'page' in create_response


# def test_detail_view_returns_content(detail_response):
#     """Detail view response includes content."""
#     assert 'page' in detail_response
#     assert 'entry' in detail_response
#     assert detail_response['entry'] == ENTRIES[0]


# def test_update_view_returns_content(update_response):
#     """Detail view response includes content."""
#     assert 'page' in update_response
#     assert 'entry' in update_response
#     assert update_response['entry'] == ENTRIES[0]


# def test_detail_view_with_id_raises_except():
#     """."""
#     from learning_journal.views.default import detail_view
#     request = testing.DummyRequest()
#     request.matchdict['id'] = '1000'
#     with pytest.raises(HTTPNotFound):
#         detail_view(request)


# def test_update_view_with_id_raises_except():
#     """."""
#     from learning_journal.views.default import update_view
#     request = testing.DummyRequest()
#     request.matchdict['id'] = '1000'
#     with pytest.raises(HTTPNotFound):
#         update_view(request)


# def test_entries():
#     """Test validity of dictionary."""
#     assert type(ENTRIES[0]) == dict


# # ++++++++ Functional Tests +++++++++ #


def test_list_route_returns_list_content(testapp):
    """Test list route creates page that has list entries."""
    response = testapp.get('/')
    html = response.html
    post_count = html.find_all('section')
    assert html.find('h2').text in JOURNAL_ENTRIES[0].title
    assert len(post_count) == len(JOURNAL_ENTRIES)


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
