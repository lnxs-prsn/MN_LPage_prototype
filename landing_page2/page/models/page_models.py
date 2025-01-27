from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.exceptions import ValidationError


# Socials model to store social media platform information
class Socials(models.Model):
    platform_name = models.CharField(max_length=250, db_index=True)  # Name of the social media platform
    url = models.URLField()  # URL to the social media page
    title = models.CharField(max_length=250)  # Title for the social media entry
    icon = models.ImageField(upload_to='icons/', null=True, blank=True)  # Optional icon image for the platform
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the record was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for when the record was last updated
    slug = models.SlugField(unique=True, db_index=True)  # Slug field for URL-friendly names (unique for each record)
    meta_description = models.CharField(max_length=300, null=True, blank=True)  # Meta description for SEO purposes
    metadata = models.JSONField()
    category = models.CharField(max_length=350, null=True, blank=True)  # Optional category field for grouping
    status = models.BooleanField(default=True)
    submission_url = models.URLField(default=dict)

    def __str__(self):
        return f'{self.title} in the {self.platform_name}'  # Return a string representation for the object

    def save(self, *args, **kwargs):
        # Automatically generate a slug if it does not exist, ensuring it's unique
        if not self.slug:
            self.slug = slugify(self.title)
            base_slug = self.slug
            counter = 1
            while Socials.objects.filter(slug=self.slug).exists():
                self.slug = f'{base_slug}-{counter}'
                counter += 1
        super().save(*args, **kwargs)  # Call the parent save method

    def clean(self):
        # Ensure that the meta_description field does not exceed 300 characters
        if self.meta_description and len(self.meta_description) > 300:
            raise ValidationError("Meta description can't be longer than 300 characters.")
        super().clean()  # Call the parent clean method

    class Meta:
        ordering = ['-created_at']  # Order records by creation date in descending order


# AboutUs model to store information about the "About Us" section of a website
class AboutUs(models.Model):
    mission = models.TextField()  # Mission statement
    team = models.TextField()  # Team description
    contact_info = models.TextField(null=True, blank=True)  # Optional contact information
    history = models.TextField(null=True, blank=True)  # Optional history section
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the record was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for when the record was last updated
    meta_description = models.CharField(max_length=300, null=True, blank=True)  # Meta description for SEO purposes
    status = models.BooleanField(default=True)
    metadata = models.JSONField(default=dict)

    def __str__(self):
        return 'About Page'  # Return a string representation for the object

    def clean(self):
        # Ensure that the meta_description field does not exceed 300 characters
        if self.meta_description and len(self.meta_description) > 300:
            raise ValidationError("Meta description can't be longer than 300 characters.")
        super().clean()  # Call the parent clean method

    class Meta:
        verbose_name = 'About Page'  # Custom singular name for the model
        verbose_name_plural = 'About Pages'  # Custom plural name for the model


# Campaigns model to store information about campaigns
class Campaigns(models.Model):
    title = models.CharField(max_length=255, db_index=True)  # Title of the campaign
    content = models.TextField()  # Detailed content of the campaign
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='campaigns', db_index=True, null=True)  # Foreign key linking to the User who created the campaign
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the record was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for when the record was last updated
    slug = models.SlugField(unique=True, db_index=True)  # Slug field for URL-friendly names (unique for each record)
    meta_description = models.CharField(max_length=300, null=True, blank=True)  # Meta description for SEO purposes
    category = models.CharField(max_length=350, null=True, blank=True)  # Optional category field for grouping
    status = models.BooleanField(default=False)
    submission_url = models.URLField()
    metadata = models.JSONField(default=dict)

    def __str__(self):
        return f'{self.title} campaign'  # Return a string representation for the object

    def save(self, *args, **kwargs):
        # Automatically generate a slug if it does not exist, ensuring it's unique
        if not self.slug:
            self.slug = slugify(self.title)
            base_slug = self.slug
            counter = 1
            while Campaigns.objects.filter(slug=self.slug).exists():
                self.slug = f'{base_slug}-{counter}'
                counter += 1
        super().save(*args, **kwargs)  # Call the parent save method
    
    def clean(self):
        # Ensure that the meta_description field does not exceed 300 characters
        if self.meta_description and len(self.meta_description) > 300:
            raise ValidationError("Meta description can't be longer than 300 characters.")
        super().clean()  # Call the parent clean method
    
    class Meta:
        ordering = ['-created_at']  # Order records by creation date in descending order


