from django import template
from datetime import timedelta
import datetime
import time

register = template.Library()

def create_datetime(tuple):
	return datetime.datetime(tuple[0], tuple[1], tuple[2], tuple[3], tuple[4], tuple[5])

@register.filter
def format_date(value):
	post_datetime = create_datetime(time.gmtime(value))
	delta = datetime.datetime.today() - post_datetime
	delta_minutes = delta.seconds % 3600
	delta_hours = delta.seconds // 3600

	if delta_minutes < 10:
		return 'только что'
	elif delta_minutes >= 10 and delta.days < 1 :
		return f'{delta_hours} часов назад'
	else:
		return post_datetime.date()


# необходимо добавить фильтр для поля `score`
@register.filter
def score_filter(score, default):
	if score:
		if score < -5:
			return 'все плохо'
		elif score >= -5 and score < 5:
			return 'нейтрально'
		else:
			return 'хорошо'
	else:
		return default


@register.filter
def format_num_comments(value):
    if value == 0:
    	return 'Оставьте комментарий'
    elif value > 0 and value < 50:
    	return value
    elif value >=50:
    	return '50+'


@register.filter
def format_selftext(text, count):
	result = text.split(' ')
	first = ' '.join(result[0 : count])
	last = ' '.join(result[len(result) - count : len(result)])
	result = f'{first} ... {last}'
	return result


