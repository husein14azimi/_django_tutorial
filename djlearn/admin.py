from django.contrib import admin
from .models import Person, OwnerFamily, Holding, Company


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Person._meta.fields
    ]




@admin.register(OwnerFamily)
class OwnerFamilyAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in OwnerFamily._meta.fields
    ]

@admin.register(Holding)
class HoldingAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Holding._meta.fields
    ]

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Company._meta.fields
    ]
    list_per_page = 1