from rest_framework import serializers
from page.models.page_models import *
from django.contrib.auth.models import User


# Serializer for the Socials model
# This converts Socials model instances to JSON and vice versa
class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socials  # Specify the model to be serialized
        fields = '__all__'  # Include all fields of the Socials model in the serialized data


# Serializer for the AboutUs model
# This converts AboutUs model instances to JSON and vice versa
class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs  # Specify the model to be serialized
        fields = '__all__'  # Include all fields of the AboutUs model in the serialized data


# Serializer for the Campaigns model
# This converts Campaigns model instances to JSON and vice versa
class CampaignsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaigns  # Specify the model to be serialized
        fields = '__all__'  # Include all fields of the Campaigns model in the serialized data


# Serializer for the ContactForm model
# This converts ContactForm model instances to JSON and vice versa
class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm  # Specify the model to be serialized
        fields = '__all__'  # Include all fields of the ContactForm model in the serialized data


# Serializer for the Testimonials model
# This converts Testimonials model instances to JSON and vice versa
class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials  # Specify the model to be serialized
        fields = '__all__'  # Include all fields of the Testimonials model in the serialized data


# Serializer for the LandingPage model
# This converts LandingPage model instances to JSON and vice versa
# Additionally, it includes nested serializers for related models like Campaigns, Testimonials, and Socials
class LandingPageSerializer(serializers.ModelSerializer):
    featured_campaigns = CampaignsSerializer(many=True)  # Nested serializer for related Campaigns
    testimonials = TestimonialsSerializer(many=True)  # Nested serializer for related Testimonials
    socials_links = SocialSerializer(many=True)  # Nested serializer for related Socials
    
    class Meta:
        model = LandingPage  # Specify the model to be serialized
        fields = '__all__'  # Include all fields of the LandingPage model in the serialized data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'date_joined']