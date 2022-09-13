from django.urls import path
from . import views

app_name = 'App_all'

urlpatterns = [
    path('', views.home, name='home'),
    path('features/', views.features, name='features'),
    path("predict-view/", views.predict_view, name="predict-view"),
    path('contact-us/', views.contact_us, name='contact-us'),
]
