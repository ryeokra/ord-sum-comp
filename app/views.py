from html import escape

from pyramid.view import view_config


@view_config(route_name='root', renderer='../templates/index.jinja2')
def root_view(request):
    return {
        'gh_username':
        'ryeokra',
        'gh_profile':
        'https://github.com/ryeokra',
        'challenge_link':
        'https://www.frontendmentor.io/challenges/order-summary-component-QlPmajDUj'
    }
