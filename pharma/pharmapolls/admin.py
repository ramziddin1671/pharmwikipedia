from django.contrib import admin
from .models import *
# Register your models here.

class VidioInline(admin.StackedInline):
    model = Video_Gallery


class video(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ["title", "photo"]})
    ]
    inlines = [VidioInline]


admin.site.register(Organization,)
admin.site.register(Author,)
admin.site.register(Jurnal,)
admin.site.register(Contact)
admin.site.register(Subdivision,)
admin.site.register(Statya,)
admin.site.register(Conference,)
admin.site.register(Seminar,)
admin.site.register(Video,)
admin.site.register(News,)
