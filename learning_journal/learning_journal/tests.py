"""Learning Journal tests."""
from pyramid import testing
# from pyramid.response import Response
from pyramid.httpexceptions import HTTPNotFound
from learning_journal.views.data.entries import ENTRIES
import pytest


@pytest.fixture
def httprequest():
    """Return a test request."""
    request = testing.DummyRequest()
    return request


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


def test_list_view_returns_content(list_response):
    """List view response includes content."""
    assert 'page' in list_response
    assert 'entry' in list_response
    assert list_response['entry'] == ENTRIES


def test_create_view_returns_content(create_response):
    """Create view response includes content."""
    assert 'page' in create_response


def test_detail_view_returns_content(detail_response):
    """Detail view response includes content."""
    assert 'page' in detail_response
    assert 'entry' in detail_response
    assert detail_response['entry'] == ENTRIES[0]


def test_update_view_returns_content(update_response):
    """Detail view response includes content."""
    assert 'page' in update_response
    assert 'entry' in update_response
    assert update_response['entry'] == ENTRIES[0]


def test_detail_view_with_id_raises_except():
    """."""
    from learning_journal.views.default import detail_view
    request = testing.DummyRequest()
    request.matchdict['id'] = '1000'
    with pytest.raises(HTTPNotFound):
        detail_view(request)


def test_update_view_with_id_raises_except():
    """."""
    from learning_journal.views.default import update_view
    request = testing.DummyRequest()
    request.matchdict['id'] = '1000'
    with pytest.raises(HTTPNotFound):
        update_view(request)


def test_entries():
    """Test validity of dictionary."""
    assert type(ENTRIES[0]) == dict


# ++++++++ Functional Tests +++++++++ #


@pytest.fixture
def testapp():
    """Create a test application for functional tests."""
    from learning_journal import main
    from webtest import TestApp
    app = main({})
    return TestApp(app)


def test_home_route_returns_home_content(testapp):
    """."""
    response = testapp.get('/')
    html = response.html
    assert str(html.find('h2')) == '<h2>Entry 1</h2>'
