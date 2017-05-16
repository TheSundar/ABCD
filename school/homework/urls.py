from django.conf.urls import url
from . import views

urlpatterns=[
        url(r'(?P<student_name>\w+)/(?P<class_name>\w+)/$',views.homework_description, name="homework_description"),
]