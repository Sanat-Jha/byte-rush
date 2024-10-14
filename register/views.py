from django.shortcuts import render
from .models import Participants
from submissions.models import SiteSetting
# Create your views here.
def newregister(request):
    context = {
        "mssg":False,
        "show":SiteSetting.objects.get(key="Registrations").value
    }
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        formNumber = request.POST.get("formNumber")
        if len(list(Participants.objects.filter(form_number=formNumber))) != 0:
            context = {
                "mssg":"True",
                "text":"This Form number is already registered."
            }
            return render(request,"Register.html",context)
        newpart = Participants(name=name,email=email,form_number=formNumber)
        newpart.save()
        
        context = {
                "mssg":True,
                "text":"Successfully Registered. Happy Coding."
            }
        return render(request,"Register.html",context)

    return render(request,"Register.html",context)