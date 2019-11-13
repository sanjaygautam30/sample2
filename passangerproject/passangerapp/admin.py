from django.contrib import admin
from .models import Passanger
class PassangerAdmin(admin.ModelAdmin):
    list_display=['pid','fname','lname','age','seatno']
admin.site.register(Passanger,PassangerAdmin)