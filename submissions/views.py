from django.conf import settings
from django.shortcuts import render
from .models import Submission,Participants
from datetime import datetime
from submissions.models import SiteSetting
from django.core.mail import EmailMessage


thankyouemailhtml = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ByteRush - Submission Successful</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #333333;
            font-size: 24px;
            text-align: center;
        }
        p {
            color: #666666;
            line-height: 1.6;
            font-size: 16px;
        }
        .btn {
            display: inline-block;
            margin: 20px auto;
            padding: 12px 24px;
            background-color: #007bff;
            color: white;
            text-align: center;
            text-decoration: none;
            border-radius: 5px;
            font-size: 16px;
            font-weight: bold;
        }
        .footer {
            margin-top: 30px;
            text-align: center;
            font-size: 14px;
            color: #aaaaaa;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Project Submission Successful!</h1>
        <p>Dear Participant,</p>
        <p>Congratulations! Your project has been successfully submitted for ByteRush. We are thrilled to have you on board, and we can't wait to see your amazing work.</p>
        <p>Your hard work and dedication are truly appreciated. If you have any further updates or wish to review your submission, feel free to log in to your account using the link below.</p>
        <a href="https://byterush.example.com/login" class="btn">View Submission</a>
        <p>Best of luck, and we look forward to seeing your innovative project in action!</p>
        <p>Kind regards,</p>
        <p>The ByteRush Team</p>
        <div class="footer">
            <p>ByteRush Hackathon | IIT Roorkee</p>
        </div>
    </div>
</body>
</html>

"""
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
                "text":"This Form number is not registered in the competiton. Please register before submitting your project.",
                "show":SiteSetting.objects.get(key="Submissions").value
            }
            return render(request,"submission.html",context)
        participant= participants[0]
        githubRepo = request.POST.get("githubRepo")
        problemStatement = request.POST.get("problemStatement")
        current_date = datetime.now().date()
        if len(list(Submission.objects.filter(participant=participant,date=current_date))) != 0:
            context = {
                "mssg":"True",
                "text":"This Form number has already submitted for today.",
                "show":SiteSetting.objects.get(key="Submissions").value
            }
            return render(request,"submission.html",context)
        newsubmission = Submission(githuburl=githubRepo,problemStatement=problemStatement,participant=participant,date=current_date)
        newsubmission.save()
        email = EmailMessage(
        subject='Submissions completed.',
        body=thankyouemailhtml,
        from_email=settings.EMAIL_HOST_USER,
        to=[email],
        )
        email.content_subtype = "html"
        email.send(fail_silently=False)
        
        context = {
                "mssg":True,
                "text":"Successfully Submitted",
                "show":SiteSetting.objects.get(key="Submissions").value
            }
        return render(request,"submission.html",context)

    return render(request,"submission.html",context)