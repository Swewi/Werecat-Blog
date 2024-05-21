from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("gallery/", include(gallery.urls), name="gallery-urls"),
    path("contact/", include("contact.urls"), name="contact-urls"),
    path("about/", include("about.urls"), name="about-urls"),
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path("", include("blog.urls"), name="blog-urls"),   
]