from django.template.loader import get_template

from django import template

register = template.Library()

def change_author_name(value, arg):
    if(arg == 'change'):
        value = 'Shakib'
        return value
    if(arg == 'title'):
        return value.title()
    
    
def show_courses():
    courses = [
            {"id": 1, "course": "c", "teacher": "rahim"},
            {"id": 2, "course": "java", "teacher": "john"},
            {"id": 3, "course": "python", "teacher": "alice"},
            {"id": 4, "course": "javascript", "teacher": "bob"},
            {"id": 5, "course": "html", "teacher": "emma"},
            {"id": 6, "course": "css", "teacher": "michael"},
            {"id": 7, "course": "php", "teacher": "olivia"},
            {"id": 8, "course": "sql", "teacher": "william"},
            {"id": 9, "course": "ruby", "teacher": "sophia"},
            {"id": 10, "course": "c++", "teacher": "james"}
    ]
    
    return {'courses': courses}

courses_template = get_template('bootstrap/courses.html')

register.filter('change_author_name', change_author_name)

register.inclusion_tag(courses_template)(show_courses)

