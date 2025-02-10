from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from courses.models import Course, Topic, Test, AnswerOption
from courses.forms.create import CreateCourse, CreateTopic, CreateTest, CreateAnswerOption
from courses.forms.edit import EditCourse, EditTopic, EditTest, EditAnswerOption

@api_view(['GET'])
def get_course(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response({'error': 'Course not found'}, status=404)
    
    topics_data = []
    for topic in course.topics.all():
        topics_data.append({
            'title': topic.title,
            'description': topic.description
        })

    return Response({
        'course_name': course.name,
        'description': course.description,
        'created_at': course.created_at,
        'teacher_name': course.teacher_name,
        'price': course.price,
        'subject': course.subject,
        'topics': topics_data
    })

@api_view(['GET'])
def get_topic(request, topic_id):
    try:
        topic = Topic.objects.get(id=topic_id)
    except Topic.DoesNotExist:
        return Response({'error': 'Topic not found'}, status=404)
    
    test_count = topic.tests.count()
    tests_data = []
    for test in topic.tests.all():
        answer_options = [{'text': option.text, 'is_correct': option.is_correct} for option in test.answer_options.all()]
        tests_data.append({
            'question': test.question_text,
            'answer_options': answer_options
        })

    return Response({
        'topic_title': topic.title,
        'description': topic.description,
        'tests': tests_data,
        'test_count': test_count
    })

@api_view(['GET'])
def list_courses(request):
    courses = Course.objects.all()
    courses_data = []
    for course in courses:
        courses_data.append({
            'course_name': course.name,
            'price': course.price,
            'subject': course.subject,
            'created_at': course.created_at,
            'topic_count': course.topics.count()
        })

    return Response({'courses': courses_data})

@api_view(['POST'])
def create_course(request):
    form = CreateCourse(request.data)
    if form.is_valid():
        course = form.save()
        return Response({'message': 'Course created successfully!', 'course_id': course.id})
    return Response({'errors': form.errors}, status=400)

@api_view(['PUT'])
def edit_course(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response({'error': 'Course not found'}, status=404)
    
    form = EditCourse(request.data, instance=course)
    if form.is_valid():
        form.save()
        return Response({'message': 'Course updated successfully!'})
    return Response({'errors': form.errors}, status=400)

@api_view(['DELETE'])
def delete_course(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response({'error': 'Course not found'}, status=404)

    course.topics.all().delete()
    course.delete()

    return Response({'message': 'Course and its related topics, tests, and answer options deleted successfully!'})

@api_view(['POST'])
def create_topic(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response({'error': 'Course not found'}, status=404)
    
    form = CreateTopic(request.data)
    if form.is_valid():
        topic = form.save(commit=False)
        topic.course = course
        topic.save()
        return Response({'message': 'Topic created successfully!', 'topic_id': topic.id})
    return Response({'errors': form.errors}, status=400)

@api_view(['PUT'])
def edit_topic(request, topic_id):
    try:
        topic = Topic.objects.get(id=topic_id)
    except Topic.DoesNotExist:
        return Response({'error': 'Topic not found'}, status=404)
    
    form = EditTopic(request.data, instance=topic)
    if form.is_valid():
        form.save()
        return Response({'message': 'Topic updated successfully!'})
    return Response({'errors': form.errors}, status=400)

@api_view(['DELETE'])
def delete_topic(request, topic_id):
    try:
        topic = Topic.objects.get(id=topic_id)
    except Topic.DoesNotExist:
        return Response({'error': 'Topic not found'}, status=404)
    
    topic.tests.all().delete()
    topic.delete()

    return Response({'message': 'Topic and its related tests and answer options deleted successfully!'})

@api_view(['POST'])
def create_test(request, topic_id):
    try:
        topic = Topic.objects.get(id=topic_id)
    except Topic.DoesNotExist:
        return Response({'error': 'Topic not found'}, status=404)
    
    form = CreateTest(request.data)
    if form.is_valid():
        test = form.save(commit=False)
        test.topic = topic
        test.save()
        return Response({'message': 'Test created successfully!', 'test_id': test.id})
    return Response({'errors': form.errors}, status=400)

@api_view(['PUT'])
def edit_test(request, test_id):
    try:
        test = Test.objects.get(id=test_id)
    except Test.DoesNotExist:
        return Response({'error': 'Test not found'}, status=404)
    
    form = EditTest(request.data, instance=test)
    if form.is_valid():
        form.save()
        return Response({'message': 'Test updated successfully!'})
    return Response({'errors': form.errors}, status=400)

@api_view(['DELETE'])
def delete_test(request, test_id):
    try:
        test = Test.objects.get(id=test_id)
    except Test.DoesNotExist:
        return Response({'error': 'Test not found'}, status=404)
    
    test.answer_options.all().delete()
    test.delete()

    return Response({'message': 'Test and its related answer options deleted successfully!'})

@api_view(['POST'])
def create_test_with_answers(request, topic_id):
    try:
        topic = Topic.objects.get(id=topic_id)
    except Topic.DoesNotExist:
        return Response({'error': 'Topic not found'}, status=404)
    
    test_data = request.data.get('test')
    answer_options_data = request.data.get('answer_options', [])
    
    test_form = CreateTest(test_data)
    if test_form.is_valid():
        test = test_form.save(commit=False)
        test.topic = topic
        test.save()

        for option_data in answer_options_data:
            answer_option_form = CreateAnswerOption(option_data)
            if answer_option_form.is_valid():
                answer_option = answer_option_form.save(commit=False)
                answer_option.test = test
                answer_option.save()
        
        return Response({'message': 'Test and answer options created successfully!', 'test_id': test.id})
    
    return Response({'errors': test_form.errors}, status=400)

@api_view(['POST'])
def create_answer_option(request, test_id):
    try:
        test = Test.objects.get(id=test_id)
    except Test.DoesNotExist:
        return Response({'error': 'Test not found'}, status=404)
    
    form = CreateAnswerOption(request.data)
    if form.is_valid():
        answer_option = form.save(commit=False)
        answer_option.test = test
        answer_option.save()
        return Response({'message': 'Answer option created successfully!', 'answer_option_id': answer_option.id})
    return Response({'errors': form.errors}, status=400)

@api_view(['PUT'])
def edit_answer_option(request, answer_option_id):
    try:
        answer_option = AnswerOption.objects.get(id=answer_option_id)
    except AnswerOption.DoesNotExist:
        return Response({'error': 'Answer option not found'}, status=404)
    
    form = EditAnswerOption(request.data, instance=answer_option)
    if form.is_valid():
        form.save()
        return Response({'message': 'Answer option updated successfully!'})
    return Response({'errors': form.errors}, status=400)

@api_view(['DELETE'])
def delete_answer_option(request, answer_option_id):
    try:
        answer_option = AnswerOption.objects.get(id=answer_option_id)
    except AnswerOption.DoesNotExist:
        return Response({'error': 'Answer option not found'}, status=404)
    
    answer_option.delete()
    return Response({'message': 'Answer option deleted successfully!'})
