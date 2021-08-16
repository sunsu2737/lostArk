from django.urls import path
from . import views


urlpatterns=[
    path('home',views.HomePage.as_view(),name='home'),
    path('create',views.GuideCreate.as_view(),name='create'),
    path('guide/<int:boss_id>',views.GuideSelect.as_view(),name='guide')
    
]