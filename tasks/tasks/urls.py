from django.contrib import admin
from django.urls import path
from registration.views import login_view,logout_view,register_view,map_view,MapPDFView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('map/', map_view, name='map'),
    path('map/pdf/', MapPDFView.as_view(), name='map_pdf'),
]
