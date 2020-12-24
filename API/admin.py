from django.contrib import admin
from .models import HeaderImage, Testimonial, Services, ContactUs

# Register your models here.
admin.site.register(HeaderImage)
admin.site.register(Services)
admin.site.register(Testimonial)
admin.site.register(ContactUs)