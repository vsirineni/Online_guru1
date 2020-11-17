# this tags are purely to use django built in functions in template - Apr 9 2020

from django import template

register = template.Library()


@register.filter(name='split')
def split(value, arg):
    return value.split(arg)

@register.filter
def for_user(enrollments, user):
    return enrollments.filter(username_id=user.id)