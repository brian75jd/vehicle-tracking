from django.urls import path
from .import views

app_name='contact'

urlpatterns = [
    path('',views.feedback,name='feedback'),
    path('message/',views.AdminMessages,name='Adminmessage'),
    path('analysis/',views.Analysis,name='analysis'),
    path('track/',views.Live_Tracking,name='liveTrack'),
    path('messages/<int:message_id>/',views.message_details,name='message_detail')
]
