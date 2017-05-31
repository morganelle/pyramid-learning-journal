"""Set up the route returns."""


from pyramid.response import Response
from os import path


HERE = path.dirname(__file__)


def list_view(request):
    """Return index.html."""
    with open(path.join(HERE, '../templates/index.html')) as the_file:
        html_file = the_file.read()
    return Response(html_file)


def detail_view(request):
    """Return post.html."""
    with open(path.join(HERE, '../templates/post.html')) as the_file:
        html_file = the_file.read()
    return Response(html_file)


def create_view(request):
    """Return post-new.html."""
    with open(path.join(HERE, '../templates/post-new.html')) as the_file:
        html_file = the_file.read()
    return Response(html_file)


def update_view(request):
    """Return post-edit.html."""
    with open(path.join(HERE, '../templates/post-edit.html')) as the_file:
        html_file = the_file.read()
    return Response(html_file)
