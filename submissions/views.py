from django.shortcuts import render
from .models import Submission,Participants
from datetime import datetime
from submissions.models import SiteSetting



# Create your views here.
def submission(request):
    context = {
        "mssg":False,
        "show":SiteSetting.objects.get(key="Submissions").value
    }
    if request.method == "POST":
        participants = list(Participants.objects.filter(form_number=request.POST.get("formNumber")))
        if len(participants) == 0:
            context = {
                "mssg":"True",
                "text":"This Form number is not registered in the competiton. Please register before submitting your project."
            }
            return render(request,"submission.html",context)
        participant= participants[0]
        githubRepo = request.POST.get("githubRepo")
        problemStatement = request.POST.get("problemStatement")
        current_date = datetime.now().date()
        if len(list(Submission.objects.filter(participant=participant,date=current_date))) != 0:
            context = {
                "mssg":"True",
                "text":"This Form number has already submitted for today."
            }
            return render(request,"submission.html",context)
        newsubmission = Submission(githuburl=githubRepo,problemStatement=problemStatement,participant=participant,date=current_date)
        newsubmission.save()
        
        context = {
                "mssg":True,
                "text":"Successfully Submitted"
            }
        return render(request,"submission.html",context)

    return render(request,"submission.html",context)