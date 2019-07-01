from django.contrib import admin

# Register your models here.
from .models import siteUser, review, destination,  history, state

admin.site.register(siteUser)
admin.site.register(review)
admin.site.register(destination)
admin.site.register(history)
admin.site.register(state)

