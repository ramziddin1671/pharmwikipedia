from rest_framework import serializers
from .models import *


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'description', 'adress', 'phon_number', 'facs_number', 'email', 'website',
                  'image', 'logo', 'issn', 'top', 'number_table', )
        model = Organization


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'surname', 'family_name', 'description', )
        model = Author


class JurnalSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'organization', 'name', 'description', 'date', 'downloadview', 'views',
                  'file', 'keyword', 'image', )
        model = Jurnal


class SubdivisionSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'organization', 'name', 'description', 'adress', 'phon_number', 'facs_number', 'email', 'website', )
        model = Subdivision


class StatyaSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'name', 'jurnal', 'downloadfile', 'downloadview', 'views', )
        model = Statya


class ConferenceSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'organization', 'name', 'description', 'adress', 'phon_number', 'date', 'sponsor', )
        model = Conference


class SeminarSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'organization', 'name', 'description', 'link', 'phon_number', 'date', 'sponsor', )
        model = Seminar


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'photo', )
        model = Video


class Video_GallerySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'video', 'videourl', 'title', )
        model = Video_Gallery


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'description', 'date', 'photo', )
        model = News


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'phon_number', 'email', 'taklif', )
        model = Contact
