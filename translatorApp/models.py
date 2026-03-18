from django.db import models
from django.contrib.auth.models import User



# Create your models here.
from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Translation(models.Model):
    source_language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name="source")
    target_language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name="target")
    original_text = models.TextField()
    translated_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.original_text} -> {self.translated_text}"


class TranslationHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    translation = models.ForeignKey(Translation, on_delete=models.CASCADE)
    used_at = models.DateTimeField(auto_now_add=True)