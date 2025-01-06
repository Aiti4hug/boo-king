from rest_framework import permissions


class CheckUserRating(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.profile

class Client(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.status_user == 'client':
            return True
        return False


class CheckHotelUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.hotel_owner


class CheckBooking(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.status_user == 'client':
            return True
        return False

class CheckBookingUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.user

