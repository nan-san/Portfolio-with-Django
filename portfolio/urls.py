from django.urls import path,include
from . import views
from .views import ContactFormView, ContactResultView


app_name = 'portfolio'

urlpatterns = [
    # path('', views.HomeView.as_view(), name='home'),
    path('', views.home, name='home'),
    
    path('contact/', ContactFormView.as_view(), name='contact_form'),
    path('contact/result/', ContactResultView.as_view(), name='contact_result'),

]