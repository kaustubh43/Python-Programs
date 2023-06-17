from django.contrib import admin

from . import models

# Register your models here.


class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')



# Register that the model we created is attached to the admin model
admin.site.register(models.Notes, NotesAdmin)

