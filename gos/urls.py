from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from gosuslugi import views as gosuslugi_views


router = routers.DefaultRouter()
router.register(r'polzovateli', gosuslugi_views.PolzovateliViewSet)
router.register(r'uslugi', gosuslugi_views.UslugiViewSet)
router.register(r'zayavkipolz', gosuslugi_views.ZayavkiPolzViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('addUsl/', gosuslugi_views.create_usluga),
    path('addPolz/', gosuslugi_views.create_polzovatel),
    path('addZay/', gosuslugi_views.create_zayavka),
    path('delPolz/<int:id>/', gosuslugi_views.delPozl),
    path('delUsl/<int:id>/', gosuslugi_views.delUsl),
    path('delZay/<int:id>/', gosuslugi_views.delZay),
    path('statusZayCh/<int:id>/', gosuslugi_views.statusZayChange),
    path('uslugiCh/<int:id>/', gosuslugi_views.uslugiChange),
    path('statusZayChUser/<int:id>/', gosuslugi_views.statusZayChangeUser),
]
