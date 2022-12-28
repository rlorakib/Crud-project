from django import forms
from . import models



class StudentForm(forms.ModelForm):
    class Meta:
        model = models.student
        fields = "__all__"