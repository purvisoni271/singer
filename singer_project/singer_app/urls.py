from django.urls import path
from .views import SingerList

urlpatterns = [
	path('', SingerList.as_view())
]
