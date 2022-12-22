from . import serializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import generics
from . import models
from rest_framework import generics, status
from rest_framework.response import Response
from .permissions import IsAuthenticatedOrReadOnly



class OrganizationList(ListCreateAPIView):
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer


class OrganizationDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer


class AuthorList(ListCreateAPIView):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class AuthorDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class JurnalList(ListCreateAPIView):
    queryset = models.Jurnal.objects.all()
    serializer_class = serializers.JurnalSerializer


class PopularJurnalList(generics.ListAPIView):
    queryset = models.Jurnal.objects.all().order_by('-downloadview')[:12]
    serializer_class = serializers.JurnalSerializer



class JurnalDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = models.Jurnal.objects.all()
    serializer_class = serializers.JurnalSerializer


class SubdivisionList(ListCreateAPIView):
    queryset = models.Subdivision.objects.all()
    serializer_class = serializers.SubdivisionSerializer


class SubdivisionDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = models.Subdivision.objects.all()
    serializer_class = serializers.SubdivisionSerializer


class StatyaList(ListCreateAPIView):
    queryset = models.Statya.objects.all()
    serializer_class = serializers.StatyaSerializer


class StatyaDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = models.Statya.objects.all()
    serializer_class = serializers.StatyaSerializer


class StatisticsApiView(generics.ListAPIView):
    queryset = None
    serializer_class = None

    def get(self, request, *args, **kwargs):
        context = {'request': request}
        journals = models.Jurnal.objects.all().count()
        authors = models.Author.objects.all().count()
        organizations = models.Organization.objects.all().count()
        seminars = models.Seminar.objects.all().count()



        payload = {
            'journals': journals,
            'authors': authors,
            'organizations': organizations,
            'seminars': seminars,
        }
        return Response(payload, status=status.HTTP_200_OK)


class ConferenceList(ListCreateAPIView):
    queryset = models.Conference.objects.all()
    serializer_class = serializers.ConferenceSerializer


class ConferenceDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = models.Conference.objects.all()
    serializer_class = serializers.ConferenceSerializer


class PlanningConferenceApiView(generics.ListAPIView):
    queryset = models.Conference.objects.all().order_by('date')[:12]
    serializer_class = serializers.ConferenceSerializer


class SeminarList(ListCreateAPIView):
    queryset = models.Seminar.objects.all()
    serializer_class = serializers.SeminarSerializer


class SeminarDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = models.Seminar.objects.all()
    serializer_class = serializers.SeminarSerializer


class VideoList(ListCreateAPIView):
    queryset = models.Video.objects.all()
    serializer_class = serializers.VideoSerializer


class VideoDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = models.Video.objects.all()
    serializer_class = serializers.VideoSerializer


class Video_GalleryList(ListCreateAPIView):
    queryset = models.Video_Gallery.objects.all()
    serializer_class = serializers.Video_GallerySerializer


class Video_GalleryDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = models.Video_Gallery.objects.all()
    serializer_class = serializers.Video_GallerySerializer


class NewsList(ListCreateAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer


class NewsDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer


class ContactList(ListCreateAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer


class ContactDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer

