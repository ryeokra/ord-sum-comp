from html import escape

from pyramid.view import view_config

@view_config(route_name='root', renderer='../templates/index.jinja2')
def root_view(request):
    return {'gh-username': 'ryeokra', 'gh-profile': 'https://github.com/ryeokra'}
