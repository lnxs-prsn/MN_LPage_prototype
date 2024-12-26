from django.urls import path, include
from rest_framework.routers import DefaultRouter
from page.views.api_views import *



router = DefaultRouter()
router.register('socials', SocialViewSet, basename='socials')
router.register('about-us', AboutUsViewSet, basename='aboutus')
router.register('campaigns', CampaignsViewSet, basename='campaigns')
router.register('contact-form', ContactFormViewSet, basename='contactform')
router.register('testimonials', TestimonialsViewSet, basename='testimonials')
router.register('landing-page', LandingPageViewSet, basename='landingpage')


# app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
]