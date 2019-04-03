from django import template


register = template.Library()

@register.filter
def format_color(value):
    if value['key'] == 'Год':
        color = 'white'
    elif value['key'] == 'Суммарная':
        color = 'lightgrey'
    else: 
        
        if value['count'] == '-':
            color = 'white'
        elif value['count'] == 'Год':
            color = 'blue'
        elif value['count'] < 0:
            color = 'green' 
        elif value['count'] >= 1 and value['count'] < 2:
            color = 'orangered'
        elif value['count'] >= 2 and value['count'] < 5:
            color = 'red'
        elif value['count'] >= 5:
            color = 'darkred'
        else:
            color = 'white'

    return '<li style="display: inline-block; width: 44px; background-color:{}">{}</li>'.format(color, value['count'])
