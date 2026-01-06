from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'system'

urlpatterns = [

    path('api/upload/', views.upload_vehicle_data, name='upload_vehicle_data'),
    path('api/my-vehicles/', views.my_vehicles, name='my_vehicles'),
    path('',views.user_login,name='login'),
    path('layer/',views.layer,name='layer'),
    path('home/',views.home,name='home'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('users/<int:vehicle_id>/',views.vehicle_details,name='vehicleid'),
    path('map/',views.map,name='map'),
    path('trans/',views.transanction,name='transanction'),
    path('signup/',views.RegisterUser,name='signup'),
    path('register/',views.Register2,name='register2'),
    path('info/',views.info,name='info'),
    path('finish/',views.finish_page,name='finish'),
    path('landing/',views.landing_page,name='landing'),
    path('cancel/',views.cancel_reg,name='cancel'),
    path('logout/',views.logoutUser,name='logout'),
    
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
