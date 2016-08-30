from django.conf.urls import patterns, url, include
from rest_framework import routers
import api
import views

router = routers.DefaultRouter()
router.register(r'carname', api.carNameViewSet)
router.register(r'manufacturer', api.ManufacturerViewSet)


urlpatterns = patterns('',
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += patterns('',
    # urls for carName
    url(r'^car/carname/$', views.carNameListView.as_view(), name='car_carname_list'),
    url(r'^car/carname/create/$', views.carNameCreateView.as_view(), name='car_carname_create'),
    url(r'^car/carname/detail/(?P<slug>\S+)/$', views.carNameDetailView.as_view(), name='car_carname_detail'),
    url(r'^car/carname/update/(?P<slug>\S+)/$', views.carNameUpdateView.as_view(), name='car_carname_update'),
)

urlpatterns += patterns('',
    # urls for Manufacturer
    url(r'^car/manufacturer/$', views.ManufacturerListView.as_view(), name='car_manufacturer_list'),
    url(r'^car/manufacturer/create/$', views.ManufacturerCreateView.as_view(), name='car_manufacturer_create'),
    url(r'^car/manufacturer/detail/(?P<slug>\S+)/$', views.ManufacturerDetailView.as_view(), name='car_manufacturer_detail'),
    url(r'^car/manufacturer/update/(?P<slug>\S+)/$', views.ManufacturerUpdateView.as_view(), name='car_manufacturer_update'),
)

