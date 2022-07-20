
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('', views.home, name='home_url'),
    path('about/', views.about, name='about_url'),
    path('blog/', views.blog, name='blog_url'),
    path('contact/', views.contact, name='contact_url'),
    path('blogSingle/<int:id>/', views.blogSingle, name='blogSingle_url'),

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
