from django.shortcuts import render
from django.http import JsonResponse
import json
from datetime import datetime
from submissions.models import Submission,SiteSetting
from register.models import Participants
# Create your views here.
def dashboard(request):
    unique_dates = list(Submission.objects.dates('date',"day", order='ASC'))
    context = {
        "Dates":unique_dates,
        "Submissions":SiteSetting.objects.get(key="Submissions").value,
        "Registrations":SiteSetting.objects.get(key="Registrations").value,
        "password":"password"
    }

    if request.method == "POST":
        context["submissions"] = list(Submission.objects.filter(date=request.POST.get("date")))
    else:
        context["submissions"] = list(Submission.objects.all())
    return render(request, "dashboard.html",context)


def submitscore(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            form_number = data['formNumber']
            date = data['date']
            score = data['score']
            print(score)
            date_obj = datetime.strptime(date, '%d/%m/%Y').date()
            print(date)
            participant = Participants.objects.get(form_number=form_number)
            print(participant)
            project = Submission.objects.filter(participant=participant,date=date_obj)[0]
            print(project)
            project.score = score
            project.save()
            
            # Logic to find the specific submission using form_number and date
            # For example, query the submission model by form_number and date, then update the score
            # submission = Submission.objects.get(form_number=form_number, date=date)
            # submission.score = score
            # submission.save()

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})
def toggle_registration(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            open = data['open']
            registrations = SiteSetting.objects.get(key="Registrations")
            registrations.value = open
            registrations.save()

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})
def toggle_submission(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            open = data['open']
            submission = SiteSetting.objects.get(key="Submissions")
            submission.value = open
            submission.save()

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})
