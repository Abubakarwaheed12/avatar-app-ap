from rest_framework import serializers
from user.models import User, Add_Appointment


class UserRegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'tc', 'password', 'image']
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



class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    image = serializers.ImageField(required=False)
    email = serializers.EmailField(max_length=255, required=False)

    class Meta:
        model = User
        fields = ['email','first_name', 'last_name', 'phone', 'image', 'password', 'confirm_password']

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.image = validated_data.get('image', instance.image)

        password = validated_data.get('password')
        confirm_password = validated_data.get('confirm_password')
        if password or confirm_password:
            if not (password and confirm_password):
                raise serializers.ValidationError("Both password and confirm_password are required.")
            elif password != confirm_password:
                raise serializers.ValidationError("Passwords do not match.")
            else:
                instance.set_password(password)

        instance.save()
        return instance
