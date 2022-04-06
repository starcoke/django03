from django.shortcuts import render
import googletrans
from googletrans import Translator

# Create your views here.
def index(request):
            
    context = {
        "ncode" : googletrans.LANGUAGES
        }
    if request.method == "POST":
        bf = request.POST.get("bf")
        fr = request.POST.get("fr")
        to = request.POST.get("to")

        if bf:
            translator = Translator()
            tr = translator.translate(bf, src=fr, dest=to)
            context.update({
                "af" : tr.text,
                "bf" : bf,
                "fr" : fr,
                "to" : to
            })
    return render(request, "trans/index.html", context)