from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()

@register.filter
def format_decimal(value):
    if value is None:
        return ""
    if value == int(value):
        return intcomma(int(value))
    else:
        return intcomma(f"{value:,.2f}")
