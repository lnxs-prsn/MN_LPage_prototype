from django.urls import path
from page.views.page_views import *


app_name = 'page'

urlpatterns = [
    path('landing-page/', landing_page_view, name='landing_page'),
]



