from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BuildingViewSet, RoomViewSet, ResidentViewSet,
    MaintenanceRequestViewSet, EventViewSet, AnnouncementViewSet,
    UserViewSet,
    CommunicationViewSet,
    RegistrationForResidentViewSet,
    PaymentViewSet
)

router = DefaultRouter()

router.register(r'buildings', BuildingViewSet, basename='building')
router.register(r'rooms', RoomViewSet, basename='room')
router.register(r'residents', ResidentViewSet, basename='resident')
router.register(r'maintenance-requests', MaintenanceRequestViewSet, basename='maintenance_request')
router.register(r'events', EventViewSet, basename='event')
router.register(r'announcements', AnnouncementViewSet, basename='announcement')
router.register(r'communications', CommunicationViewSet, basename='communication')
router.register(r'registrations', RegistrationForResidentViewSet, basename='registration')
router.register(r'payments', PaymentViewSet, basename='payment')

user_actions = UserViewSet.as_view({
    'post': 'register'
})
login_action = UserViewSet.as_view({
    'post': 'login'
})

urlpatterns = [
    path('', include(router.urls)), 
    path('register/', user_actions, name='register'),  
    path('login/', login_action, name='login'),        
]
