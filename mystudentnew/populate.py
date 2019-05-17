import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mystudentnew.settings'
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mystudentnew.settings')

import django
django.setup()

from studentnew1.models import Student,Subject,Mark

def populate():
    students = [
        {'First_name': 'Dharini',
        'Last_name': 'K',
        'Register_number': 1001,
        },
        {'First_name': 'Deepa',
        'Last_name': 'S',
        'Register_number': 1003,
        },
	{'First_name': 'jafrin',
        'Last_name': 'S',
        'Register_number': 1004,
        },
	{'First_name': 'Preethi',
        'Last_name': 'V',
        'Register_number': 1005,
        },
	{'First_name': 'Sarada',
        'Last_name': 'A',
        'Register_number': 1006,
        },
	{'First_name': 'Sarada',
        'Last_name': 'A',
        'Register_number': 1006,
        },
	{'First_name': 'Sivasalini',
        'Last_name': 'S',
        'Register_number': 1007,
        },
	{'First_name': 'Subhalakshmi',
        'Last_name': 'S',
        'Register_number': 1008,
        },
	{'First_name': 'Ushakumari',
        'Last_name': 'K',
        'Register_number': 1009,
        }
    ]

    subjects = [
        {'Subject_code': 'PCP1178',
         'Subject_title': 'Machine Learning',
        },
        {'Subject_code': 'PCP1102',
         'Subject_title': 'Network Design Technolgies',
        },
	{'Subject_code': 'PMA1177',
         'Subject_title': 'Applied Probability And Statistics',
        },
	{'Subject_code': 'PCP1101',
         'Subject_title': 'Multicore Architecture And GPU',
        },
	{'Subject_code': 'PCP1177',
         'Subject_title': 'Advanced Software Engineering',
        },
	{'Subject_code': 'PCP1176',
         'Subject_title': 'Advanced Data Structures And Algoritms',
        }
    ]
    marks = [
    {'First_name': 'Dharini','Subject_title': 'Machine Learning','cat1_mark':68,'cat2_mark':70,'cat3_mark':78,},


    {'First_name': 'Dharini','Subject_title': 'Network Design Technolgies','cat1_mark':84,'cat2_mark':80,'cat3_mark':73,},


    {'First_name': 'Dharini','Subject_title':'Applied Probability And Statistics','cat1_mark':82,'cat2_mark':67,'cat3_mark':90,},


    {'First_name': 'Dharini','Subject_title': 'Multicore Architecture And GPU','cat1_mark':88,'cat2_mark':80,'cat3_mark':74,},


    {'First_name': 'Dharini','Subject_title': 'Advanced Software Engineering','cat1_mark':69,'cat2_mark':71,'cat3_mark':76,},


    {'First_name': 'Dharini','Subject_title': 'Advanced Data Structures And Algoritms','cat1_mark':65,'cat2_mark':78,'cat3_mark':94,},

    ]


    for student in students:
        s = add_student(student)
        print (s)

    for subject in subjects:
        sub = add_subject(subject)
        print (sub)

    for mark in marks:
        m = add_mark(mark)
        print (m)


    '''
    for subject in subjects:
        print (student['First_name'], student['Last_name'], student['Register_number'])
    '''

def add_student(student):
    s = Student.objects.get_or_create(First_name=student['First_name'], Last_name=student['Last_name'], Register_number=student['Register_number'])[0]
    s.save()
    return s

def add_subject(subject):
    sub = Subject.objects.get_or_create(Subject_code=subject['Subject_code'], Subject_title=subject['Subject_title'])[0]
    sub.save()
    return sub

def add_mark(mark):
    m = Mark.objects.get_or_create(First_name=mark['First_name'],Subject_title=mark['Subject_title'],cat1_mark=mark['cat1_mark'],cat2_mark=mark['cat2_mark'],cat3_mark=mark['cat3_mark'])[0]
    #m = Mark.objects.get_or_create(cat1_mark=mark['cat1_mark'],cat2_mark=mark['cat2_mark'],cat3_mark=mark['cat3_mark'])[0]
    m.save()
    return m

populate()
