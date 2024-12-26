# Importing necessary modules and classes from Django Rest Framework and project files.
from rest_framework import viewsets
from page.models.page_models import *  # Importing all models from page_models.py
from page.serializers import *  # Importing all serializers from serializers.py
from rest_framework.permissions import IsAdminUser  # Importing the permission class that ensures only admin users can access the views

# ViewSet for managing the Socials model. This allows admins to perform CRUD operations on social media data.
class SocialViewSet(viewsets.ModelViewSet):
    queryset = Socials.objects.all()  # Retrieving all Socials instances from the database
    serializer_class = SocialSerializer  # Associating the SocialSerializer with this ViewSet for serialization
    permission_classes = [IsAdminUser]  # Ensuring that only admin users have access to this view

# ViewSet for managing the AboutUs model. This allows admins to perform CRUD operations on the About Us section data.
class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()  # Retrieving all AboutUs instances from the database
    serializer_class = AboutUsSerializer  # Using the AboutUsSerializer for serialization
    permission_classes = [IsAdminUser]  # Restricting access to admin users only

# ViewSet for managing the Campaigns model. This allows admins to manage campaign-related data.
class CampaignsViewSet(viewsets.ModelViewSet):
    queryset = Campaigns.objects.all()  # Retrieving all Campaigns instances from the database
    serializer_class = CampaignsSerializer  # Using the CampaignsSerializer to format the data
    permission_classes = [IsAdminUser]  # Allowing access only to admin users

# ViewSet for managing the ContactForm model. This handles data related to contact forms submitted by users.
class ContactFormViewSet(viewsets.ModelViewSet):
    queryset = ContactForm.objects.all()  # Retrieving all ContactForm instances from the database
    serializer_class = ContactFormSerializer  # Serializing ContactForm data with ContactFormSerializer
    permission_classes = [IsAdminUser]  # Limiting access to admin users only

# ViewSet for managing the Testimonials model. This allows admins to handle customer testimonials.
class TestimonialsViewSet(viewsets.ModelViewSet):
    queryset = Testimonials.objects.all()  # Retrieving all Testimonials instances from the database
    serializer_class = TestimonialsSerializer  # Using TestimonialsSerializer for serialization
    permission_classes = [IsAdminUser]  # Restricting access to admins

# ViewSet for managing the LandingPage model. Admins can manage the landing page information through this view.
class LandingPageViewSet(viewsets.ModelViewSet):
    queryset = LandingPage.objects.all()  # Retrieving all LandingPage instances
    serializer_class = LandingPageSerializer  # Serializing LandingPage data with LandingPageSerializer
    permission_classes = [IsAdminUser]  # Ensuring that only admin users can access this endpoint

# ViewSet for managing the User model. Admins can perform CRUD operations on user data.
class UserSerializerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # Retrieving all User instances from the database
    serializer_class = UserSerializer  # Using UserSerializer to format user data
    permission_classes = [IsAdminUser]  # Ensuring that only admin users can access the view
