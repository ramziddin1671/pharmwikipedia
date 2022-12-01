from django.urls import path
from .views import OrganizationList, OrganizationDetail


urlpatterns = [
    path("<int:pk>/", OrganizationDetail.as_view()),
    path("", OrganizationList.as_view()),
]