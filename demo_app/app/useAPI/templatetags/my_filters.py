from django import template
from django.template.defaultfilters import register

@register.filter(name='get_item')
def get_item(dictionary, index):
    if index in dictionary:
        return dictionary[index]
    return ''