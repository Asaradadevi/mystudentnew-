from django import forms
from studentnew1.models import Student, Mark

class StudentForm(forms.ModelForm):
    First_name = forms.CharField(max_length = 80, help_text = "Enter the name: ")
    Register_number = forms.IntegerField(initial = 1001, help_text = "Enter the register number: ")


    class Meta:
        model = Student
        fields = ['First_name', 'Register_number']

class MarkForm(forms.ModelForm):
    Subject_title = forms.CharField(max_length = 120, help_text = "Enter the subject title: ")
    cat1_mark = forms.IntegerField(initial = 0, help_text = "Enter the cat1 mark: ")
    cat2_mark = forms.IntegerField(initial = 0, help_text = "Enter the cat2 mark: ")
    cat3_mark = forms.IntegerField(initial = 0, help_text = "Enter the cat3 mark: ")

    class Meta:
        model = Mark
        fields = ['Subject_title', 'cat1_mark','cat2_mark','cat3_mark']
