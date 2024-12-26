from rest_framework import viewsets
from page.models.page_models import *
from page.serializers import *
from rest_framework.permissions import IsAdminUser



class SocialViewSet(viewsets.ModelViewSet):
    queryset = Socials.objects.all()
    serializer_class = SocialSerializer
    permission_classes = [IsAdminUser]


class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [IsAdminUser]


class CampaignsViewSet(viewsets.ModelViewSet):
    queryset = Campaigns.objects.all()
    serializer_class = CampaignsSerializer
    permission_classes = [IsAdminUser]


class ContactFormViewSet(viewsets.ModelViewSet):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
    permission_classes = [IsAdminUser]


class TestimonialsViewSet(viewsets.ModelViewSet):
    queryset = Testimonials.objects.all()
    serializer_class = TestimonialsSerializer
    permission_classes = [IsAdminUser]


class LandingPageViewSet(viewsets.ModelViewSet):
    queryset = LandingPage.objects.all()
    serializer_class = LandingPageSerializer
    permission_classes = [IsAdminUser]

class UserSerializerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer   
    permission_classes = [IsAdminUser]