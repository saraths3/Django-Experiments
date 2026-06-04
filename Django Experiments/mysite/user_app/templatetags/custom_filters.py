from django import template

register = template.Library()

@register.filter
def mul(value, arg):
    return float(value) * int(arg)

@register.filter
def format_currency(value):
    return f"₹{float(value):.2f}"
