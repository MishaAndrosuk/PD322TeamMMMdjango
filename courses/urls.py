from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.list_courses, name='courses'),
    path('course/topics/', views.get_course, name='topics'),
    path('topic/tests', views.get_topic, name='tests'),
    path('create/course/', views.create_course, name='create_course'),
    path('create/topic/', views.create_topic, name='create_topic'),
    path('create/test/', views.create_test, name='create_test'),
    path('create/answer_option/', views.create_answer_option, name='create_answer_option'),
    path('create/test/answer_option/', views.create_test_with_answers, name='create_test_with_answers'),
    path('edit/course/', views.edit_course, name='edit_course'),
    path('edit/topic/', views.edit_topic, name='edit_topic'),
    path('edit/test/', views.edit_test, name='edit_test'),
    path('edit/answer_option/', views.edit_answer_option, name='edit_answer_option'),
    path('delete/course/', views.delete_course, name='delete_course'),
    path('delete/topic/', views.delete_topic, name='delete_topic'),
    path('delete/test/', views.delete_test, name='delete_test'),
    path('delete/answer_option/', views.delete_answer_option, name='delete_answer_option'),
]