from django.contrib import admin
from . import models
from .models import Organization, Author, Jurnal
from modeltranslation.admin import TranslationAdmin


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


class AuthorAdmin(TranslationAdmin):
    model = Author


class JurnalAdmin(TranslationAdmin):
    model = Jurnal


admin.site.register(models.Organization, OrganizationAdmin)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Jurnal, JurnalAdmin)
admin.site.register(models.Contact)
admin.site.register(models.Subdivision,)
admin.site.register(models.Statya,)
admin.site.register(models.Video, VideoGallerys,)
admin.site.register(models.News,)
admin.site.register(models.Banner, )
admin.site.register(models.Faq,)
admin.site.register(models.Webcontact,)


