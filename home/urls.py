from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'departments', views.DepartmentViewSet)
router.register(r'programs', views.ProgramViewSet)
router.register(r'teachers', views.TeacherViewSet)
router.register(r'rooms', views.RoomViewSet)
router.register(r'subjects', views.SubjectsViewSet)
router.register(r'batch', views.BatchViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'timeslots', views.TimeslotViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]