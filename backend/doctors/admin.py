from django.contrib import admin
from doctors.models import Hospital, Medecin

admin.site.register(Medecin)
admin.site.register(Hospital)
