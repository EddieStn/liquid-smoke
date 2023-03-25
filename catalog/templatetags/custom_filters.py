from django import template

register = template.Library()


@register.filter
def make_range(value, start=1):
    return range(start, value+1)