from django.conf.urls import url
from . import views
from mysite import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', views.post_list, name='post_list')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)