from django import template

register = template.Library()


@register.filter
def classname(obj):
    return obj.__class__.__name__


@register.filter
def list_stars(value):
    return ["x" for i in range(value)] + ["o" for i in range(5 - value)]
