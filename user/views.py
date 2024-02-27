from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from user.serializers import UserRegisterationSerializer, UserLoginSerializer
from django.contrib.auth import authenticate
from user.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Add_Appointment
from .serializers import AddAppointmentSerial


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }

class UserRegisterationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        print(request.data)
        serializer = UserRegisterationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({
                'user': {
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'phone': user.phone
                },
                'msg': 'Registration Successful',
                'token': token,
            }, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        print(request.data)
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({
                    'user': {
                        'email': user.email,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'phone': user.phone
                    },
                    'msg': 'Login Successful',
                    'token': token,
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'errors': {'non_field_errors':['Email or Password is not valid']}
                }, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AddAppointmentView(APIView):
    def get(self, request):
        shop_details = Add_Appointment.objects.all()
        serializer = AddAppointmentSerial(shop_details, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AddAppointmentSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class GetAppointmentByDate(APIView):
    def get(self, request, date):
        appointments = Add_Appointment.objects.filter(Date=date)
        serializer = AddAppointmentSerial(appointments, many=True)
        return Response(serializer.data)
    


    
class DeleteAppointment(APIView):
    def delete(self, request, id):
        try:
            appointment = Add_Appointment.objects.get(id=id)
        except Add_Appointment.DoesNotExist:
            return Response({"error": "Appointment not found"}, status=status.HTTP_404_NOT_FOUND)

        appointment.delete()
        return Response({"message": "Appointment deleted successfully"}, status=status.HTTP_204_NO_CONTENT)