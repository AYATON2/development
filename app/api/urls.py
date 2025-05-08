from django.urls import path
from .views import HelloWorld
#from .views import Students
from .views import ContactListView
from .views import ContactUpdateDetailView


urlpatterns = [
 #path('hello/', HelloWorld.as_view(), name='hello_world'),
 path('contact/', ContactListView.as_view(), name='contact_new'),
 #path('students/', Students.as_view(), name='list_students'),
 path('contacts/', ContactListView.as_view(), name='contact_list'),

]
