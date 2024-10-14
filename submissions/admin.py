from django.contrib import admin

from submissions.models import Submission,SiteSetting

# Register your models here.
admin.site.register(Submission)
admin.site.register(SiteSetting)