from django.urls import path
from .views import *


urlpatterns = [
    path("", OrganizationList.as_view()),
    path("organization/<int:pk>/", OrganizationDetail.as_view()),
    path("authors/", AuthorList.as_view()),
    path("author/<int:pk>/", AuthorDetail.as_view()),
    path("journals/", JurnalList.as_view()),
    path("journal/<int:pk>/", JurnalDetail.as_view()),
    path("subdivisions/", SubdivisionList.as_view()),
    path("subdivision/<int:pk>/", SubdivisionDetail.as_view()),
    path("articles/", StatyaList.as_view()),
    path("article/<int:pk>/", StatyaDetail.as_view()),
    path("conferences/", ConferenceList.as_view()),
    path("conference/<int:pk>/", ConferenceDetail.as_view()),
    path("seminars/", SeminarList.as_view()),
    path("seminar/<int:pk>/", SeminarDetail.as_view()),
    path("videos/", VideoList.as_view()),
    path("video/<int:pk>/", VideoDetail.as_view()),
    path("video_gallery/", Video_GalleryList.as_view()),
    path("video_gallery/<int:pk>/", Video_GalleryDetail.as_view()),
    path("news/", NewsList.as_view()),
    path("news/<int:pk>/", NewsDetail.as_view()),
    path("contacts/", ContactList.as_view()),
    path("contact/<int:pk>/", ContactDetail.as_view()),
]
