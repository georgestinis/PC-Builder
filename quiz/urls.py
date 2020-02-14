from django.urls import path, reverse
from .views import HomeView, PcBuilderView

app_name = 'quiz'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('pc-builder/', PcBuilderView.as_view(), name='quiz')
]