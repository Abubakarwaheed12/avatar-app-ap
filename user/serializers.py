from rest_framework import serializers
from user.models import User, Add_Appointment


class UserRegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'tc', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        return data
    
    def create(self, data):
        return User.objects.create_user(**data)
    
   
    
class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email', 'password']


class AddAppointmentSerial(serializers.ModelSerializer):
    class Meta:
        model = Add_Appointment
        fields = '__all__'