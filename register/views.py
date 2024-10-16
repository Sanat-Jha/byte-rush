from django.conf import settings
from django.shortcuts import render
from .models import Participants
from submissions.models import SiteSetting
from django.core.mail import EmailMessage
# Create your views here.

thankyouemailhtml = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thank You for Registering</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            color: #333;
        }
        .container {
            width: 100%;
            max-width: 600px;
            margin: auto;
            background-color: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #4CAF50;
            text-align: center;
        }
        p {
            font-size: 1.2rem;
            line-height: 1.5;
        }
        .footer {
            text-align: center;
            margin-top: 20px;
            font-size: 0.9rem;
            color: #777;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Thank You for Registering!</h1>
        <p>Dear [Participant Name],</p>
        <p>Thank you for registering for Byte Rush! We are excited to have you on board. Your participation will make this event even more special.</p>
        <p>Please keep an eye on your inbox for further details regarding the event schedule, venue, and other important information.</p>
        <p>If you have any questions or need assistance, feel free to reach out to us at <a href="mailto:support@example.com">support@example.com</a>.</p>
        <p>Looking forward to seeing you at the event!</p>
        <p>Best Regards,<br>The Byte Rush Team</p>
        
        <div class="footer">
            <p>© 2024 Byte Rush. All rights reserved.</p>
        </div>
    </div>
</body>
</html>

"""
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
                "text":"This Form number is already registered.",
                "show":SiteSetting.objects.get(key="Registrations").value
            }
            return render(request,"Register.html",context)
        newpart = Participants(name=name,email=email,form_number=formNumber)
        newpart.save()
        email = EmailMessage(
        subject='Thanks for registering in ByteRush',
        body=thankyouemailhtml,
        from_email=settings.EMAIL_HOST_USER,
        to=[email],
        )
        email.content_subtype = "html"
        email.send(fail_silently=False)
        
        context = {
                "mssg":True,
                "text":"Successfully Registered. Happy Coding.",
                "show":SiteSetting.objects.get(key="Registrations").value
            }
        return render(request,"Register.html",context)

    return render(request,"Register.html",context)