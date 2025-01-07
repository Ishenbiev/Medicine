from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path

router = DefaultRouter()
router.register(r'user_profiles', UserProfileViewSet)
router.register(r'patient', PatientDetaileProfileViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'records', MedicalRecordViewSet)
router.register(r'feedbacks', FeedbackViewSet)

urlpatterns = [
    path('', DoctorLastViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('<int:pk>/', DoctorDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                              'delete': 'destroy'}), name='product_detail'),
]
