from django import template

register = template.Library()

def change_author_name(value, arg):
    if(arg == 'change'):
        value = 'Shakib'
        return value
    if(arg == 'title'):
        return value.title()


register.filter('change_author_name', change_author_name)