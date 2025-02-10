from django.db import models

# Модель Курс
class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    teacher_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    subject = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
    
# Модель Тема
class Topic(models.Model):
    course = models.ForeignKey(Course, related_name='topics', on_delete=models.CASCADE) 
    title = models.CharField(max_length=200) 
    description = models.TextField()

    def __str__(self):
        return self.title

# Модель Тест
class Test(models.Model):
    topic = models.ForeignKey(Topic, related_name='tests', on_delete=models.CASCADE)
    question_text = models.TextField()

    def __str__(self):
        return f"Test {self.topic.title}"

# Модель Варіант відповіді
class AnswerOption(models.Model):
    test = models.ForeignKey(Test, related_name='answer_options', on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
