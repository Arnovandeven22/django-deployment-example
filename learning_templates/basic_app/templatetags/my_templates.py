from django import template

register = template.Library()

@register.filter(name='strip_value')
def strip_value(value, arg):
    """
    This cuts out all values or 'arg' from the string!
    """
    return value.replace(arg, '')

# register.filter('strip_value', strip_value)
