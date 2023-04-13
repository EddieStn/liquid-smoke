from django import template

register = template.Library()


@register.filter
def make_range(value, start=1):
    return range(start, value+1)


@register.filter
def multiply(value, arg):
    return value * arg
