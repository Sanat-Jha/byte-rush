"""
URL configuration for byterush project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from dashboard.views import dashboard,submitscore,toggle_registration,toggle_submission
from .views import home
from django.conf import settings
from django.conf.urls.static import static
from register.views import newregister
from submissions.views import submission
from leaderboard.views import leaderboard
from emailproblemstatement.views import sendproblemstatement
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="Home"),
    path("register",newregister,name="Register"),
    path("submission",submission,name="Submit"),
    path("dashboard",dashboard,name="Dashboard"),
    path("submit-score",submitscore,name="submit-score"),
    path("toggle-registration",toggle_registration,name="toggle-registration"),
    path("toggle-submissions",toggle_submission,name="toggle-submission"),
    path('leaderboard/', leaderboard, name='leaderboard'),
    path('sendproblemstatement/', sendproblemstatement, name='sendproblemstatement'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)