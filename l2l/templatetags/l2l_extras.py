from django import template
from datetime import datetime
from typing import Union

register = template.Library()

@register.filter
def l2l_dt(input: Union[datetime, str]):
    try:
        return input.strftime("%Y-%m-%dT%H:%M:%S")
    except AttributeError:
        try:
            return datetime.strptime(input, "%Y-%m-%dT%H:%M:%S")
        except ValueError:
            return 'Unexpected input to l2l_dt filter: expected as datetime.datetime object or ISO string'