# ContactForm model to store contact form submissions
class ContactForm(models.Model):
    name = models.CharField(max_length=250)  # Name of the person submitting the contact form
    email = models.EmailField(db_index=True)  # Email address of the person submitting the contact form
    message = models.TextField()  # Message content submitted through the contact form
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the record was created
    meta_description = models.CharField(max_length=300, null=True, blank=True)  # Meta description for SEO purposes
    status = models.BooleanField(default=True)
    submission_url = models.URLField(null=True, blank=True)
    metadata = models.JSONField(default=dict)

    def __str__(self):
        return f'Contact submission by {self.name} on {self.created_at}'  # Return a string representation for the object

    def clean(self):
        # Ensure that the meta_description field does not exceed 300 characters
        if self.meta_description and len(self.meta_description) > 300:
            raise ValidationError("Meta description can't be longer than 300 characters.")
        super().clean()  # Call the parent clean method


# Testimonials model to store customer testimonials
class Testimonials(models.Model):
    name = models.CharField(max_length=250)  # Name of the person giving the testimonial
    content = models.TextField()  # Content of the testimonial
    campaign = models.ForeignKey(Campaigns, on_delete=models.SET_NULL, related_name='ctestimonials', null=True, blank=True)  # Optional link to the related campaign
    video = models.ForeignKey(Socials, on_delete=models.SET_NULL, related_name='stestimonials', null=True, blank=True)  # Optional link to a related social media video
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the record was created
    meta_description = models.CharField(max_length=300, null=True, blank=True)  # Meta description for SEO purposes
    status = models.BooleanField(default=False)
    submission_url = models.URLField()
    metadata = models.JSONField(default=dict)

    def __str__(self):
        return self.name  # Return the name of the person giving the testimonial

    def clean(self):
        # Ensure that the meta_description field does not exceed 300 characters
        if self.meta_description and len(self.meta_description) > 300:
            raise ValidationError("Meta description can't be longer than 300 characters.")
        super().clean()  # Call the parent clean method

    class Meta:
        verbose_name = 'Testimonials'  # Custom singular name for the model
        verbose_name_plural = 'Testimonials'  # Custom plural name for the model


# LandingPage model to store information about the landing page
class LandingPage(models.Model):
    title = models.CharField(max_length=250, db_index=True)  # Title of the landing page
    hero_image = models.ImageField(upload_to='landing_page/', null=True, blank=True)  # Optional hero image for the landing page
    hero_text = models.TextField(null=True, blank=True)  # Optional hero text for the landing page
    about_section = models.ForeignKey(AboutUs, on_delete=models.SET_NULL, null=True, blank=True, related_name='alanding_pages')  # Foreign key linking to the About Us section
    featured_campaigns = models.ManyToManyField(Campaigns, related_name='cfeatured_on_landing', blank=True)  # Many-to-many relationship with featured campaigns
    testimonials = models.ManyToManyField(Testimonials, related_name='tfeatured_on_landing', blank=True)  # Many-to-many relationship with featured testimonials
    socials_links = models.ManyToManyField(Socials, related_name='sfeatured_on_landing', blank=True)  # Many-to-many relationship with featured social links
    contact_form = models.ForeignKey(ContactForm, on_delete=models.SET_NULL, related_name='clanding_pages', null=True, blank=True)  # Optional link to the contact form
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the record was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for when the record was last updated
    meta_description = models.CharField(max_length=300, null=True, blank=True)  # Meta description for SEO purposes
    status = models.BooleanField(default=True)
    metadata = models.JSONField(default=dict)

    def __str__(self):
        return self.title  # Return the title of the landing page

    def clean(self):
        # Ensure that the meta_description field does not exceed 300 characters
        if self.meta_description and len(self.meta_description) > 300:
            raise ValidationError("Meta description can't be longer than 300 characters.")
        super().clean()  # Call the parent clean method

    class Meta:
        verbose_name = 'Landing Page'  # Custom singular name for the model
        verbose_name_plural = 'Landing Pages'  # Custom plural name for the model
