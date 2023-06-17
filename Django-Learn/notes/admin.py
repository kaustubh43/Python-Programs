from django.contrib import admin

from . import models
# Register your models here.


class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')


admin.site.register(models.Note, NotesAdmin)
