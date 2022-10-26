from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('admin/', admin.site.urls),
   #path('accounts/', include('django.contrib.auth.urls')),
   #path("accounts/", include("accounts.urls")),
   path("accounts/", include("allauth.urls")),
   path('pages/', include('django.contrib.flatpages.urls')),
   # Делаем так, чтобы все адреса из нашего приложения (simpleapp/urls.py)
   # подключались к главному приложению с префиксом products/.
   path('news/', include('simpleapp.urls')),
   ]