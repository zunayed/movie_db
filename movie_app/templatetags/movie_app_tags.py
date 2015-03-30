from random import randint
from django import template

register = template.Library()

@register.assignment_tag()
def random_avatar_color():
    """
    Create a random integer for avatar colors
    css library has 215 different colors
    """
    return randint(0, 215)
