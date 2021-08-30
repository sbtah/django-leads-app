from django.contrib import admin
from .models import User, Agent, Lead, OrganisationProfile


admin.site.register(User)
admin.site.register(Agent)
admin.site.register(Lead)
admin.site.register(OrganisationProfile)
