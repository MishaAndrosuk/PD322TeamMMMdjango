from django import forms
from courses.models import Course, Topic, Test, AnswerOption
import datetime

class CreateCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"

    def clean_name(self):
        teacher_name = self.cleaned_data.get("teacher_name")
        if not all(x.isalpha() or x.isspace() for x in teacher_name):
            raise forms.ValidationError("Name of teacher must contain only letters.")
        return teacher_name

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price <= 0:
            raise forms.ValidationError("Price must be a positive number.")
        return price

    def clean_created_at(self):
        created_at = self.cleaned_data.get("created_at")
        if created_at and created_at > datetime.datetime.now():
            raise forms.ValidationError("Date cannot be greater than the current date.")
        return created_at
    
class CreateTopic(forms.ModelForm):
    class Meta:
        model = Topic
        fields = "__all__"
        
class CreateTest(forms.ModelForm):
    class Meta:
        model = Test
        fields = "__all__"

class CreateAnswerOption(forms.ModelForm):
    class Meta:
        model = AnswerOption
        fields = "__all__"