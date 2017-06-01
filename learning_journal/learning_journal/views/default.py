"""Set up the route returns."""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound
from learning_journal.views.data.entries import ENTRIES


@view_config(route_name='list', renderer='../templates/list.jinja2')
def list_view(request):
    """Return the home view."""
    return {
        'page': 'Home',
        'entry': ENTRIES
    }


@view_config(route_name='detail', renderer='../templates/detail.jinja2')
def detail_view(request):
    """Return the detail view."""
    the_id = int(request.matchdict['id'])
    entry = None
    for item in ENTRIES:
        if item['id'] == the_id:
            entry = item
            break
    if not entry:
        raise HTTPNotFound
    return {
        'page': entry['title'],
        'entry': entry
    }


@view_config(route_name='create', renderer='../templates/new.jinja2')
def create_view(request):
    """Return the create view."""
    return {
        'page': 'New Entry'
    }


@view_config(route_name='update', renderer='../templates/edit.jinja2')
def update_view(request):
    """Return the update view."""
    the_id = int(request.matchdict['id'])
    try:
        entry = ENTRIES[the_id]
    except IndexError:
        raise HTTPNotFound
    return {
        'page': 'Edit Entry',
        'entry': entry
    }
