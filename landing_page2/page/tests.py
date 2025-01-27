from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from page.models import Socials
from rest_framework_simplejwt.views import TokenBlacklistView
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework.test import APIClient
import jwt


class SocialsAPITestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()

        # Call get_new_tokens to ensure fresh tokens before each test
        self.get_new_tokens()

    def get_new_tokens(self):
        # Obtain tokens for each test
        response = self.client.post(
            reverse('api:token_obtain_pair'),
            {'username': 'testuser', 'password': 'testpassword'},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Ensure token generation is successful
        self.access_token = response.data['access']  # Save the access token
        self.refresh_token = RefreshToken(response.data['refresh'])  # Save the refresh token

        # Debug print: check the generated tokens
        print(f"Generated Access Token: {self.access_token}")  
        print(f"Generated Refresh Token: {self.refresh_token}")

    def get_auth_headers(self):
        return {'Authorization': f'Bearer {self.access_token}'}



    # def test_logout(self):
    #     # Get a valid token (already done in the setup part of the test, assuming `self.access_token`)
    #     access_token = self.access_token
    #     self.logout_url = reverse('api:token_blacklist') 
    #     # Post request to logout with the access token
    #     logout_response = self.client.post(self.logout_url, HTTP_AUTHORIZATION='Bearer ' + access_token)

    #     # Assert that the response status code is 200
    #     self.assertEqual(logout_response.status_code, status.HTTP_200_OK)

    #     # Check if the token is now blacklisted
    #     blacklist_check = BlacklistedToken.objects.filter(token=access_token).exists()

    #     # Assert that the token is blacklisted
    #     self.assertTrue(blacklist_check, "Token should be blacklisted")




    

    def test_logout(self):
        # The refresh token should be blacklisted
        refresh_token = self.refresh_token  # You already have this in setup

        # Blacklist the refresh token
        response = self.client.post(
            reverse('api:token_blacklist'),
            {'refresh': str(refresh_token)},
            format='json'
        )
        print(f"Blacklist Response: {response.status_code} - {response.content}")


    #     # Check if the token is now blacklisted
        blacklist_check = BlacklistedToken.objects.filter(token__jti=refresh_token.payload['jti']).exists(),
        if blacklist_check == True:
            print('the token is inside the blacklisted tokens list@@@@@@@@@@@@@@@@@')
        else:
            print('the token is not inside the blacklisted tokens list')


        # Verify that the refresh token was blacklisted by checking for the jti
        self.assertTrue(
            BlacklistedToken.objects.filter(token__jti=refresh_token.payload['jti']).exists(),
            "Refresh token was not blacklisted"
        )

        # Attempt to access a protected endpoint using the access token
        response = self.client.get(
            reverse('api:socials-list'),
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'  # Use the access token
        )

        # Assert the access token is now invalid after blacklisting the refresh token
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_list_socials(self):
        # Ensure fresh tokens before the test
        self.get_new_tokens()
        print(f"Access Token in List Test: {self.access_token}")  # Debug print
        # Normal authenticated request (before logout)
        response = self.client.get(reverse('api:socials-list'), HTTP_AUTHORIZATION=self.get_auth_headers()['Authorization'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_social(self):
        # Ensure fresh tokens before the test
        self.get_new_tokens()
        data = {
            "platform_name": "Twitter",
            "url": "https://twitter.com/example",
            "title": "Example Twitter Page",
            "meta_description": "An example Twitter page.",
            "submission_url": "https://twitter.com/example",
            "slug": "twitter-example"
        }
        response = self.client.post(reverse('api:socials-list'), data, HTTP_AUTHORIZATION=self.get_auth_headers()['Authorization'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_social(self):
        # Ensure fresh tokens before the test
        self.get_new_tokens()
        social = Socials.objects.create(
            platform_name="Facebook", 
            url="https://facebook.com/example", 
            title="Example Facebook Page",
            meta_description="An example Facebook page.",
            submission_url="https://facebook.com/example",
            slug="facebook-example"
        )
        data = {"title": "Updated Facebook Page"}
        response = self.client.patch(reverse('api:socials-detail', args=[social.id]), data, HTTP_AUTHORIZATION=self.get_auth_headers()['Authorization'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_social(self):
        # Ensure fresh tokens before the test
        self.get_new_tokens()
        social = Socials.objects.create(
            platform_name="Instagram", 
            url="https://instagram.com/example", 
            title="Example Instagram Page",
            meta_description="An example Instagram page.",
            submission_url="https://instagram.com/example",
            slug="instagram-example"
        )
        response = self.client.delete(reverse('api:socials-detail', args=[social.id]), HTTP_AUTHORIZATION=self.get_auth_headers()['Authorization'])
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Socials.objects.filter(id=social.id).exists())
