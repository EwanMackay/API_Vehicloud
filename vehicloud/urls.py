from django.urls import path, include
#from .views import get_sensorData
from rest_framework import routers
from . import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'sensorDatas', views.sensorDataViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/',admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


#urlpatterns = [
#path('sensorData/<int:id>/', get_sensorData)  	
#]'''