from rest_framework.decorators import api_view
from rest_framework.response import Response
from courses.models import Course, Topic, Test, AnswerOption
from courses.serializers import (
    CourseSerializer, TopicSerializer, TestSerializer, AnswerOptionSerializer,
    CreateCourseSerializer, EditCourseSerializer, CreateTopicSerializer, EditTopicSerializer,
    CreateTestSerializer, EditTestSerializer, CreateAnswerOptionSerializer, EditAnswerOptionSerializer
)
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

@api_view(['GET'])
@permission_classes([AllowAny]) 
def get_course(request, courseId):
    try:
        course = Course.objects.get(id=courseId)
    except Course.DoesNotExist:
        return Response({'error': 'Course not found'}, status=404)
    
    course_serializer = CourseSerializer(course)
    return Response(course_serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny]) 
def get_topic(request, topicId):
    try:
        topic = Topic.objects.get(id=topicId)
    except Topic.DoesNotExist:
        return Response({'error': 'Topic not found'}, status=404)
    
    topic_serializer = TopicSerializer(topic)
    return Response(topic_serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny]) 
def list_courses(request):
    courses = Course.objects.all()
    courses_serializer = CourseSerializer(courses, many=True)
    return Response({'courses': courses_serializer.data})


@api_view(['POST'])
def create_course(request):
    serializer = CreateCourseSerializer(data=request.data)
    if serializer.is_valid():
        course = serializer.save()
        return Response({'message': 'Course created successfully!', 'courseId': course.id})
    return Response({'errors': serializer.errors}, status=400)


@api_view(['PUT'])
def edit_course(request, courseId):
    try:
        course = Course.objects.get(id=courseId)
    except Course.DoesNotExist:
        return Response({'error': 'Course not found'}, status=404)
    
    serializer = EditCourseSerializer(course, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Course updated successfully!'})
    return Response({'errors': serializer.errors}, status=400)


@api_view(['DELETE'])
def delete_course(request, courseId):
    try:
        course = Course.objects.get(id=courseId)
    except Course.DoesNotExist:
        return Response({'error': 'Course not found'}, status=404)
    
    course.topics.all().delete()
    course.delete()
    return Response({'message': 'Course and its related topics, tests, and answer options deleted successfully!'})


@api_view(['POST'])
def create_topic(request, courseId):
    try:
        course = Course.objects.get(id=courseId)
    except Course.DoesNotExist:
        return Response({'error': 'Course not found'}, status=404)
    
    serializer = CreateTopicSerializer(data=request.data)
    if serializer.is_valid():
        topic = serializer.save(course=course)
        return Response({'message': 'Topic created successfully!', 'topic_id': topic.id})
    return Response({'errors': serializer.errors}, status=400)


@api_view(['PUT'])
def edit_topic(request, topicId):
    try:
        topic = Topic.objects.get(id=topicId)
    except Topic.DoesNotExist:
        return Response({'error': 'Topic not found'}, status=404)
    
    serializer = EditTopicSerializer(topic, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Topic updated successfully!'})
    return Response({'errors': serializer.errors}, status=400)


@api_view(['DELETE'])
def delete_topic(request, topicId):
    try:
        topic = Topic.objects.get(id=topicId)
    except Topic.DoesNotExist:
        return Response({'error': 'Topic not found'}, status=404)
    
    topic.tests.all().delete()
    topic.delete()
    return Response({'message': 'Topic and its related tests and answer options deleted successfully!'})


@api_view(['POST'])
def create_test(request, topicId):
    try:
        topic = Topic.objects.get(id=topicId)
    except Topic.DoesNotExist:
        return Response({'error': 'Topic not found'}, status=404)
    
    serializer = CreateTestSerializer(data=request.data)
    if serializer.is_valid():
        test = serializer.save(topic=topic)
        return Response({'message': 'Test created successfully!', 'test_id': test.id})
    return Response({'errors': serializer.errors}, status=400)


@api_view(['GET'])
def get_test(request, testId):
    try:
        test = Test.objects.get(id=testId)
    except Test.DoesNotExist:
        return Response({'error': 'Test not found'}, status=404)
    
    test_serializer = TestSerializer(test)
    return Response(test_serializer.data)


@api_view(['PUT'])
def edit_test(request, testId):
    try:
        test = Test.objects.get(id=testId)
    except Test.DoesNotExist:
        return Response({'error': 'Test not found'}, status=404)
    
    serializer = EditTestSerializer(test, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Test updated successfully!'})
    return Response({'errors': serializer.errors}, status=400)


@api_view(['DELETE'])
def delete_test(request, testId):
    try:
        test = Test.objects.get(id=testId)
    except Test.DoesNotExist:
        return Response({'error': 'Test not found'}, status=404)
    
    test.answer_options.all().delete()
    test.delete()
    return Response({'message': 'Test and its related answer options deleted successfully!'})


@api_view(['POST'])
def create_answer_option(request, testId):
    try:
        test = Test.objects.get(id=testId)
    except Test.DoesNotExist:
        return Response({'error': 'Test not found'}, status=404)
    
    serializer = CreateAnswerOptionSerializer(data=request.data)
    if serializer.is_valid():
        answer_option = serializer.save(test=test)
        return Response({'message': 'Answer option created successfully!', 'answer_option_id': answer_option.id})
    return Response({'errors': serializer.errors}, status=400)


@api_view(['GET'])
def get_answer_option(request, answerId):
    try:
        answer_option = AnswerOption.objects.get(id=answerId)
    except AnswerOption.DoesNotExist:
        return Response({'error': 'Answer option not found'}, status=404)
    
    answer_option_serializer = AnswerOptionSerializer(answer_option)
    return Response(answer_option_serializer.data)


@api_view(['PUT'])
def edit_answer_option(request, answerId):
    try:
        answer_option = AnswerOption.objects.get(id=answerId)
    except AnswerOption.DoesNotExist:
        return Response({'error': 'Answer option not found'}, status=404)
    
    serializer = EditAnswerOptionSerializer(answer_option, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Answer option updated successfully!'})
    return Response({'errors': serializer.errors}, status=400)


@api_view(['DELETE'])
def delete_answer_option(request, answerId):
    try:
        answer_option = AnswerOption.objects.get(id=answerId)
    except AnswerOption.DoesNotExist:
        return Response({'error': 'Answer option not found'}, status=404)
    
    answer_option.delete()
    return Response({'message': 'Answer option deleted successfully!'})
