"""VetDataHub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from VetDataHub import views
from vdh import views as vdh_views
from registration.backends.simple.views import RegistrationView
from accounts.forms import *
from accounts.views import *

app_name = 'vdh' 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home , name='home'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/register/$', UserFormView.as_view(), name='registration_register'),
 #   url(r'^users/$', vdh_views.user, name='user'),
    url(r'^vpp-edit-profile/$', vdh_views.vpp_edit_profile, name= 'vpp_edit_profile'),
    url(r'^vet-edit-profile/$', vdh_views.vet_edit_profile, name= 'vet_edit_profile'),
    url(r'^med-producer-edit-profile/$', vdh_views.med_producer_edit_profile, name= 'med_producer_edit_profile'),
    url(r'^med-distributer-edit-profile/$', vdh_views.med_distributer_edit_profile, name= 'med_distributer_edit_profile'),
    url(r'^users/dashboard$', vdh_views.dashboard, name='dashboard'),
    url(r'^data/clinical-work-data$', vdh_views.clinical_work_data, name= 'clinical_work_data'),
    url(r'^data/med-prod-data$', vdh_views.med_producer_data, name= 'med_producer_data'),
    url(r'^data/med-dist-data$', vdh_views.med_distributer_data, name= 'med_distributer_data'),

 
]
