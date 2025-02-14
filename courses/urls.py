from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.list_courses, name='courses'),
    path('course/<int:id>/topics/', views.get_course, name='topics'),
    path('topic/<int:id>/tests', views.get_topic, name='tests'),
    path('create/course/', views.create_course, name='create_course'),
    path('create/topic/<int:courseId>', views.create_topic, name='create_topic'),
    path('create/test/<int:id>', views.create_test, name='create_test'),
    path('create/answer/<int:id>', views.create_answer_option, name='create_answer'),
    path('edit/course/<int:id>', views.edit_course, name='edit_course'),
    path('edit/topic/<int:id>', views.edit_topic, name='edit_topic'),
    path('edit/test/<int:id>', views.edit_test, name='edit_test'),
    path('edit/answer/<int:id>', views.edit_answer_option, name='edit_answer'),
    path('delete/course/<int:id>', views.delete_course, name='delete_course'),
    path('delete/topic/<int:id>', views.delete_topic, name='delete_topic'),
    path('delete/test/<int:id>', views.delete_test, name='delete_test'),
    path('delete/answer/<int:id>', views.delete_answer_option, name='delete_answer'),
]