# Importing necessary modules and classes from Django Rest Framework and project files.
from rest_framework import viewsets, status
from page.models.page_models import *  # Importing all models from page_models.py
from page.serializers import *  # Importing all serializers from serializers.py
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny  # Importing the permission class that ensures only admin users can access the views
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db import IntegrityError
from rest_framework_simplejwt.tokens import RefreshToken



# ViewSet for managing the Socials model. This allows admins to perform CRUD operations on social media data.
class SocialViewSet(viewsets.ModelViewSet):
    queryset = Socials.objects.all()  # Retrieving all Socials instances from the database
    serializer_class = SocialSerializer  # Associating the SocialSerializer with this ViewSet for serialization
    # permission_classes = [IsAdminUser]  # Ensuring that only admin users have access to this view
    permission_classes = [IsAuthenticated]

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




# I will replace this with better way of doing this but now its just this
# I deleted this part in the deployed project 

# class UserProfileViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserProfileSerializer
#     permission_classes = [IsAuthenticated]
#     # permission_classes = [AllowAny]


#     def get_queryset(self):
#         # Limit the queryset to the authenticated user for security
#         return User.objects.filter(id=self.request.user.id)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]  # Ensures only authenticated users can access

    def get_queryset(self):
        # Restrict to the authenticated user's profile
        return User.objects.filter(id=self.request.user.id)

    def list(self, request, *args, **kwargs):
        # Instead of a list, return just the single authenticated user's data
        user = self.get_queryset().first()
        serializer = self.get_serializer(user)
        return Response(serializer.data)



# comment better
class UserRegistrationViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]  # Allow access without authentication


    def create(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = serializer.save()  # Save user details and hash password
                refresh = RefreshToken.for_user(user)  # Generate JWT tokens
                return Response({
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'name': f"{user.first_name} {user.last_name}",
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response(
                    {'error': 'A user with this username or email already exists.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



