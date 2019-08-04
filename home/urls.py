from django.contrib import admin
from django.urls import path, include
from .views import *
from My_site import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', view_home_page.as_view(), name='homepage'),
    path('about/', view_about_page.as_view(), name='about'),
    path('portofolio/', view_portofolio.as_view(), name='portofolio'),
    path('projects/', view_projects.as_view(), name='projects'),
    path('blog/', my_blog.as_view(), name='blog'),
    path('contact/', view_contact_page.contact_us, name='contact'),

    path('comment/', post_comment, name='comment')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
