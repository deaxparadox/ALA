from django.urls import path 

from .api.apiviews import URLView

app_name="data"

urlpatterns = [
    path("", URLView.as_view(), name="api_home")
]
