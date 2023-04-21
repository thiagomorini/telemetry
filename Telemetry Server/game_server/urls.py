from django.urls import path, include

urlpatterns = [
    path('api/', include('server.urls')),
    path('', include('front.urls'))
]
