from django import template

register = template.Library()


@register.filter
def make_range(number):
    return range(number)
