from rest_framework import viewsets
from rest_framework.response import Response
from .models import Building, Room, Resident, MaintenanceRequest, Event, Announcement, Communication, Resident, Payment, RegistrationForResident
from .serializers import (
    BuildingSerializer, RoomSerializer, ResidentSerializer,
    MaintenanceRequestSerializer, EventSerializer, AnnouncementSerializer,
    SignupSerializer, LoginSerializer,
    PaymentSerializer,
    RegistrationForResidentSerializer,
    CommunicationSerializer
)
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated


# ViewSets for the models

@swagger_auto_schema(
    operation_summary="List all buildings",
    operation_description="Retrieve a list of all buildings."
)


@method_decorator(csrf_exempt, name='dispatch')
class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    permission_classes = [permissions.IsAuthenticated]  

    @swagger_auto_schema(
        operation_summary="List all buildings",
        operation_description="Retrieve a list of all buildings."
    )
    def list(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print(f"Authenticated user: {request.user.username}")
        else:
            print("User is not authenticated")
        
        buildings = self.queryset
        serializer = self.get_serializer(buildings, many=True)
        return Response({
            "message": "Buildings retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Create a new building",
        operation_description="Create a new building in the system.",
        request_body=BuildingSerializer,
        responses={status.HTTP_201_CREATED: BuildingSerializer}
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            "message": "Building created successfully.",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_summary="Retrieve a building",
        operation_description="Retrieve a specific building by its ID.",
        responses={status.HTTP_200_OK: BuildingSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        building = self.get_object()
        serializer = self.get_serializer(building)
        return Response({
            "message": "Building retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Update a building",
        operation_description="Update an existing building.",
        request_body=BuildingSerializer,
        responses={status.HTTP_200_OK: BuildingSerializer}
    )
    def update(self, request, *args, **kwargs):
        building = self.get_object()
        serializer = self.get_serializer(building, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "message": "Building updated successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Partial update a building",
        operation_description="Partially update a building.",
        request_body=BuildingSerializer,
        responses={status.HTTP_200_OK: BuildingSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        building = self.get_object()
        serializer = self.get_serializer(building, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "message": "Building partially updated successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Delete a building",
        operation_description="Delete a specific building by its ID."
    )
    def destroy(self, request, *args, **kwargs):
        building = self.get_object()
        self.perform_destroy(building)
        return Response({
            "message": "Building deleted successfully."
        }, status=status.HTTP_204_NO_CONTENT)

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]  

    @swagger_auto_schema(
        operation_summary="List all rooms",
        operation_description="Retrieve a list of all rooms."
    )
    def list(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print(f"Authenticated user: {request.user.username}")
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
    

class ResidentViewSet(viewsets.ModelViewSet):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer
    permission_classes = [permissions.IsAuthenticated]  

    @swagger_auto_schema(
        operation_summary="List all residents",
        operation_description="Retrieve a list of all residents."
    )
    def list(self, request, *args, **kwargs):
        residents = self.queryset
        serializer = self.get_serializer(residents, many=True)
        return Response({
            "message": "Residents retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Create a new resident",
        operation_description="Create a new resident in the system.",
        request_body=ResidentSerializer,
        responses={status.HTTP_201_CREATED: ResidentSerializer}
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            "message": "Resident created successfully.",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_summary="Retrieve a resident",
        operation_description="Retrieve a specific resident by its ID.",
        responses={status.HTTP_200_OK: ResidentSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        resident = self.get_object()
        serializer = self.get_serializer(resident)
        return Response({
            "message": "Resident retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Update a resident",
        operation_description="Update an existing resident.",
        request_body=ResidentSerializer,
        responses={status.HTTP_200_OK: ResidentSerializer}
    )
    def update(self, request, *args, **kwargs):
        resident = self.get_object()
        serializer = self.get_serializer(resident, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "message": "Resident updated successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Partial update a resident",
        operation_description="Partially update a resident.",
        request_body=ResidentSerializer,
        responses={status.HTTP_200_OK: ResidentSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        resident = self.get_object()
        serializer = self.get_serializer(resident, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "message": "Resident partially updated successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Delete a resident",
        operation_description="Delete a specific resident by its ID."
    )
    def destroy(self, request, *args, **kwargs):
        resident = self.get_object()
        self.perform_destroy(resident)
        return Response({
            "message": "Resident deleted successfully."
        }, status=status.HTTP_204_NO_CONTENT)



class MaintenanceRequestViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceRequest.objects.all()
    serializer_class = MaintenanceRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

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
    

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]  

    @swagger_auto_schema(
        operation_summary="List all events",
        operation_description="Retrieve a list of all events."
    )
    def list(self, request, *args, **kwargs):
        events = self.queryset
        serializer = self.get_serializer(events, many=True)
        return Response({
            "message": "Events retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Create a new event",
        operation_description="Create a new event in the system.",
        request_body=EventSerializer,
        responses={status.HTTP_201_CREATED: EventSerializer}
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            "message": "Event created successfully.",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_summary="Retrieve an event",
        operation_description="Retrieve a specific event by its ID.",
        responses={status.HTTP_200_OK: EventSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        event = self.get_object()
        serializer = self.get_serializer(event)
        return Response({
            "message": "Event retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Update an event",
        operation_description="Update an existing event.",
        request_body=EventSerializer,
        responses={status.HTTP_200_OK: EventSerializer}
    )
    def update(self, request, *args, **kwargs):
        event = self.get_object()
        serializer = self.get_serializer(event, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "message": "Event updated successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Partial update an event",
        operation_description="Partially update an event.",
        request_body=EventSerializer,
        responses={status.HTTP_200_OK: EventSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        event = self.get_object()
        serializer = self.get_serializer(event, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "message": "Event partially updated successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Delete an event",
        operation_description="Delete a specific event by its ID."
    )
    def destroy(self, request, *args, **kwargs):
        event = self.get_object()
        self.perform_destroy(event)
        return Response({
            "message": "Event deleted successfully."
        }, status=status.HTTP_204_NO_CONTENT)

class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [permissions.IsAuthenticated] 

    @swagger_auto_schema(
        operation_summary="List all announcements",
        operation_description="Retrieve a list of all announcements."
    )
    def list(self, request, *args, **kwargs):
        announcements = self.queryset
        serializer = self.get_serializer(announcements, many=True)
        return Response({
            "message": "Announcements retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Create a new announcement",
        operation_description="Create a new announcement in the system.",
        request_body=AnnouncementSerializer,
        responses={status.HTTP_201_CREATED: AnnouncementSerializer}
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            "message": "Announcement created successfully.",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_summary="Retrieve an announcement",
        operation_description="Retrieve a specific announcement by its ID.",
        responses={status.HTTP_200_OK: AnnouncementSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        announcement = self.get_object()
        serializer = self.get_serializer(announcement)
        return Response({
            "message": "Announcement retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Update an announcement",
        operation_description="Update an existing announcement.",
        request_body=AnnouncementSerializer,
        responses={status.HTTP_200_OK: AnnouncementSerializer}
    )
    def update(self, request, *args, **kwargs):
        announcement = self.get_object()
        serializer = self.get_serializer(announcement, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "message": "Announcement updated successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Partial update an announcement",
        operation_description="Partially update an announcement.",
        request_body=AnnouncementSerializer,
        responses={status.HTTP_200_OK: AnnouncementSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        announcement = self.get_object()
        serializer = self.get_serializer(announcement, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "message": "Announcement partially updated successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Delete an announcement",
        operation_description="Delete a specific announcement by its ID."
    )
    def destroy(self, request, *args, **kwargs):
        announcement = self.get_object()
        self.perform_destroy(announcement)
        return Response({
            "message": "Announcement deleted successfully."
        }, status=status.HTTP_204_NO_CONTENT)
    
    

from drf_yasg import openapi
from django.contrib.auth.models import User
from django.shortcuts import get_list_or_404
from rest_framework.authtoken.models import Token
from drf_yasg.views import get_schema_view

swagger_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'Authorization': openapi.Schema(type=openapi.TYPE_STRING, description='Token required to access this endpoint (e.g., Token <your_token>)'),
    },
)

security_schema = {
    'Authorization': {
        'type': 'apiKey',
        'name': 'Authorization',
        'in': 'header',
        'description': 'Token required to access this endpoint (e.g., Token <your_token>)',
    }
}

# Create schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Your API Title",
        default_version='v1',
        description="API description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

schema_view.security = [{'Authorization': []}]  



class UserViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    @swagger_auto_schema(
        operation_summary='Register users',
        operation_description="Register new users in the system.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'email': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD)
            },
            required=['username', 'email', 'password']
        )
    )

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=serializer.data['username'])
            user.set_password(request.data['password'])
            user.save()
            token = Token.objects.create(user = user)
            return Response({
                'status': 'user successful register',
                "user":serializer.data,
                'token': token.key}, 
                status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary='Login users',
        operation_description="Log in existing users.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD)
            },
            required=['username', 'password']
        )
    )
    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            user.set_password(request.data['password'])
            user.save()
            token, create = Token.objects.get_or_create(user=user)
            return Response({
                'status': 'login successful',
                'token': token.key,
                'user': LoginSerializer(user).data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="List all payments",
        operation_description="Retrieve a list of all payments.",
        responses={status.HTTP_200_OK: PaymentSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print(f"Authenticated user: {request.user.username}")
        else:
            print("User is not authenticated")
        payments = self.get_queryset()
        serializer = self.get_serializer(payments, many=True)
        return Response({"message": "Payments retrieved successfully.", "data": serializer.data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Create a new payment",
        operation_description="Create a new payment in the system.",
        request_body=PaymentSerializer,
        responses={
            status.HTTP_201_CREATED: PaymentSerializer,
            status.HTTP_400_BAD_REQUEST: "Bad Request - Invalid input"
        }
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        payment = serializer.save()
        return Response({"message": "Payment created successfully.", "data": PaymentSerializer(payment).data}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_summary="Retrieve a payment",
        operation_description="Retrieve a specific payment by its ID.",
        responses={
            status.HTTP_200_OK: PaymentSerializer,
            status.HTTP_404_NOT_FOUND: "Not Found - Payment does not exist"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        payment = self.get_object()
        serializer = self.get_serializer(payment)
        return Response({"message": "Payment retrieved successfully.", "data": serializer.data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Update a payment",
        operation_description="Update an existing payment.",
        request_body=PaymentSerializer,
        responses={
            status.HTTP_200_OK: PaymentSerializer,
            status.HTTP_400_BAD_REQUEST: "Bad Request - Invalid input",
            status.HTTP_404_NOT_FOUND: "Not Found - Payment does not exist"
        }
    )
    def update(self, request, *args, **kwargs):
        payment = self.get_object()
        serializer = self.get_serializer(payment, data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_payment = serializer.save()
        return Response({"message": "Payment updated successfully.", "data": PaymentSerializer(updated_payment).data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Partially update a payment",
        operation_description="Partially update a payment.",
        request_body=PaymentSerializer,
        responses={
            status.HTTP_200_OK: PaymentSerializer,
            status.HTTP_400_BAD_REQUEST: "Bad Request - Invalid input",
            status.HTTP_404_NOT_FOUND: "Not Found - Payment does not exist"
        }
    )
    def partial_update(self, request, *args, **kwargs):
        payment = self.get_object()
        serializer = self.get_serializer(payment, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated_payment = serializer.save()
        return Response({"message": "Payment partially updated successfully.", "data": PaymentSerializer(updated_payment).data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Delete a payment",
        operation_description="Delete a specific payment by its ID.",
        responses={
            status.HTTP_204_NO_CONTENT: "No Content - Payment deleted successfully",
            status.HTTP_404_NOT_FOUND: "Not Found - Payment does not exist"
        }
    )
    def destroy(self, request, *args, **kwargs):
        payment = self.get_object()
        payment.delete()
        return Response({"message": "Payment deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

# ViewSet for Communication
class CommunicationViewSet(viewsets.ModelViewSet):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer
    permission_classes = [permissions.IsAuthenticated]  

    @swagger_auto_schema(
        operation_summary="List all communications",
        operation_description="Retrieve a list of all communications."
    )
    def list(self, request, *args, **kwargs):
        communications = self.queryset
        serializer = self.get_serializer(communications, many=True)
        return Response({
            "message": "Communications retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Create a new communication",
        operation_description="Create a new communication in the system.",
        request_body=CommunicationSerializer,
        responses={status.HTTP_201_CREATED: CommunicationSerializer}
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            "message": "Communication created successfully.",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_summary="Retrieve a communication",
        operation_description="Retrieve a specific communication by its ID.",
        responses={status.HTTP_200_OK: CommunicationSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        communication = self.get_object()
        serializer = self.get_serializer(communication)
        return Response({
            "message": "Communication retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Update a communication",
        operation_description="Update an existing communication.",
        request_body=CommunicationSerializer,
        responses={status.HTTP_200_OK: CommunicationSerializer}
    )
    def update(self, request, *args, **kwargs):
        communication = self.get_object()
        serializer = self.get_serializer(communication, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "message": "Communication updated successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Partial update a communication",
        operation_description="Partially update a communication.",
        request_body=CommunicationSerializer,
        responses={status.HTTP_200_OK: CommunicationSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        communication = self.get_object()
        serializer = self.get_serializer(communication, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "message": "Communication partially updated successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Delete a communication",
        operation_description="Delete a specific communication by its ID."
    )
    def destroy(self, request, *args, **kwargs):
        communication = self.get_object()
        self.perform_destroy(communication)
        return Response({
            "message": "Communication deleted successfully."
        }, status=status.HTTP_204_NO_CONTENT)
    

from rest_framework.permissions import IsAuthenticated

class RegistrationForResidentViewSet(viewsets.ModelViewSet):
    queryset = RegistrationForResident.objects.all()
    serializer_class = RegistrationForResidentSerializer
    permission_classes = [IsAuthenticated]  

    @swagger_auto_schema(
        operation_summary="List all resident registrations",
        operation_description="Retrieve a list of all resident registrations.",
        responses={status.HTTP_200_OK: RegistrationForResidentSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        registrations = self.get_queryset()
        serializer = self.get_serializer(registrations, many=True)
        return Response({"message": "Resident registrations retrieved successfully.", "data": serializer.data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Create a new resident registration",
        operation_description="Register a new resident in the system.",
        request_body=RegistrationForResidentSerializer,
        responses={
            status.HTTP_201_CREATED: RegistrationForResidentSerializer,
            status.HTTP_400_BAD_REQUEST: "Bad Request - Invalid input"
        }
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        registration = serializer.save()  
        return Response({"message": "Resident registration created successfully.", "data": RegistrationForResidentSerializer(registration).data}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_summary="Retrieve a resident registration",
        operation_description="Retrieve a specific resident registration by its ID.",
        responses={
            status.HTTP_200_OK: RegistrationForResidentSerializer,
            status.HTTP_404_NOT_FOUND: "Not Found - Registration does not exist"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        registration = self.get_object()  
        serializer = self.get_serializer(registration)
        return Response({"message": "Resident registration retrieved successfully.", "data": serializer.data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Update a resident registration",
        operation_description="Update an existing resident registration.",
        request_body=RegistrationForResidentSerializer,
        responses={
            status.HTTP_200_OK: RegistrationForResidentSerializer,
            status.HTTP_400_BAD_REQUEST: "Bad Request - Invalid input",
            status.HTTP_404_NOT_FOUND: "Not Found - Registration does not exist"
        }
    )
    def update(self, request, *args, **kwargs):
        registration = self.get_object()  
        serializer = self.get_serializer(registration, data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_registration = serializer.save()  
        return Response({"message": "Resident registration updated successfully.", "data": RegistrationForResidentSerializer(updated_registration).data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Partially update a resident registration",
        operation_description="Partially update a resident registration.",
        request_body=RegistrationForResidentSerializer,
        responses={
            status.HTTP_200_OK: RegistrationForResidentSerializer,
            status.HTTP_400_BAD_REQUEST: "Bad Request - Invalid input",
            status.HTTP_404_NOT_FOUND: "Not Found - Registration does not exist"
        }
    )
    def partial_update(self, request, *args, **kwargs):
        registration = self.get_object() 
        serializer = self.get_serializer(registration, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated_registration = serializer.save()  
        return Response({"message": "Resident registration partially updated successfully.", "data": RegistrationForResidentSerializer(updated_registration).data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Delete a resident registration",
        operation_description="Delete a specific resident registration by its ID.",
        responses={
            status.HTTP_204_NO_CONTENT: "No Content - Registration deleted successfully",
            status.HTTP_404_NOT_FOUND: "Not Found - Registration does not exist"
        }
    )
    def destroy(self, request, *args, **kwargs):
        registration = self.get_object() 
        registration.delete()  
        return Response({"message": "Resident registration deleted successfully."}, status=status.HTTP_204_NO_CONTENT)