from rest_framework import serializers
from . import models
from django.db.models import Sum
from django.utils.html import strip_tags


class SubdivisionSerializer(serializers.ModelSerializer):
    organization = serializers.StringRelatedField()


    class Meta:
        fields = ('id', 'organization', 'name', 'description', 'adress', 'phon_number', 'facs_number', 'email', 'website', 'logo', )
        model = models.Subdivision

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['description'] = strip_tags(instance.description)
        return data




class OrganizationSerializer(serializers.ModelSerializer):
    subdivisions = SubdivisionSerializer(many=True, source='organization_subdivision')

    class Meta:
        fields = ('id', 'name', 'description', 'adress', 'phon_number', 'facs_number', 'email', 'website',
                  'image', 'logo', 'issn', 'top', 'number_table', 'subdivisions')
        model = models.Organization


    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['description'] = strip_tags(instance.description)
        return data


class AuthorSerializer(serializers.ModelSerializer):
    count_download = serializers.CharField(write_only=True)
    count_article = serializers.CharField(write_only=True)

    class Meta:
        fields = ('id', 'name', 'surname', 'family_name', 'description', 'work', 'count_author', 'count_download', 'count_article')
        model = models.Author

    def to_representation(self, instance):
        article = models.Statya.objects.filter(author__id=instance.id).aggregate(Sum('downloadview'))
        count_article = models.Statya.objects.filter(author__id=instance.id).count()
        data = super().to_representation(instance)
        data['description'] = strip_tags(instance.description)
        data['count_download'] = article["downloadview__sum"]
        data['count_article'] = str(count_article)
        return data


class StatyaSerializer(serializers.ModelSerializer):
    jurnal = serializers.StringRelatedField()
    author = AuthorSerializer(read_only=True, many=True)


    class Meta:
        fields = ('id', 'author', 'name', 'jurnal', 'language', 'downloadfile', 'downloadview', 'views', 'date', 'keyword', )
        model = models.Statya



class StatyaforAuthorSerializer(serializers.ModelSerializer):
    jurnal = serializers.StringRelatedField()

    class Meta:
        fields = ('id', 'name', 'jurnal', 'language', 'downloadfile', 'downloadview', 'views', 'date', 'keyword', )
        model = models.Statya




class AuthorDetailSerializer(serializers.ModelSerializer):
    count_download = serializers.CharField(write_only=True)
    count_article = serializers.CharField(write_only=True)
    articles = StatyaforAuthorSerializer(many=True, source='article_author')

    class Meta:
        fields = ('id', 'name', 'surname', 'family_name', 'description', 'work', 'count_author', 'count_download', 'count_article', 'articles')
        model = models.Author

    def to_representation(self, instance):
        article = models.Statya.objects.filter(author__id=instance.id).aggregate(Sum('downloadview'))
        count_article = models.Statya.objects.filter(author__id=instance.id).count()
        data = super().to_representation(instance)
        data['description'] = strip_tags(instance.description)
        data['count_download'] = article["downloadview__sum"]
        data['count_article'] = str(count_article)
        return data



class JurnalDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    organization = OrganizationSerializer()
    articles = StatyaSerializer(many=True, source='journal_article')

    class Meta:
        fields = ('id', 'author', 'organization', 'name', 'description', 'date', 'downloadview', 'views',
                  'pdf_file', 'keyword', 'image', 'articles' )
        model = models.Jurnal

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['description'] = strip_tags(instance.description)
        return data





class JurnalSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    organization = serializers.StringRelatedField()

    class Meta:
        fields = ('id', 'author', 'organization', 'name', 'description', 'date', 'downloadview', 'views',
                  'pdf_file', 'keyword', 'image' )
        model = models.Jurnal

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['description'] = strip_tags(instance.description)
        return data



class ConferenceSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'organization', 'name', 'description', 'adress', 'phon_number', 'date', 'sponsor', 'email', )
        model = models.Conference
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['description'] = strip_tags(instance.description)
        return data


class SeminarSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'organization', 'name', 'description', 'link', 'linkbutton', 'phon_number', 'date', 'sponsor', )
        model = models.Seminar


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'photo', 'organization', 'views', 'date', )
        model = models.Video


class Video_GallerySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'video', 'videourl', 'title', )
        model = models.Video_Gallery


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'description', 'date', 'photo', 'views', )
        model = models.News


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'phon_number', 'email', 'message', 'organization', 'lavozim', 'theme', )
        model = models.Contact
