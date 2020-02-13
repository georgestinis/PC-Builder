from django.urls import path, reverse
from .views import HomeView

app_name = 'quiz'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]