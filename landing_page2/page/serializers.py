from rest_framework import serializers
from page.models.page_models import *


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socials
        fields = '__all__'


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'


class CampaignsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaigns
        fields = '__all__'


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = '__all__'



class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = '__all__'


class LandingPageSerializer(serializers.ModelSerializer):
    featured_campaigns = CampaignsSerializer(many=True)
    testimonials = TestimonialsSerializer(many=True)
    socials_links = SocialSerializer(many=True)
    
    class Meta:
        model = LandingPage
        fields = '__all__'

