from rest_framework import serializers
from .models import *
from django.utils.html import strip_tags



class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'description', 'adress', 'phon_number', 'facs_number', 'email', 'website',
                  'image', 'logo', 'issn', 'top', 'number_table', )
        model = Organization


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'surname', 'family_name', 'description', 'work', 'count_author', )
        model = Author


class JurnalSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'organization', 'name', 'description', 'date', 'downloadview', 'views',
                  'pdf_file', 'keyword', 'image', )
        model = Jurnal


class SubdivisionSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'organization', 'name', 'description', 'adress', 'phon_number', 'facs_number', 'email', 'website', 'logo', )
        model = Subdivision


class StatyaSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'name', 'jurnal', 'language', 'downloadfile', 'downloadview', 'views', 'date', 'keyword', )
        model = Statya


class ConferenceSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'organization', 'name', 'description', 'adress', 'phon_number', 'date', 'sponsor', 'email', )
        model = Conference
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['description'] = strip_tags(instance.description)
        return data


class SeminarSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'organization', 'name', 'description', 'link', 'linkbutton', 'phon_number', 'date', 'sponsor', )
        model = Seminar


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'photo', 'organization', 'views', 'date', )
        model = Video


class Video_GallerySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'video', 'videourl', 'title', )
        model = Video_Gallery


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'description', 'date', 'photo', 'views', )
        model = News


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'phon_number', 'email', 'message', 'organization', 'lavozim', 'theme', )
        model = Contact
