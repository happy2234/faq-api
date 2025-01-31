from django.contrib import admin
from .models import FAQ
from ckeditor.widgets import CKEditorWidget
from django import forms

class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = '__all__'
        widgets = {f.answer: CKEditorWidget() for f in FAQ._meta.get_fields() if 'answer_' in f.name}

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    form = FAQForm
    list_display = ('question_en', 'id')
    fieldsets = [
        (lang.upper(), {'fields': [f'question_{lang}', f'answer_{lang}']}) 
        for lang in ['en', 'hi', 'bn']
    ]