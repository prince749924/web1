from django.urls import path
from  customer import views

urlpatterns =[
    path('',views.homepage),
    path('login',views.login , name = 'login'),
    path('register',views.register ,name = 'register'),
    path('dashboard',views.dashboard ,name = 'dash'),
    path('customerview',views.customerview , name = 'customerview'),
    path('customeradd',views.customeradd),
    path('customeredit/<int:id>',views.customeredit),
    path('customerupdate/<int:id>',views.customerupdate),
    path('customerdelete/<int:id>',views.customerdelete)
    

]