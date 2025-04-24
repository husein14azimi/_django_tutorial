from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('temp/', views.temp),
    path('person/', views.persons),
    path('person/<int:id>/', views.person),
    

    path('app2/', include('app2.urls')),
    path('api/', include('api.urls')),
] + debug_toolbar_urls()
