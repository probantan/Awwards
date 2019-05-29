from  django.conf.urls import url


from . import views 
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.models import User

urlpatterns=[
    url(r'^$', views.home, name='home'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^update/profile$', views.updateprofile, name='updateprofile'),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    url(r'^upload/$', views.upload_project, name='upload_project'),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

