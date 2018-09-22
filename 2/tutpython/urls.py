from django.conf.urls import include, url
from django.contrib import admin
from tutpython import views
 
urlpatterns = [
    url(r'^$', views.reg_redirect, name='reg_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^registration/', include('registration.urls'))
]
