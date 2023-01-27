
from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =	 [
	path('', views.main, name="main"),
	path('user_page/', views.ShowUserPageView.as_view(), name="user_page"),
	path('registration/', views.register, name="registration"),
	path('admin/', admin.site.urls, name='admin'),
	#path('login/', views.login, name="login"),
]
if settings.DEBUG:
	urlpatterns +=	static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
