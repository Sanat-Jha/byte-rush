from django.shortcuts import render
from register.models import Participants

# Create your views here.
def leaderboard(request):
    # Dummy participants data
    participants = Participants.objects.order_by('-score')
    return render(request, 'leaderboard.html', {'participants': participants})