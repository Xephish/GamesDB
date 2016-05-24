from django.contrib import admin
import models

admin.site.register(models.Developer)
admin.site.register(models.Platform)
admin.site.register(models.Game)
admin.site.register(models.GameReview)