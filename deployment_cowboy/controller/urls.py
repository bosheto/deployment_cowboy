
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='controller-home'),
    path('about/', views.about, name='controller-about'),
    path('build-jar/', views.build_jar, name='build-jar-button'),
    path('test-jar', views.run_test, name='test-jar-button'),
    path('clear-output', views.clear_console_output, name='clear-output-button'),
]
