"""Set up the route returns."""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from learning_journal.models import JournalEntry
import datetime


@view_config(route_name='list', renderer='../templates/list.jinja2')
def list_view(request):
    """Return the home view."""
    session = request.dbsession
    entry = session.query(JournalEntry).order_by(JournalEntry.publish_date.desc()).all()
    return {
        'page': 'Home',
        'entry': entry
    }


@view_config(route_name='detail', renderer='../templates/detail.jinja2')
def detail_view(request):
    """Return the detail view."""
    the_id = int(request.matchdict['id'])
    session = request.dbsession
    entry = session.query(JournalEntry).get(the_id)
    if not entry:
        raise HTTPNotFound
    return {
        'page': entry.title,
        'date': datetime.datetime.strftime(entry.publish_date, '%A %B %-d, %Y'),
        'title': entry.title,
        'text': entry.body,
        'id': entry.id
    }


@view_config(route_name='create', renderer='../templates/new.jinja2')
def create_view(request):
    """Return the create view."""
    print('in create view')
    print(request, request.method)
    if request.method == 'POST' and request.POST:
        print('in createview POST logic')
        new_entry = JournalEntry(
            title=request.POST['title'],
            body=request.POST['body'],
            author='Morgan',
            publish_date=datetime.datetime.now()
        )
        request.dbsession.add(new_entry)
        return HTTPFound(
            location=request.route_url('list')
        )
    return {}


@view_config(route_name='update', renderer='../templates/edit.jinja2')
def update_view(request):
    """Return the update view."""
    the_id = int(request.matchdict['id'])
    session = request.dbsession
    entry = session.query(JournalEntry).get(the_id)
    if not entry:
        raise HTTPNotFound
    return {
        'page': 'Edit Entry',
        'date': entry.publish_date,
        'title': entry.title,
        'text': entry.body,
        'id': entry.id
    }
