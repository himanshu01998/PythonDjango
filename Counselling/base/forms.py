from django.db import models
from django.db.models import fields
from django.forms.models import ModelForm
from . models import course, applyforcourse
from django.contrib.auth.models import User

class courseForm(ModelForm):
    class Meta:
        model = course
        fields = '__all__'
        exclude = ['user', 'course_isactive']

class courseFormEdit(ModelForm):
    class Meta:
        model = course
        fields = '__all__'
        exclude = ['user']

class userFormEdit(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'groups', 'is_staff', 'is_active']

class applyForm(ModelForm):
    class Meta:
        model = applyforcourse
        fields = ['accepted']