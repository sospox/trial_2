from django.forms import ModelForm
from .models import Language,Translation,TranslationHistory

class LanguageForm(ModelForm):
    class Meta:
        model = Language
        fields ='__all__'
        
class TranslationForm(ModelForm):
    class Meta:
        model = Translation
        fields ='__all__'

class TranslationHistoryForm(ModelForm):
    class Meta:
        model = TranslationHistory
        fields ='__all__'
