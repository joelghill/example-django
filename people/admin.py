from django.contrib import admin
from django.contrib.admin.decorators import register
from people.models import Person, Address


@register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')


@register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'city', 'postal_code')