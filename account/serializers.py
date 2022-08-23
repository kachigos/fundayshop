# from rest_framework import serializers
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.tokens import RefreshToken, TokenError
#
# from django.contrib.auth import get_user_model, authenticate
# from django.utils.translation import gettext_lazy as _
#
# User = get_user_model()
#
#
# class RegisterSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(min_length=6, max_length=100, required=True, write_only=True)
#     password = serializers.CharField(min_length=6, max_length=100, required=True, write_only=True)
#
#     class Meta:
#         model = User
#         fields = ('email', 'password', 'password2')
#
#     def validate(self, attrs):
#         password2 = attrs.pop('password2')
#         if attrs.get('password') != password2:
#             raise serializers.ValidationError('Passwords did not match!')
#         if not attrs.get('password').isalnum():
#             raise serializers.ValidationError('Password field must be contain alpha symbols and numbers!')
#         return attrs
#
#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user
#
#
# class LoginSerializer(TokenObtainPairSerializer):
#     password = serializers.CharField(min_length=6, write_only=True)
#
#     def validate(self, attrs):
#         email = attrs.get('email')
#         password = attrs.pop('password')
#         if not User.objects.filter(email=email).exists():
#             raise serializers.ValidationError('User not found')
#         user = authenticate(email=email, password=password)
#         if user and user.is_active:
#             refresh = self.get_token(user)
#             attrs['refresh'] = str(refresh)
#             attrs['access'] = str(refresh.access_token)
#         else:
#             raise serializers.ValidationError('Invalid password!')
#         return attrs
#
#
# class LogoutSerializer(serializers.Serializer):
#     refresh = serializers.CharField()
#     default_error_messages = {
#         'bad_token': _('Token is invalid or expired!')
#     }
#
#     def validate(self, attrs):
#         self.token = attrs['refresh']
#         return attrs
#
#     def save(self, **kwargs):
#         try:
#             RefreshToken(self.token).blacklist()
#         except TokenError:
#             self.fail('bad_token')