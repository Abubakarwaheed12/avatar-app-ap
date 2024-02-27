from django.urls import path
from user.views import UserRegisterationView, UserLoginView , AddAppointmentView,GetAppointmentByDate,DeleteAppointment, UserProfileView

urlpatterns = [
    path('register/', UserRegisterationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('AddAppointment/', AddAppointmentView.as_view(), name='AddAppointmentView'),
    path('AddAppointment/<str:date>/', GetAppointmentByDate.as_view(), name='get_appointments_by_date'),
    path('delete_appointment/<int:id>/', DeleteAppointment.as_view(), name='delete_appointment'),
]