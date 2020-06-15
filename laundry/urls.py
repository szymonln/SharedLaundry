from django.urls import path

from . import views


urlpatterns = [
    path('color', views.choose_color, name='choose_color'),
    path('size', views.choose_size, name='choose_size'),
    path('term', views.choose_term, name='choose_term'),
    path('confirm', views.confirm_term, name='confirm_term')
]
