from django import template

register = template.Library()

def contains(value, arg):
    """
    Usage:
    {% if link_url|contains:"http://www.youtube.com/" %}
    Stuff
    {% else %}
    Not stuff
    {% endif %}
    """
    return arg in value
register.filter('contains', contains) 
