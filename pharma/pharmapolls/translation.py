from modeltranslation.translator import register, TranslationOptions
from . import models


@register(models.Organization)
class OrganizationTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'adress', )


@register(models.Author)
class AuthorTranslationOptions(TranslationOptions):
    fields = ('name', 'surname', 'family_name', 'description', 'work', )


@register(models.Jurnal)
class JurnalTranslationOptions(TranslationOptions):
    fields = ('name', 'description', )