from .models import Pattern
from django import forms
from ckeditor.widgets import CKEditorWidget
class PatternForm(forms.ModelForm):
    
    # boss=forms.Select(Pattern.boss)
    class Meta:
        model= Pattern
        fields='__all__'
        labels ={
            'boss' : '레이드 보스',
            'mode' : '모드',
            'phase' : '페이즈',
            'guide' : False,
        }

