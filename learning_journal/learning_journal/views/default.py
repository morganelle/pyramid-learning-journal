"""Set up the route returns."""
from pyramid.security import remember, forget
from learning_journal.security import check_credentials
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from learning_journal.models import JournalEntry
import datetime


@view_config(route_name='list', renderer='../templates/list.jinja2', require_csrf=False)
def list_view(request):
    """Return the home view."""
    session = request.dbsession
    entry = session.query(JournalEntry).order_by(JournalEntry.publish_date.desc()).all()
    return {
        'page': 'Home',
        'entry': entry,
        'userauth': request.authenticated_userid
    }


@view_config(route_name='detail', renderer='../templates/detail.jinja2', require_csrf=False)
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
        'id': entry.id,
        'userauth': request.authenticated_userid
    }


@view_config(route_name='create', renderer='../templates/new.jinja2', permission='secret')
def create_view(request):
    """Return the create view."""
    print('in create view')
    print(request, request.method)
    if request.method == 'POST' and request.POST:
        if not request.POST['title'] or not request.POST['body']:
            return {
                'title': request.POST['title'],
                'body': request.POST['body']
            }
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


@view_config(route_name='update', renderer='../templates/edit.jinja2', permission='secret')
def update_view(request):
    """Return the update view."""
    the_id = int(request.matchdict['id'])
    session = request.dbsession
    entry = session.query(JournalEntry).get(the_id)

    if not entry:
        raise HTTPNotFound

    if request.method == 'GET':
        return {
            'page': 'Edit Entry',
            'date': entry.publish_date,
            'title': entry.title,
            'text': entry.body,
            'id': entry.id
        }

    if request.method == 'POST':
        entry.title = request.POST['title'],
        entry.body = request.POST['body']
        request.dbsession.flush()
        return HTTPFound(request.route_url('detail', id=entry.id))


@view_config(route_name='login', renderer='../templates/login.jinja2', require_csrf=False)
def login_view(request):
    """View for logging in a user."""
    if request.method == "GET":
        return {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if check_credentials(username, password):
            headers = remember(request, username)
            return HTTPFound(
                location=request.route_url('list'),
                headers=headers
            )
        return {'error': 'Bad username or password'}


@view_config(route_name='logout', require_csrf=False)
def logout(request):
    """Log user out."""
    headers = forget(request)
    return HTTPFound(request.route_url('list'), headers=headers)
