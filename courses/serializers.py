from rest_framework import serializers
from courses.models import Course, Topic, Test, AnswerOption

class AnswerOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerOption
        fields = ['id', 'text', 'is_correct']


class TestSerializer(serializers.ModelSerializer):
    answer_options = AnswerOptionSerializer(many=True)

    class Meta:
        model = Test
        fields = ['id', 'question_text', 'answer_options']


class TopicSerializer(serializers.ModelSerializer):
    tests = TestSerializer(many=True)
    courseId = serializers.IntegerField(source='course.id', read_only=True)

    class Meta:
        model = Topic
        fields = ['id', 'title', 'description', 'courseId', 'tests']


class CourseSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'teacher_name', 'price', 'subject', 'topics']


class CreateCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'description', 'teacher_name', 'price', 'subject']


class EditCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'description', 'teacher_name', 'price', 'subject']


class CreateTopicSerializer(serializers.ModelSerializer):
    course_id = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), source='course')

    class Meta:
        model = Topic
        fields = ['courseId', 'title', 'description']


class EditTopicSerializer(serializers.ModelSerializer):
    courseId = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), source='course', required=False)

    class Meta:
        model = Topic
        fields = ['courseId', 'title', 'description']


class CreateTestSerializer(serializers.ModelSerializer):
    topic_id = serializers.PrimaryKeyRelatedField(queryset=Topic.objects.all(), source='topic')

    class Meta:
        model = Test
        fields = ['topicId', 'question_text']


class EditTestSerializer(serializers.ModelSerializer):
    topic_id = serializers.PrimaryKeyRelatedField(queryset=Topic.objects.all(), source='topic', required=False)

    class Meta:
        model = Test
        fields = ['topicId', 'question_text']


class CreateAnswerOptionSerializer(serializers.ModelSerializer):
    test_id = serializers.PrimaryKeyRelatedField(queryset=Test.objects.all(), source='test')

    class Meta:
        model = AnswerOption
        fields = ['testId', 'text', 'is_correct']


class EditAnswerOptionSerializer(serializers.ModelSerializer):
    test_id = serializers.PrimaryKeyRelatedField(queryset=Test.objects.all(), source='test', required=False)

    class Meta:
        model = AnswerOption
        fields = ['testId', 'text', 'is_correct']
