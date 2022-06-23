from django.urls import path
from item import views

urlpatterns = [
    path('?category=<slug:category>', views.ItemAPIView.as_view())
]