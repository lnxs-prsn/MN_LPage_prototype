from django.shortcuts import render
from page.models.page_models import LandingPage

def landing_page_view(request):
    # Get the landing page data from the database (you can adjust the query as needed)
    landing_page = LandingPage.objects.first()  # You can modify this as needed
    return render(request, 'page/landing_page.html', {'landing_page': landing_page})
