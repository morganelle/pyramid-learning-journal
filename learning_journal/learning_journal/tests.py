from pyramid import testing
from pyramid.response import Response
import pytest


@pytest.fixture
def list_response():
    """Return a response from the list view."""
    from learning_journal.views.default import list_view
    request = testing.DummyRequest()
    response = list_view(request)
    return response


def test_list_view_returns_response_given_request(list_response):
    """List view returns a Response object when given a request."""
    assert isinstance(list_response, Response)


def test_list_view_is_good(list_response):
    """List view response comes with a status 200 OK."""
    assert list_response.status_code == 200


def test_list_view_returns_proper_content(list_response):
    """List view response includes the content we added."""
    expected_text = '<p>Morgan Nomura // Blog</p>'
    assert expected_text in list_response.text


@pytest.fixture
def detail_response():
    """Return a response from the detail view."""
    from learning_journal.views.default import detail_view
    request = testing.DummyRequest()
    response = detail_view(request)
    return response


def test_detail_view_returns_response_given_request(detail_response):
    """Detail view returns a Response object when given a request."""
    assert isinstance(detail_response, Response)


def test_detail_view_is_good(detail_response):
    """List detail response comes with a status 200 OK."""
    assert detail_response.status_code == 200


def test_detail_view_returns_proper_content(detail_response):
    """Detail view response includes the content we added."""
    expected_text = '<p class="post-content">Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    assert expected_text in detail_response.text


@pytest.fixture
def create_response():
    """Return a response from the create view."""
    from learning_journal.views.default import create_view
    request = testing.DummyRequest()
    response = create_view(request)
    return response


def test_create_view_returns_response_given_request(create_response):
    """Create view returns a Response object when given a request."""
    assert isinstance(create_response, Response)


def test_create_view_is_good(create_response):
    """List create response comes with a status 200 OK."""
    assert create_response.status_code == 200


def test_create_view_returns_proper_content(create_response):
    """Create view response includes the content we added."""
    expected_text = '<h1>Create a new post</h1>'
    assert expected_text in create_response.text


@pytest.fixture
def update_response():
    """Return a response from the update view."""
    from learning_journal.views.default import update_view
    request = testing.DummyRequest()
    response = update_view(request)
    return response


def test_update_view_returns_response_given_request(update_response):
    """Update view returns a Response object when given a request."""
    assert isinstance(update_response, Response)


def test_update_view_is_good(update_response):
    """List update response comes with a status 200 OK."""
    assert update_response.status_code == 200


def test_update_view_returns_proper_content(update_response):
    """Update view response includes the content we added."""
    expected_text = '<h1>Edit post</h1>'
    assert expected_text in update_response.text
