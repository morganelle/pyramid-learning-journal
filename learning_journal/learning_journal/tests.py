"""Learning Journal tests."""
from pyramid import testing
from pyramid.response import Response
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
    response = update_view(request)
    return response


def test_view_function_returns_responses(httprequest):
    """Ensure view functions return a Response object."""
    from learning_journal.views.default import list_view, detail_view, create_view, update_view
    assert isinstance(list_view(httprequest), Response)
    assert isinstance(detail_view(httprequest), Response)
    assert isinstance(create_view(httprequest), Response)
    assert isinstance(update_view(httprequest), Response)


def test_view_function_status_200(httprequest):
    """Ensure view functions return a Response object."""
    from learning_journal.views.default import list_view, detail_view, create_view, update_view
    assert list_view(httprequest).status_code == 200
    assert detail_view(httprequest).status_code == 200
    assert create_view(httprequest).status_code == 200
    assert update_view(httprequest).status_code == 200


def test_list_view_returns_proper_content(list_response):
    """List view response includes the content we added."""
    expected_text = '<p>Morgan Nomura // Blog</p>'
    assert expected_text in list_response.text


def test_detail_view_returns_proper_content(detail_response):
    """Detail view response includes the content we added."""
    expected_text = '<p class="post-content">Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    assert expected_text in detail_response.text


def test_create_view_returns_proper_content(create_response):
    """Create view response includes the content we added."""
    expected_text = '<h1>Create a new post</h1>'
    assert expected_text in create_response.text


def test_update_view_returns_proper_content(update_response):
    """Update view response includes the content we added."""
    expected_text = '<h1>Edit post</h1>'
    assert expected_text in update_response.text
