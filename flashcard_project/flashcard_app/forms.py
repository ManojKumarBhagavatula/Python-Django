from django import forms
from .models import Subject, FlashCard

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']

class FlashCardForm(forms.ModelForm):
    class Meta:
        model = FlashCard
        fields = ['question', 'answer']
