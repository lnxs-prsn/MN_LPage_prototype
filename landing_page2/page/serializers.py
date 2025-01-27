from rest_framework import serializers # Importing the necessary module for creating serializers in Django REST framework.
from page.models.page_models import *
from django.contrib.auth.models import User  # Importing the User model from Django's built-in auth system.
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator


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



class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user






class UserProfileSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name']

    def get_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
