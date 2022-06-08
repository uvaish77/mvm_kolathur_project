from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home-page"),
    path('about_us', views.aboutus, name="about-us"),
    path('admission_us', views.admission, name="admission-us"),
    path('contact_us', views.contactus, name="contact-us"),
    path('fees_us', views.fees, name="fees-us"),
    path('gallery_us', views.gallery, name="gallery-us"),
    path('inclusive_us', views.inclusive, name="inclusive-us"),
    path('matric_us', views.matric, name="matric-us"),
    path('osla_us', views.osla, name="osla-us"),
    path('special_us', views.special, name="special-us"),
    path('sports_us', views.sports, name="sports-us"),
    path('send_email', views.contact, name="send-email"),
    path('matric_enquiry', views.enquirymatric, name="matric-enquiry"),
    path('inclusive_enquiry', views.enquiryinclusive, name="inclusive-enquiry"),

]

urlpatterns += staticfiles_urlpatterns()
