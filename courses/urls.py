from django.urls import path
from . import views

urlpatterns = [
    path("buy/", views.buy_course),
    path("has_purchased/<int:student_id>/<int:course_id>/", views.has_purchased),
    path('courses/', views.list_courses, name='courses'),
    path('course/<int:courseId>/topics/', views.get_course, name='topics'),
    path('topic/<int:topicId>/tests', views.get_topic, name='tests'),
    path('test/<int:testId>/answers', views.get_test, name='answers'),
    path('create/course/', views.create_course, name='create_course'),
    path('create/topic/<int:courseId>', views.create_topic, name='create_topic'),
    path('create/test/<int:topicId>', views.create_test, name='create_test'),
    path('create/answer/<int:testId>', views.create_answer_option, name='create_answer'),
    path('edit/course/<int:courseId>', views.edit_course, name='edit_course'),
    path('edit/topic/<int:topicId>', views.edit_topic, name='edit_topic'),
    path('edit/test/<int:testId>', views.edit_test, name='edit_test'),
    path('edit/answer/<int:answerId>', views.edit_answer_option, name='edit_answer'),
    path('delete/course/<int:courseId>', views.delete_course, name='delete_course'),
    path('delete/topic/<int:topicId>', views.delete_topic, name='delete_topic'),
    path('delete/test/<int:testId>', views.delete_test, name='delete_test'),
    path('delete/answer/<int:answerId>', views.delete_answer_option, name='delete_answer'),
]