from django.urls import path, include
from rest_framework.routers import DefaultRouter
from page.views.api_views import *

# below the code 
#  "Sets up the DefaultRouter for generating RESTful routes for various ViewSets."

router = DefaultRouter()
router.register('socials', SocialViewSet, basename='socials')
router.register('about-us', AboutUsViewSet, basename='aboutus')
router.register('campaigns', CampaignsViewSet, basename='campaigns')
router.register('contact-form', ContactFormViewSet, basename='contactform')
router.register('testimonials', TestimonialsViewSet, basename='testimonials')
router.register('landing-page', LandingPageViewSet, basename='landingpage')
# url example 
# http://127.0.0.1:8000/api/socials/
# http://127.0.0.1:8000/api/about-us/
# http://127.0.0.1:8000/api/campaigns/
# http://127.0.0.1:8000/api/contact-form/
# http://127.0.0.1:8000/api/testimonials/
# http://127.0.0.1:8000/api/landing-page/




app_name = 'api'


#  Define the URL patterns for the API, utilizing the DefaultRouter for automatic route generation
urlpatterns = [
    path('', include(router.urls)),
]