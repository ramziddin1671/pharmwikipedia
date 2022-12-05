from .serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .permissions import IsAuthenticatedOrReadOnly

# Create your views here.


class OrganizationList(ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class AuthorList(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class JurnalList(ListCreateAPIView):
    queryset = Jurnal.objects.all()
    serializer_class = JurnalSerializer


class JurnalDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Jurnal.objects.all()
    serializer_class = JurnalSerializer


class SubdivisionList(ListCreateAPIView):
    queryset = Subdivision.objects.all()
    serializer_class = SubdivisionSerializer


class SubdivisionDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Subdivision.objects.all()
    serializer_class = SubdivisionSerializer


class StatyaList(ListCreateAPIView):
    queryset = Statya.objects.all()
    serializer_class = StatyaSerializer


class StatyaDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Statya.objects.all()
    serializer_class = StatyaSerializer


class ConferenceList(ListCreateAPIView):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer


class ConferenceDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer


class SeminarList(ListCreateAPIView):
    queryset = Seminar.objects.all()
    serializer_class = SeminarSerializer


class SeminarDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Seminar.objects.all()
    serializer_class = SeminarSerializer


class VideoList(ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class Video_GalleryList(ListCreateAPIView):
    queryset = Video_Gallery.objects.all()
    serializer_class = Video_GallerySerializer


class Video_GalleryDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Video_Gallery.objects.all()
    serializer_class = Video_GallerySerializer


class NewsList(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class ContactList(ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer