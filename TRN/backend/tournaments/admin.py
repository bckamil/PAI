from django.contrib import admin

from tournaments.models import Application, Match, Tournament

admin.site.register(Application)
admin.site.register(Match)
admin.site.register(Tournament)
