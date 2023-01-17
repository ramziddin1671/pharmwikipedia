from django.contrib import admin
from . import models
from modeltranslation.admin import TranslationAdmin
# Register your models here.
from .models import Organization


class VidioInline(admin.StackedInline):
    model = models.Video_Gallery


class VideoGallerys(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ["title", "photo"]})
    ]
    inlines = [VidioInline]


@admin.register(models.Conference)
class ConferanceAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'archive']



@admin.register(models.Seminar)
class ConferanceAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'archive']


class OrganizationAdmin(TranslationAdmin):
    model = Organization


admin.site.register(models.Organization, OrganizationAdmin,)
admin.site.register(models.Author,)
admin.site.register(models.Jurnal,)
admin.site.register(models.Contact)
admin.site.register(models.Subdivision,)
admin.site.register(models.Statya,)
admin.site.register(models.Video, VideoGallerys,)
admin.site.register(models.News,)
admin.site.register(models.Banner, )
admin.site.register(models.Faq,)
admin.site.register(models.Webcontact,)


