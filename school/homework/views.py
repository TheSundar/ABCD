from django.shortcuts import render
from django.http import HttpResponse
from models import HomeWork
import json
import string
import random

def homework_description(request, student_name, class_name):
    print "st, class",student_name, class_name
    db_value = HomeWork.objects.filter(student_name=student_name).filter(student_class=class_name).values('school_name',
                                                                             'student_name','student_class',
                                                                             'student_hw_sub1','student_hw_sub2',
                                                                             'student_hw_sub3','student_hw_sub4',
                                                                            'student_hw_sub5','student_hw_sub6')
    # chars = string.ascii_lowercase + string.digits
    # for i in range(100):
    #     obj = HomeWork()
    #     obj.school_name = ''.join(random.choice(string.ascii_uppercase) for _ in range(10))
    #     obj.student_name = ''.join(random.choice(string.ascii_uppercase) for _ in range(10))
    #     obj.student_class = ''.join(random.choice(chars) for _ in range(10))
    #     obj.student_hw_sub1 = ''.join(random.choice(chars) for _ in range(250))
    #     obj.student_hw_sub2 = ''.join(random.choice(chars) for _ in range(300))
    #     obj.student_hw_sub3 = ''.join(random.choice(chars) for _ in range(400))
    #     obj.student_hw_sub4 = ''.join(random.choice(chars) for _ in range(250))
    #     obj.student_hw_sub5 = ''.join(random.choice(chars) for _ in range(360))
    #     obj.student_hw_sub6 = ''.join(random.choice(chars) for _ in range(570))
    #     obj.save()

    #db_value = HomeWork.objects.filter(student_name='Sumangala')
    #print "data----",db_value

    #context = {'status':True, 'homework':json.dumps(db_value[0])}
    #return render(request,'homework/homework.html',context)
    return HttpResponse(json.dumps(db_value[0]), content_type='application/json')