import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mystudentnew.settings'
import django
django.setup()

from studentnew1.models import Student

def populate():
    students = [
        {'First_name': 'Dharini',
        'Last_name': 'K',
        'Register_number': 1001,
        },
        {'First_name': 'Deepa',
        'Last_name': 'S',
        'Register_number': 1002,
        }
    ]

    subjects = [
        {'Subject_code': 'CP01',
         'Subject_title': 'Machine Learning',
        },
        {'Subject_code': 'CP02',
         'Subject_title': 'Web Application Development'
        }
    ]

    for student in students:
        pass
        #s = add_student(student)
        #print (s)
    '''
    for subject in subjects:
        print (subject)
    '''

def add_student(student):
    s = Student.objects.get_or_create(student['First_name'], student['Last_name'], student[Register_number])[0]
    s.save()
    return s

populate()
