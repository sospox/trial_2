from django.contrib import admin
from . models import Language, Translation, TranslationHistory

# Register your models here.
admin.site.register(Language)
admin.site.register(Translation)
admin.site.register(TranslationHistory)
