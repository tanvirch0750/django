from django_model.models import Student

from django import forms


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        # fields = ['name', 'roll']
        # exclude = ['roll']
        labels = {
            'name': 'Student Name',
            'roll': 'Student Roll',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-class'}),
            # 'roll': forms.PasswordInput()
        }
        help_texts = {
            'name': 'Write your full name'
        }
        error_messages = {
            'name': {'required': 'Your name is required'}
        }
        