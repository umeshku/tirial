from import_export import resources
from .models import Household, Personal

class PersonalResource(resources.ModelResource):
    class Meta:
        model = Personal
class HouseholdResource(resources.ModelResource):
    class Meta:
        model = Household
