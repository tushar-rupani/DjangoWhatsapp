from django.urls import path
from .views import *

urlpatterns = [

	path('', home, name="home-view"),
	path('send/', send_message, name="send-view"),
	path('hand/', hand, name="hand-view"),
	path('hand-convert/', hand_convert, name="hand-convert"),
	

]