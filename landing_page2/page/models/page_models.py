from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.exceptions import ValidationError







class Socials(models.Model):
    platform_name = models.CharField(max_length=250, db_index=True)
    url = models.URLField()
    title = models.CharField(max_length=250)
    icon = models.ImageField(upload_to='icons/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    meta_description = models.CharField(max_length=300, null=True, blank=True)
    category = models.CharField(max_length=350, null=True, blank=True)

    def __str__(self):
        return f'{self.title} in the {self.platform_name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            base_slug = self.slug
            counter = 1
            while Socials.objects.filter(slug=self.slug).exists():
                self.slug = f'{base_slug}-{counter}'
                counter += 1
        super().save(*args, **kwargs)

    def clean(self):
        if self.meta_description and len(self.meta_description) > 300:
            raise ValidationError("Meta description can't be longer than 300 characters.")
        super().clean()

    class Meta:
        ordering = ['-created_at']


class AboutUs(models.Model):
    mission = models.TextField()
    team = models.TextField()
    contact_info = models.TextField(null=True, blank=True)
    history = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    meta_description = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return 'About Page'

    def clean(self):
        if self.meta_description and len(self.meta_description) > 300:
            raise ValidationError("Meta description can't be longer than 300 characters.")
        super().clean()

    class Meta:
        verbose_name = 'About Page'
        verbose_name_plural = 'About Pages'



class Campaigns(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='campaigns', db_index=True, null=True, )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    meta_description = models.CharField(max_length=300, null=True, blank=True)
    category = models.CharField(max_length=350, null=True, blank=True)


    def __str__(self):
        return f'{self.title} campaign'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            base_slug = self.slug
            counter = 1
            while Campaigns.objects.filter(slug=self.slug).exists():
                self.slug = f'{base_slug}-{counter}'
                counter += 1
        super().save(*args, **kwargs)
    
    def clean(self):
        if self.meta_description and len(self.meta_description) > 300:
            raise ValidationError("Meta description can't be longer than 300 characters.")
        super().clean()
    
    class Meta:
        ordering = ['-created_at']




class ContactForm(models.Model):
    name = models.CharField(max_length=250,)
    email = models.EmailField(db_index=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    meta_description = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f'Contact submission by {self.name} on {self.created_at}'

    def clean(self):
        if self.meta_description and len(self.meta_description) > 300:
            raise ValidationError("Meta description can't be longer than 300 characters.")
        super().clean()    


class Testimonials(models.Model):
    name = models.CharField(max_length=250)
    content = models.TextField()
    campaign = models.ForeignKey(Campaigns, on_delete=models.SET_NULL, related_name='ctestimonials', null=True, blank=True)
    video = models.ForeignKey(Socials, on_delete=models.SET_NULL, related_name='stestimonials', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    meta_description = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name

    def clean(self):
        if self.meta_description and len(self.meta_description) > 300:
            raise ValidationError("Meta description can't be longer than 300 characters.")
        super().clean()

    class Meta:
        verbose_name = 'Testimonials'
        verbose_name_plural = 'Testimonials'



class LandingPage(models.Model):
    title = models.CharField(max_length=250, db_index=True)
    hero_image = models.ImageField(upload_to='landing_page/', null=True, blank=True)
    hero_text = models.TextField(null=True, blank=True)
    about_section = models.ForeignKey(AboutUs, on_delete=models.SET_NULL, null=True, blank=True, related_name='alanding_pages')
    featured_campaigns = models.ManyToManyField(Campaigns, related_name='cfeatured_on_landing', blank=True)
    testimonials = models.ManyToManyField(Testimonials, related_name='tfeatured_on_landing', blank=True)
    socials_links = models.ManyToManyField(Socials, related_name='sfeatured_on_landing', blank=True)
    contact_form = models.ForeignKey(ContactForm, on_delete=models.SET_NULL, related_name='clanding_pages', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    meta_description = models.CharField(max_length=300, null=True, blank=True)


    def __str__(self):
        return self.title

    def clean(self):
        if self.meta_description and len(self.meta_description) > 300:
            raise ValidationError("Meta description can't be longer than 300 characters.")
        super().clean()

    class Meta:
        verbose_name = 'Landing Page'
        verbose_name_plural = 'Landing Pages'