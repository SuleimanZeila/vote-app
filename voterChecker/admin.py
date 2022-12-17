from django.contrib import admin
from django_admin_search.admin import AdvancedSearchAdmin
from .models import Voter,VoterAdmin
# Register your models here.

admin.site.register(Voter,VoterAdmin)

