import logging
from django.http import JsonResponse

# Configure logging
logger = logging.getLogger(__name__)

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import logging
from .encryption import encrypt_data, decrypt_data
from .anonymization import anonymize_data
from rest_framework import viewsets
from .models import Building, Room, Resident, MaintenanceRequest, Event, Announcement, Communication, Resident, Payment
from .serializers import (
    BuildingSerializer, RoomSerializer, ResidentSerializer,
    MaintenanceRequestSerializer, EventSerializer, AnnouncementSerializer,
    SignupSerializer, LoginSerializer,
    PaymentSerializer,
    RegistrationForResidentSerializer,
    CommunicationSerializer
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema

# ViewSets for the models

@swagger_auto_schema(
    operation_summary="List all buildings",
    operation_description="Retrieve a list of all buildings."
)
class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

    @swagger_auto_schema(
        operation_summary="Create a new building",
        operation_description="Create a new building in the system.",
        request_body=BuildingSerializer,
        responses={status.HTTP_201_CREATED: BuildingSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a building",
        operation_description="Retrieve a specific building by its ID.",
        responses={status.HTTP_200_OK: BuildingSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a building",
        operation_description="Update an existing building.",
        request_body=BuildingSerializer,
        responses={status.HTTP_200_OK: BuildingSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partial update a building",
        operation_description="Partially update a building.",
        request_body=BuildingSerializer,
        responses={status.HTTP_200_OK: BuildingSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a building",
        operation_description="Delete a specific building by its ID."
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    @swagger_auto_schema(
        operation_summary="List all rooms",
        operation_description="Retrieve a list of all rooms."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new room",
        operation_description="Create a new room in the system.",
        request_body=RoomSerializer,
        responses={status.HTTP_201_CREATED: RoomSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a room",
        operation_description="Retrieve a specific room by its ID.",
        responses={status.HTTP_200_OK: RoomSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a room",
        operation_description="Update an existing room.",
        request_body=RoomSerializer,
        responses={status.HTTP_200_OK: RoomSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partial update a room",
        operation_description="Partially update a room.",
        request_body=RoomSerializer,
        responses={status.HTTP_200_OK: RoomSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a room",
        operation_description="Delete a specific room by its ID."
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

# class RoomViewSet(viewsets.ModelViewSet):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer


class ResidentViewSet(viewsets.ModelViewSet):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer

    @swagger_auto_schema(
        operation_summary="List all residents",
        operation_description="Retrieve a list of all residents."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new resident",
        operation_description="Create a new resident in the system.",
        request_body=ResidentSerializer,
        responses={status.HTTP_201_CREATED: ResidentSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a resident",
        operation_description="Retrieve a specific resident by its ID.",
        responses={status.HTTP_200_OK: ResidentSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a resident",
        operation_description="Update an existing resident.",
        request_body=ResidentSerializer,
        responses={status.HTTP_200_OK: ResidentSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partial update a resident",
        operation_description="Partially update a resident.",
        request_body=ResidentSerializer,
        responses={status.HTTP_200_OK: ResidentSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a resident",
        operation_description="Delete a specific resident by its ID."
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class ResidentViewSet(viewsets.ModelViewSet):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer

    @swagger_auto_schema(
        operation_description="Get anonymized list of residents",
        responses={200: 'A list of anonymized residents'}
    )
    @action(detail=False, methods=['get'])
    def anonymized(self, request):
        residents = Resident.objects.all().values('room__number')
        anonymized_residents = [{'room_number': res['room__number']} for res in residents]
        return Response(anonymized_residents)

class MaintenanceRequestViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceRequest.objects.all()
    serializer_class = MaintenanceRequestSerializer

    @swagger_auto_schema(
        operation_summary="List all maintenance requests",
        operation_description="Retrieve a list of all maintenance requests."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new maintenance request",
        operation_description="Create a new maintenance request in the system.",
        request_body=MaintenanceRequestSerializer,
        responses={status.HTTP_201_CREATED: MaintenanceRequestSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a maintenance request",
        operation_description="Retrieve a specific maintenance request by its ID.",
        responses={status.HTTP_200_OK: MaintenanceRequestSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a maintenance request",
        operation_description="Update an existing maintenance request.",
        request_body=MaintenanceRequestSerializer,
        responses={status.HTTP_200_OK: MaintenanceRequestSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partial update a maintenance request",
        operation_description="Partially update a maintenance request.",
        request_body=MaintenanceRequestSerializer,
        responses={status.HTTP_200_OK: MaintenanceRequestSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a maintenance request",
        operation_description="Delete a specific maintenance request by its ID."
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
# class MaintenanceRequestViewSet(viewsets.ModelViewSet):
#     queryset = MaintenanceRequest.objects.all()
#     serializer_class = MaintenanceRequestSerializer
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @swagger_auto_schema(
        operation_summary="List all events",
        operation_description="Retrieve a list of all events."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new event",
        operation_description="Create a new event in the system.",
        request_body=EventSerializer,
        responses={status.HTTP_201_CREATED: EventSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve an event",
        operation_description="Retrieve a specific event by its ID.",
        responses={status.HTTP_200_OK: EventSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update an event",
        operation_description="Update an existing event.",
        request_body=EventSerializer,
        responses={status.HTTP_200_OK: EventSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partial update an event",
        operation_description="Partially update an event.",
        request_body=EventSerializer,
        responses={status.HTTP_200_OK: EventSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete an event",
        operation_description="Delete a specific event by its ID."
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
# class EventViewSet(viewsets.ModelViewSet):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer
class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    @swagger_auto_schema(
        operation_summary="List all announcements",
        operation_description="Retrieve a list of all announcements."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new announcement",
        operation_description="Create a new announcement in the system.",
        request_body=AnnouncementSerializer,
        responses={status.HTTP_201_CREATED: AnnouncementSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve an announcement",
        operation_description="Retrieve a specific announcement by its ID.",
        responses={status.HTTP_200_OK: AnnouncementSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update an announcement",
        operation_description="Update an existing announcement.",
        request_body=AnnouncementSerializer,
        responses={status.HTTP_200_OK: AnnouncementSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partial update an announcement",
        operation_description="Partially update an announcement.",
        request_body=AnnouncementSerializer,
        responses={status.HTTP_200_OK: AnnouncementSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete an announcement",
        operation_description="Delete a specific announcement by its ID."
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

# class AnnouncementViewSet(viewsets.ModelViewSet):
#     queryset = Announcement.objects.all()
#     serializer_class = AnnouncementSerializer

# User ViewSet for registration and login

from drf_yasg import openapi
from django.contrib.auth.models import User
from django.shortcuts import get_list_or_404
from rest_framework.authtoken.models import Token

# class UserViewSet(viewsets.ViewSet):
#     @swagger_auto_schema(
#         operation_summary='Register users',
#         operation_description="Register new users in the system.",
#         request_body=openapi.Schema(
#             type=openapi.TYPE_OBJECT,
#             properties={
#                 'username': openapi.Schema(type=openapi.TYPE_STRING),
#                 'email': openapi.Schema(type=openapi.TYPE_STRING),
#                 'password': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD)
#             },
#             required=['username', 'email', 'password']
#         )
#     )

#     @action(detail=False, methods=['post'])
#     def register(self, request):
#         serializer = SignupSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             user = User.objects.get(username=serializer.data['username'])
#             user.set_password(request.data['password'])
#             user.save()
#             token = Token.objects.create(user = user)
#             return Response({
#                 'status': 'user successful register',
#                 "user":serializer.data,
#                 'token': token.key}, 
#                 status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

#     @swagger_auto_schema(
#         operation_summary='Login users',
#         operation_description="Log in existing users.",
#         request_body=openapi.Schema(
#             type=openapi.TYPE_OBJECT,
#             properties={
#                 'username': openapi.Schema(type=openapi.TYPE_STRING),
#                 'password': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD)
#             },
#             required=['username', 'password']
#         )
#     )
#     @action(detail=False, methods=['post'])
#     def login(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.validated_data['user']
#             user.set_password(request.data['password'])
#             user.save()
#             token, create = Token.objects.get_or_create(user=user)
#             return Response({
#                 'status': 'login successful',
#                 'token': token.key,
#                 'user': LoginSerializer(user).data
#             }, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework.decorators import action
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

class UserViewSet(viewsets.ViewSet):
    # Define the input expected for the Google login in Swagger
    google_token_param = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'access_token': openapi.Schema(type=openapi.TYPE_STRING, description='Google OAuth2 access token'),
        },
        required=['access_token'],
    )

    @swagger_auto_schema(
        operation_summary='Login with Google',
        operation_description="Log in users using Google authentication.",
        request_body=google_token_param,
        responses={200: 'OK', 400: 'Bad Request'},
    )
    @action(detail=False, methods=['post'], url_path='google-login')
    def google_login(self, request):
        # Call GoogleLogin view to handle the request
        response = GoogleLogin.as_view()(request._request)  # Accessing Django's WSGIRequest from DRF's request
        return Response(response.data, status=response.status_code)


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    @swagger_auto_schema(
        operation_summary="List all payments",
        operation_description="Retrieve a list of all payments."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new payment",
        operation_description="Create a new payment in the system.",
        request_body=PaymentSerializer,
        responses={status.HTTP_201_CREATED: PaymentSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a payment",
        operation_description="Retrieve a specific payment by its ID.",
        responses={status.HTTP_200_OK: PaymentSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a payment",
        operation_description="Update an existing payment.",
        request_body=PaymentSerializer,
        responses={status.HTTP_200_OK: PaymentSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partial update a payment",
        operation_description="Partially update a payment.",
        request_body=PaymentSerializer,
        responses={status.HTTP_200_OK: PaymentSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a payment",
        operation_description="Delete a specific payment by its ID."
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


# ViewSet for Communication
class CommunicationViewSet(viewsets.ModelViewSet):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer

    @swagger_auto_schema(
        operation_summary="List all communications",
        operation_description="Retrieve a list of all communications."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new communication",
        operation_description="Create a new communication in the system.",
        request_body=CommunicationSerializer,
        responses={status.HTTP_201_CREATED: CommunicationSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a communication",
        operation_description="Retrieve a specific communication by its ID.",
        responses={status.HTTP_200_OK: CommunicationSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a communication",
        operation_description="Update an existing communication.",
        request_body=CommunicationSerializer,
        responses={status.HTTP_200_OK: CommunicationSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partial update a communication",
        operation_description="Partially update a communication.",
        request_body=CommunicationSerializer,
        responses={status.HTTP_200_OK: CommunicationSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a communication",
        operation_description="Delete a specific communication by its ID."
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


# ViewSet for RegistrationForResident
class RegistrationForResidentViewSet(viewsets.ModelViewSet):
    queryset = Resident.objects.all()  # Assuming this is where the residents are managed
    serializer_class = RegistrationForResidentSerializer  # Assuming you have created this serializer

    @swagger_auto_schema(
        operation_summary="List all resident registrations",
        operation_description="Retrieve a list of all resident registrations."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new resident registration",
        operation_description="Register a new resident in the system.",
        request_body=RegistrationForResidentSerializer,
        responses={status.HTTP_201_CREATED: RegistrationForResidentSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a resident registration",
        operation_description="Retrieve a specific resident registration by its ID.",
        responses={status.HTTP_200_OK: RegistrationForResidentSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a resident registration",
        operation_description="Update an existing resident registration.",
        request_body=RegistrationForResidentSerializer,
        responses={status.HTTP_200_OK: RegistrationForResidentSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partial update a resident registration",
        operation_description="Partially update a resident registration.",
        request_body=RegistrationForResidentSerializer,
        responses={status.HTTP_200_OK: RegistrationForResidentSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a resident registration",
        operation_description="Delete a specific resident registration by its ID."
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_personal_data(request):
    #fetching sensitive data and anonymizing or encrypting
    email = request.user.email
    encrypted_email = encrypt_data(email)
    anonymized_email = anonymize_data(email)

    return JsonResponse({
        'email': email, 
        'encrypted_email': encrypted_email,
        'anonymized_email': anonymized_email
    })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def decrypt_personal_data(request):
    encrypted_email = request.data.get('encrypted_email', '')
    decrypted_email = decrypt_data(encrypted_email)
    
    logger.info(f"User {request.user.username} decrypted email data.")
    
    return JsonResponse({'decrypted_email': decrypted_email})