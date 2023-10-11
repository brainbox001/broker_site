from django import template

register = template.Library()

@register.filter
def range(value):
    return range(value)


@register.filter
def titlecase(value):
    return value.title()


