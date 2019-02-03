from django.conf.urls import url
from .views import AdvertisementClass

urlpatterns = [
    url('', AdvertisementClass.as_view()),
]