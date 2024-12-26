from django.contrib import admin
from page.models.api_models import *
from page.models.page_models import *
from page.models.user_models import *




# inlines 
class TestimonialsInline(admin.TabularInline):  # or use admin.StackedInline for a different layout
    model = Testimonials
    extra = 1  # Number of empty forms to display by default
    fields = ('name', 'content', 'campaign', 'video', 'created_at')
    readonly_fields = ('created_at',)  # Make certain fields read-only in the inline admin


# Custom admin class for Socials model
@admin.register(Socials)
class SocialsAdmin(admin.ModelAdmin):
    list_display = ('platform_name', 'title', 'slug', 'created_at', 'updated_at')
    search_fields = ('platform_name', 'title', 'slug')
    list_filter = ('platform_name', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created_at',)

# Custom admin class for AboutUs model
@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at')
    search_fields = ('mission', 'team')
    ordering = ('-created_at',)





# Custom admin class for Campaigns model



@admin.register(Campaigns)
class CampaignsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'slug', 'created_at', 'updated_at')
    search_fields = ('title', 'author__username', 'slug')
    list_filter = ('author', 'created_at', 'category')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created_at',)
    inlines = [TestimonialsInline]  # Add the inline model to the Campaigns admin




# Custom admin class for ContactForm model
@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    ordering = ('-created_at',)

# Custom admin class for Testimonials model


@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('name', 'campaign', 'created_at')
    search_fields = ('name', 'content', 'campaign__title')
    list_filter = ('campaign', 'created_at')
    ordering = ('-created_at',)

# Custom admin class for LandingPage model
@admin.register(LandingPage)
class LandingPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'hero_text')
    filter_horizontal = ('featured_campaigns', 'testimonials', 'socials_links')
    ordering = ('-created_at',)
