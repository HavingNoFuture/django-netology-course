from django import template


register = template.Library()

@register.filter
def format_color(value):
    if value:
        val = float(value)
        if val < 0:
            return 'green'
        if 1 < val <= 2:
            return 'orangered'
        if 2 < val <= 5:
            return 'red'
        if 5 < val:
            return 'darkred'
    return '-'

@register.filter
def format_colomn(value):
    if not value:
        return '-'
    return value
