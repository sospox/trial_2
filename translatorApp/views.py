from django.shortcuts import render, retrieve
from deep_translator import GoogleTranslator
# Create your views here.
def home(request):
    text = "" 
    translated_text = ""
    languages = GoogleTranslator().get_supported_languages(as_dict=True)

   

    if request.method == "POST":
        text = request.POST.get("text")
        language = request.POST.get("language")
        

        if text and language:
            translated_text = GoogleTranslator(target = language).translate(text)
            translated_text = str(translated_text)
    context = {"translated_text": translated_text,"languages": languages, "text": text }
    return render(request ,"translatorApp/home.html",context)
