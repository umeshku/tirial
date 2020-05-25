from django.contrib import admin
from .models import Household, Personal



# Register your models here.



class ChoiceInline(admin.TabularInline):
    model = Personal
    extra = 1

class HouseholdAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]



admin.site.register(Household, HouseholdAdmin)
