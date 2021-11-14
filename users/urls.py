from django.contrib import admin
from django.urls import path ,include
from django.conf.urls.static import static
from django.conf import settings
from users import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name='home'
urlpatterns = [
    path('',views.user,name="profile"),

]
urlpatterns+= staticfiles_urlpatterns()          
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)