from django.urls import path
from .views import *


urlpatterns = [
    path("<int:pk>/", OrganizationDetail.as_view()),
    path("", OrganizationList.as_view()),
    path("Author/", AuthorList.as_view()),
    path("Author/<int:pk>/", AuthorDetail.as_view()),
    path("Jurnal/", JurnalList.as_view()),
    path("Jurnal/<int:pk>/", JurnalDetail.as_view()),
    path("Subdivision/", SubdivisionList.as_view()),
    path("Subdivision/<int:pk>/", SubdivisionDetail.as_view()),
    path("Statya/", StatyaList.as_view()),
    path("Statya/<int:pk>/", StatyaDetail.as_view()),
    path("Conference/", ConferenceList.as_view()),
    path("Conference/<int:pk>/", ConferenceDetail.as_view()),
    path("Seminar/", SeminarList.as_view()),
    path("Seminar/<int:pk>/", SeminarDetail.as_view()),
    path("Video/", VideoList.as_view()),
    path("Video/<int:pk>/", VideoDetail.as_view()),
    path("Video_Gallery/", Video_GalleryList.as_view()),
    path("Video_Gallery/<int:pk>/", Video_GalleryDetail.as_view()),
    path("News/", NewsList.as_view()),
    path("News/<int:pk>/", NewsDetail.as_view()),
    path("Contact/", ContactList.as_view()),
    path("Contact/<int:pk>/", ContactDetail.as_view()),
]
