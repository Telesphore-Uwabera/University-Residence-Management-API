from django.contrib import admin
from .models import Building, Room, Resident, MaintenanceRequest, Event, Announcement, Communication, RegistrationForResident, Payment

class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')  

class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'building', 'type', 'is_occupied')  
    list_filter = ('building', 'type', 'is_occupied') 

class ResidentAdmin(admin.ModelAdmin):
    list_display = ('user', 'room')  
    search_fields = ('user_username', 'room_number') 

class MaintenanceRequestAdmin(admin.ModelAdmin):
    list_display = ('issue', 'location', 'priority', 'status', 'created_at')  
    list_filter = ('priority', 'status')  

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location') 
    search_fields = ('title', 'location__name')  

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  

class CommunicationAdmin(admin.ModelAdmin):
    list_display = ('resident', 'message', 'created_at')  
class RegistrationForResidentAdmin(admin.ModelAdmin):
    list_display = ('resident', 'room', 'status', 'application_date')  
    list_filter = ('status',)  

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('resident', 'month', 'year', 'amount', 'payment_date') 
    list_filter = ('month', 'year')  
    search_fields = ('resident_user_username',)  

admin.site.register(Building, BuildingAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Resident, ResidentAdmin)
admin.site.register(MaintenanceRequest, MaintenanceRequestAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Communication, CommunicationAdmin)
admin.site.register(RegistrationForResident, RegistrationForResidentAdmin)
admin.site.register(Payment, PaymentAdmin)