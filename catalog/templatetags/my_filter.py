import os.path

from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

from config.settings import MEDIA_URL

register = template.Library()


@register.filter(needs_autoescape=True)
def mediapath(path, autoescape=True):
    return MEDIA_URL + str(path)


@register.simple_tag
def mediapath(path):
    return MEDIA_URL + str(path)
