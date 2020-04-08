"""CSV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from csvfile.views import profile_upload,SignUpView,validate_username,TenantAutocomplete, search_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload-csv/', profile_upload, name="profile_upload"),
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^ajax_calls/validate_username/$', validate_username, name='validate_username'),
    url( r'^tenant-autocomplete/$',  TenantAutocomplete.as_view(),name='tenant-autocomplete', ), 
    path('search/', search_view, name='search_view'),
    #url(r'^ajax_calls/search/', autocompleteModel),
]
